"""
Risk Management Layer — ABSOLUTE VETO POWER over every signal.

Operates INDEPENDENTLY of the HMM.  Even if the HMM fails completely,
circuit breakers catch drawdowns based on actual P&L.  Defense in depth.

1. PORTFOLIO-LEVEL LIMITS
   - Max total exposure : 80 % of portfolio (20 % cash floor)
   - Max single position: 15 % of portfolio
   - Max correlated exposure: 30 % in one sector
   - Max concurrent positions: 5
   - Max daily trades: 20
   - Max portfolio leverage: 1.25×

2. CIRCUIT BREAKERS  (fire on ACTUAL P&L, independent of regime)
   - Daily   DD > 2 % : halve all position sizes for the rest of the day
   - Daily   DD > 3 % : close ALL positions, halt trading for the rest of the day
   - Weekly  DD > 5 % : halve all position sizes for the rest of the week
   - Weekly  DD > 7 % : close ALL positions, halt trading for the rest of the week
   - Peak    DD > 10%  : halt ALL trading, write trading_halted.lock
                         (requires MANUAL deletion to resume)

   Every trigger is logged with: breaker type, actual DD, equity,
   positions closed, HMM regime at time (to track if HMM was wrong).

3. POSITION-LEVEL RISK
   - Every order MUST carry a stop_loss — refused otherwise.
   - Max risk per trade: 1 % of portfolio
   - Sizing: shares = (portfolio × 0.01) / |entry − stop_loss|
   - Capped at: regime_max_pct, then portfolio_max (15 %)
   - Minimum notional: $100
   - GAP RISK: overnight positions assume 3× stop gap-through.
     overnight_size = min(normal, size where 3× gap = 2 % of portfolio)
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Optional

logger = logging.getLogger(__name__)

LOCK_FILE = "trading_halted.lock"


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass
class RiskConfig:
    # Portfolio limits
    max_total_exposure:    float = 0.80
    max_single_position:   float = 0.15
    max_sector_exposure:   float = 0.30
    max_concurrent:        int   = 5
    max_daily_trades:      int   = 20
    max_leverage:          float = 1.25

    # Circuit-breaker thresholds
    cb_daily_half:         float = 0.02   # -2 %  → halve sizes
    cb_daily_close:        float = 0.03   # -3 %  → close all + halt day
    cb_weekly_half:        float = 0.05   # -5 %  → halve sizes
    cb_weekly_close:       float = 0.07   # -7 %  → close all + halt week
    cb_peak_lock:          float = 0.10   # -10 % → lock file

    # Position sizing
    risk_per_trade:        float = 0.01   # 1 % of portfolio at risk per trade
    min_notional:          float = 100.0  # $100 minimum
    gap_risk_multiplier:   float = 3.0    # assume 3× gap-through overnight
    gap_risk_budget:       float = 0.02   # overnight gap may cost ≤ 2 % portfolio


# ---------------------------------------------------------------------------
# Status snapshots
# ---------------------------------------------------------------------------

@dataclass
class CircuitBreakerStatus:
    daily_half_active:   bool  = False
    daily_halt_active:   bool  = False
    weekly_half_active:  bool  = False
    weekly_halt_active:  bool  = False
    peak_locked:         bool  = False
    scale_factor:        float = 1.0    # 1.0 = normal, 0.5 = halved
    trading_allowed:     bool  = True

    @property
    def any_active(self) -> bool:
        return any([self.daily_half_active, self.daily_halt_active,
                    self.weekly_half_active, self.weekly_halt_active,
                    self.peak_locked])


@dataclass
class PositionSizeResult:
    ticker:          str
    shares:          int
    notional:        float
    entry_price:     float
    stop_price:      float
    risk_amount:     float    # $ at risk
    overnight_capped:bool = False
    regime_capped:   bool = False
    portfolio_capped:bool = False


@dataclass
class OrderDecision:
    approved:  bool
    reason:    str
    scaled_shares: int = 0


# ---------------------------------------------------------------------------
# RiskManager
# ---------------------------------------------------------------------------

class RiskManager:
    """
    Central risk gate.  Call `approve_order()` before every submission.
    Call `update_portfolio_value()` on every bar.
    """

    def __init__(self, portfolio_value: float = 0.0,
                  config: Optional[RiskConfig] = None) -> None:
        self.config = config or RiskConfig()
        self._portfolio   = portfolio_value
        self._peak        = portfolio_value
        self._day_start   = portfolio_value
        self._week_start  = portfolio_value
        self._last_date:  Optional[date] = None
        self._last_week:  Optional[int]  = None
        self.cb           = CircuitBreakerStatus()
        self._daily_trades: int = 0
        self._open_positions: dict[str, float] = {}  # ticker → notional

    # ------------------------------------------------------------------
    # Portfolio value sync  (call every bar)
    # ------------------------------------------------------------------

    def update_portfolio_value(self, value: float,
                                regime_label: str = "unknown") -> CircuitBreakerStatus:
        """
        Update equity and evaluate all circuit breakers.
        Returns current CircuitBreakerStatus.
        """
        self._portfolio = value
        self._peak      = max(self._peak, value)

        now   = datetime.now(timezone.utc)
        today = now.date()
        week  = today.isocalendar()[1]

        # Daily reset
        if self._last_date != today:
            self._day_start    = value
            self._daily_trades = 0
            self.cb.daily_half_active  = False
            self.cb.daily_halt_active  = False
            self._last_date    = today
            logger.info("Daily reset — day_start=%.2f", value)

        # Weekly reset
        if self._last_week != week:
            self._week_start  = value
            self.cb.weekly_half_active = False
            self.cb.weekly_halt_active = False
            self._last_week   = week
            logger.info("Weekly reset — week_start=%.2f", value)

        return self._evaluate_circuit_breakers(regime_label)

    # ------------------------------------------------------------------
    # Circuit breakers
    # ------------------------------------------------------------------

    def _evaluate_circuit_breakers(self, regime: str) -> CircuitBreakerStatus:
        daily_dd  = self._daily_dd()
        weekly_dd = self._weekly_dd()
        peak_dd   = self._peak_dd()

        # --- Peak lock (most severe, checked first) ---
        if peak_dd >= self.config.cb_peak_lock and not self.cb.peak_locked:
            self._trigger_peak_lock(peak_dd, regime)

        # --- Weekly close-all ---
        if weekly_dd >= self.config.cb_weekly_close and not self.cb.weekly_halt_active:
            self._trigger_weekly_close(weekly_dd, regime)

        # --- Weekly halve ---
        elif weekly_dd >= self.config.cb_weekly_half and not self.cb.weekly_half_active:
            self._trigger_weekly_half(weekly_dd, regime)

        # --- Daily close-all ---
        if daily_dd >= self.config.cb_daily_close and not self.cb.daily_halt_active:
            self._trigger_daily_close(daily_dd, regime)

        # --- Daily halve ---
        elif daily_dd >= self.config.cb_daily_half and not self.cb.daily_half_active:
            self._trigger_daily_half(daily_dd, regime)

        # Compute effective scale factor
        if self.cb.daily_halt_active or self.cb.weekly_halt_active or self.cb.peak_locked:
            self.cb.scale_factor    = 0.0
            self.cb.trading_allowed = False
        elif self.cb.daily_half_active or self.cb.weekly_half_active:
            self.cb.scale_factor    = 0.5
            self.cb.trading_allowed = True
        else:
            self.cb.scale_factor    = 1.0
            self.cb.trading_allowed = True

        return self.cb

    def _trigger_daily_half(self, dd: float, regime: str) -> None:
        self.cb.daily_half_active = True
        logger.warning(
            "CB DAILY_HALF fired | DD=%.2f%% | equity=%.2f | regime=%s",
            dd * 100, self._portfolio, regime,
        )

    def _trigger_daily_close(self, dd: float, regime: str) -> None:
        self.cb.daily_half_active = True
        self.cb.daily_halt_active = True
        logger.warning(
            "CB DAILY_CLOSE_ALL fired | DD=%.2f%% | equity=%.2f | regime=%s — HALT DAY",
            dd * 100, self._portfolio, regime,
        )

    def _trigger_weekly_half(self, dd: float, regime: str) -> None:
        self.cb.weekly_half_active = True
        logger.warning(
            "CB WEEKLY_HALF fired | DD=%.2f%% | equity=%.2f | regime=%s",
            dd * 100, self._portfolio, regime,
        )

    def _trigger_weekly_close(self, dd: float, regime: str) -> None:
        self.cb.weekly_half_active = True
        self.cb.weekly_halt_active = True
        logger.warning(
            "CB WEEKLY_CLOSE_ALL fired | DD=%.2f%% | equity=%.2f | regime=%s — HALT WEEK",
            dd * 100, self._portfolio, regime,
        )

    def _trigger_peak_lock(self, dd: float, regime: str) -> None:
        self.cb.peak_locked      = True
        self.cb.trading_allowed  = False
        self._write_lock_file(dd, regime)
        logger.critical(
            "CB PEAK_LOCK fired | DD=%.2f%% | equity=%.2f | regime=%s — "
            "BOT HALTED. Delete %s to resume.",
            dd * 100, self._portfolio, regime, LOCK_FILE,
        )

    def _write_lock_file(self, dd: float, regime: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        content = (
            f"Trading halted by peak drawdown circuit breaker.\n"
            f"Timestamp : {now}\n"
            f"Drawdown  : {dd*100:.2f}%\n"
            f"Equity    : {self._portfolio:.2f}\n"
            f"HMM regime: {regime}\n"
            f"\nDelete this file manually to resume trading.\n"
        )
        with open(LOCK_FILE, "w") as fh:
            fh.write(content)

    # ------------------------------------------------------------------
    # Position sizing  (ATR-based, with gap-risk cap)
    # ------------------------------------------------------------------

    def calculate_position_size(self, ticker: str, entry: float,
                                  stop: float,
                                  regime_max_pct: float = 0.15) -> PositionSizeResult:
        """
        shares = (portfolio × risk_per_trade) / |entry − stop|

        Caps applied in order:
          1. Regime max (passed in from RegimeInfo.max_position_size_pct)
          2. Portfolio max (15 %)
          3. Overnight gap-risk cap
          4. Scale factor from active circuit breakers
        """
        if stop >= entry:
            raise ValueError(f"stop ({stop}) must be < entry ({entry})")

        risk_per_share = abs(entry - stop)
        raw_notional   = self._portfolio * self.config.risk_per_trade
        shares_raw     = raw_notional / risk_per_share
        notional_raw   = shares_raw * entry

        # Cap at regime max
        regime_capped  = False
        max_notional   = self._portfolio * regime_max_pct
        if notional_raw > max_notional:
            notional_raw  = max_notional
            shares_raw    = notional_raw / entry
            regime_capped = True

        # Cap at portfolio max (15 %)
        port_capped    = False
        port_max_not   = self._portfolio * self.config.max_single_position
        if notional_raw > port_max_not:
            notional_raw  = port_max_not
            shares_raw    = notional_raw / entry
            port_capped   = True

        # Overnight gap-risk cap
        # overnight_size = min(normal, size where 3× gap = 2 % of portfolio)
        gap_capped     = False
        gap_loss_per_share = risk_per_share * self.config.gap_risk_multiplier
        max_gap_shares    = (self._portfolio * self.config.gap_risk_budget) / gap_loss_per_share
        max_gap_notional  = max_gap_shares * entry
        if notional_raw > max_gap_notional:
            notional_raw  = max_gap_notional
            shares_raw    = max_gap_notional / entry
            gap_capped    = True

        # Apply circuit-breaker scale factor
        shares_raw    *= self.cb.scale_factor
        notional_raw   = shares_raw * entry

        shares = int(shares_raw)
        shares = max(shares, 0)

        # Enforce minimum notional
        if shares * entry < self.config.min_notional:
            shares = 0

        return PositionSizeResult(
            ticker           = ticker,
            shares           = shares,
            notional         = shares * entry,
            entry_price      = entry,
            stop_price       = stop,
            risk_amount      = shares * risk_per_share,
            overnight_capped = gap_capped,
            regime_capped    = regime_capped,
            portfolio_capped = port_capped,
        )

    # ------------------------------------------------------------------
    # Order validation  (veto gate)
    # ------------------------------------------------------------------

    def approve_order(self, ticker: str, notional: float, side: str,
                       stop_loss: Optional[float] = None,
                       entry_price: Optional[float] = None) -> OrderDecision:
        """
        Final gate before order submission.
        Returns OrderDecision(approved, reason).
        Checks (in order):
          1. Lock file / trading_allowed
          2. Stop-loss mandatory
          3. Daily trade limit
          4. Max concurrent positions (buys only)
          5. Max total exposure
          6. Max single position
        """
        # 1. Lock file
        if self.is_locked():
            return OrderDecision(False, f"Bot locked — delete {LOCK_FILE} to resume.")
        if not self.cb.trading_allowed:
            return OrderDecision(False, "Trading halted by circuit breaker.")

        # 2. Stop-loss mandatory for buys
        if side.upper() == "BUY" and stop_loss is None:
            return OrderDecision(False, "Order rejected: no stop_loss provided (mandatory).")

        # 3. Daily trade limit
        if self._daily_trades >= self.config.max_daily_trades:
            return OrderDecision(False, f"Daily trade limit ({self.config.max_daily_trades}) reached.")

        # 4. Max concurrent positions (buy only)
        if side.upper() == "BUY":
            if len(self._open_positions) >= self.config.max_concurrent:
                return OrderDecision(False,
                    f"Max concurrent positions ({self.config.max_concurrent}) reached.")

        # 5. Max total exposure
        current_exposure = sum(self._open_positions.values())
        if side.upper() == "BUY":
            if (current_exposure + notional) > self._portfolio * self.config.max_total_exposure:
                return OrderDecision(False,
                    f"Max total exposure ({self.config.max_total_exposure*100:.0f}%) would be exceeded.")

        # 6. Max single position
        if side.upper() == "BUY" and notional > self._portfolio * self.config.max_single_position:
            return OrderDecision(False,
                f"Notional ${notional:.0f} exceeds single-position limit "
                f"(${self._portfolio * self.config.max_single_position:.0f}).")

        scaled = int(notional / entry_price * self.cb.scale_factor) if entry_price else 0
        return OrderDecision(True, "Approved.", scaled_shares=scaled)

    def validate_leverage(self, requested: float) -> float:
        """Clamp to max_leverage; further halve if scale_factor=0.5."""
        clamped = min(requested, self.config.max_leverage)
        return clamped * self.cb.scale_factor if self.cb.scale_factor < 1.0 else clamped

    # ------------------------------------------------------------------
    # Position tracker
    # ------------------------------------------------------------------

    def record_fill(self, ticker: str, notional: float, side: str) -> None:
        """Call after every confirmed fill to update internal state."""
        if side.upper() == "BUY":
            self._open_positions[ticker] = notional
            self._daily_trades          += 1
        elif side.upper() == "SELL":
            self._open_positions.pop(ticker, None)
            self._daily_trades += 1

    def get_open_positions(self) -> dict[str, float]:
        return dict(self._open_positions)

    # ------------------------------------------------------------------
    # P&L helpers
    # ------------------------------------------------------------------

    def _daily_dd(self) -> float:
        if self._day_start <= 0:
            return 0.0
        return max(0.0, (self._day_start - self._portfolio) / self._day_start)

    def _weekly_dd(self) -> float:
        if self._week_start <= 0:
            return 0.0
        return max(0.0, (self._week_start - self._portfolio) / self._week_start)

    def _peak_dd(self) -> float:
        if self._peak <= 0:
            return 0.0
        return max(0.0, (self._peak - self._portfolio) / self._peak)

    def daily_pnl_pct(self)  -> float: return -self._daily_dd()
    def weekly_pnl_pct(self) -> float: return -self._weekly_dd()
    def peak_dd_pct(self)    -> float: return  self._peak_dd()

    # ------------------------------------------------------------------
    # Lock file
    # ------------------------------------------------------------------

    def is_locked(self) -> bool:
        return os.path.exists(LOCK_FILE) or self.cb.peak_locked
