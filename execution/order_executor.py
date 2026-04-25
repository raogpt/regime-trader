"""
Order executor.

Translates approved Signals into actual broker orders, tracks open positions,
and manages stop-loss evaluation.  Every BUY goes through RiskManager.approve_order()
before submission.  Circuit-breaker close-all is routed here via close_all_positions().
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

from models.regime_strategies import Signal
from risk.risk_manager import RiskManager, PositionSizeResult
from execution.alpaca_broker import AlpacaBroker

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class OrderResult:
    order_id:     str
    ticker:       str
    side:         str         # "buy" | "sell"
    qty:          int
    filled_price: float
    status:       str         # "filled" | "partial" | "rejected" | "pending"
    timestamp:    datetime = field(
        default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class OpenPosition:
    ticker:           str
    qty:              int
    entry_price:      float
    current_price:    float
    stop_price:       float
    pnl:              float
    pnl_pct:          float
    regime_at_entry:  str
    opened_at:        datetime


# ---------------------------------------------------------------------------
# OrderExecutor
# ---------------------------------------------------------------------------

class OrderExecutor:
    """
    High-level interface for placing, modifying, and closing positions.
    Coordinates AlpacaBroker and RiskManager.
    """

    def __init__(self, broker: AlpacaBroker, risk_manager: RiskManager) -> None:
        self._broker   = broker
        self._risk     = risk_manager
        self._open_positions: dict[str, OpenPosition] = {}
        self._trade_history:  list[OrderResult]       = []

    # ------------------------------------------------------------------
    # Rebalancing
    # ------------------------------------------------------------------

    def rebalance(self, signal: Signal, account_value: float) -> list[OrderResult]:
        """
        Compute the target notional from `signal`, compare to current position,
        and submit the minimum set of orders to reach the target.
        Returns a list of OrderResult objects (may be empty if no action needed).
        """
        results: list[OrderResult] = []

        target_notional  = self._compute_target_notional(signal, account_value)
        current_notional = self._get_current_notional(signal.symbol)
        delta            = target_notional - current_notional

        # Threshold: skip if change < 5% of account (reduces churn)
        if abs(delta) < account_value * 0.05:
            logger.debug("Rebalance skipped | %s delta=%.0f < threshold", signal.symbol, delta)
            return results

        if delta > 0:
            # Need to BUY
            size = self._risk.calculate_position_size(
                ticker         = signal.symbol,
                entry          = signal.entry_price,
                stop           = signal.stop_loss,
                regime_max_pct = signal.position_size_pct,
            )
            if size.shares > 0:
                result = self.buy(signal.symbol, size, signal.regime_name)
                if result:
                    results.append(result)
        else:
            # Need to SELL / reduce
            current_qty = self._open_positions.get(signal.symbol)
            if current_qty:
                sell_qty = min(
                    current_qty.qty,
                    int(abs(delta) / signal.entry_price),
                )
                if sell_qty > 0:
                    result = self.sell(signal.symbol, sell_qty,
                                       reason=f"rebalance signal={signal.regime_name}")
                    if result:
                        results.append(result)

        return results

    def _compute_target_notional(self, signal: Signal, account_value: float) -> float:
        return account_value * signal.position_size_pct * signal.leverage

    def _get_current_notional(self, ticker: str) -> float:
        pos = self._open_positions.get(ticker)
        if pos is None:
            return 0.0
        return pos.qty * pos.current_price

    # ------------------------------------------------------------------
    # Order placement
    # ------------------------------------------------------------------

    def buy(self, ticker: str, size: PositionSizeResult,
             regime_label: str) -> Optional[OrderResult]:
        """Submit a validated BUY market order."""
        # Risk gate
        decision = self._risk.approve_order(
            ticker      = ticker,
            notional    = size.notional,
            side        = "BUY",
            stop_loss   = size.stop_price,
            entry_price = size.entry_price,
        )
        if not decision.approved:
            logger.warning("BUY rejected | %s | %s", ticker, decision.reason)
            return OrderResult(
                order_id     = "",
                ticker       = ticker,
                side         = "buy",
                qty          = 0,
                filled_price = 0.0,
                status       = "rejected",
            )

        try:
            raw = self._broker.submit_market_order(ticker, size.shares, "buy")
        except Exception as exc:
            logger.error("BUY submit failed | %s | %s", ticker, exc)
            return None

        result = OrderResult(
            order_id     = raw["id"],
            ticker       = ticker,
            side         = "buy",
            qty          = raw.get("filled_qty", size.shares),
            filled_price = raw.get("filled_avg_price", size.entry_price),
            status       = raw.get("status", "pending"),
        )

        # Record fill in risk manager and local state
        self._risk.record_fill(ticker, size.notional, "BUY")
        self._open_positions[ticker] = OpenPosition(
            ticker          = ticker,
            qty             = result.qty,
            entry_price     = result.filled_price,
            current_price   = result.filled_price,
            stop_price      = size.stop_price,
            pnl             = 0.0,
            pnl_pct         = 0.0,
            regime_at_entry = regime_label,
            opened_at       = datetime.now(timezone.utc),
        )
        self._trade_history.append(result)
        logger.info("BUY filled | %s qty=%d @ %.2f | stop=%.2f",
                    ticker, result.qty, result.filled_price, size.stop_price)
        return result

    def sell(self, ticker: str, qty: int, reason: str = "") -> Optional[OrderResult]:
        """Submit a SELL market order (partial or full)."""
        pos = self._open_positions.get(ticker)
        if pos is None:
            logger.warning("SELL ignored — no open position for %s", ticker)
            return None

        try:
            raw = self._broker.submit_market_order(ticker, qty, "sell")
        except Exception as exc:
            logger.error("SELL submit failed | %s | %s", ticker, exc)
            return None

        result = OrderResult(
            order_id     = raw["id"],
            ticker       = ticker,
            side         = "sell",
            qty          = raw.get("filled_qty", qty),
            filled_price = raw.get("filled_avg_price", pos.current_price),
            status       = raw.get("status", "pending"),
        )

        pnl = (result.filled_price - pos.entry_price) * result.qty
        logger.info("SELL filled | %s qty=%d @ %.2f | pnl=%.2f | reason=%s",
                    ticker, result.qty, result.filled_price, pnl, reason)

        self._risk.record_fill(ticker, result.qty * result.filled_price, "SELL")

        if result.qty >= pos.qty:
            del self._open_positions[ticker]
        else:
            pos.qty -= result.qty

        self._trade_history.append(result)
        return result

    def close_position(self, ticker: str, reason: str = "") -> Optional[OrderResult]:
        """Fully close a position if one is open."""
        pos = self._open_positions.get(ticker)
        if pos is None:
            return None
        return self.sell(ticker, pos.qty, reason=reason or "close_position")

    def close_all_positions(self, reason: str = "") -> list[OrderResult]:
        """Close every tracked open position (e.g. circuit-breaker triggered)."""
        results = []
        for ticker in list(self._open_positions):
            r = self.close_position(ticker, reason=reason or "close_all")
            if r:
                results.append(r)
        return results

    # ------------------------------------------------------------------
    # Stop management
    # ------------------------------------------------------------------

    def update_stop(self, ticker: str, new_stop: float) -> bool:
        """Modify the stop price for an existing position (local state only)."""
        pos = self._open_positions.get(ticker)
        if pos is None:
            return False
        pos.stop_price = new_stop
        logger.debug("Stop updated | %s new_stop=%.2f", ticker, new_stop)
        return True

    def check_stops(self, current_prices: dict[str, float]) -> list[OrderResult]:
        """
        Evaluate all open stops against current_prices.
        Close any position where price ≤ stop_price.
        Returns list of OrderResults for positions that were closed.
        """
        closed = []
        for ticker, pos in list(self._open_positions.items()):
            price = current_prices.get(ticker)
            if price is None:
                continue
            pos.current_price = price
            pos.pnl     = (price - pos.entry_price) * pos.qty
            pos.pnl_pct = (price - pos.entry_price) / pos.entry_price

            if price <= pos.stop_price:
                logger.warning("Stop hit | %s price=%.2f stop=%.2f pnl=%.2f",
                               ticker, price, pos.stop_price, pos.pnl)
                r = self.close_position(ticker, reason="stop_hit")
                if r:
                    closed.append(r)
        return closed

    # ------------------------------------------------------------------
    # Position sync (reconcile with broker)
    # ------------------------------------------------------------------

    def sync_positions(self) -> None:
        """
        Refresh local open_positions from the broker.
        Used at startup and after any unexpected state.
        """
        broker_positions = self._broker.get_open_positions()
        broker_map = {p["symbol"]: p for p in broker_positions}

        # Remove locally-tracked positions that are no longer open on broker
        for ticker in list(self._open_positions):
            if ticker not in broker_map:
                logger.info("Sync: removing stale local position %s", ticker)
                del self._open_positions[ticker]

        # Add broker positions not tracked locally
        for symbol, p in broker_map.items():
            if symbol not in self._open_positions:
                price = p["current_price"]
                entry = p["avg_entry"]
                qty   = p["qty"]
                self._open_positions[symbol] = OpenPosition(
                    ticker          = symbol,
                    qty             = qty,
                    entry_price     = entry,
                    current_price   = price,
                    stop_price      = entry * 0.97,   # default 3% stop if unknown
                    pnl             = p["unrealized_pl"],
                    pnl_pct         = (price - entry) / entry if entry else 0.0,
                    regime_at_entry = "unknown",
                    opened_at       = datetime.now(timezone.utc),
                )
            else:
                # Update mark-to-market
                pos               = self._open_positions[symbol]
                pos.current_price = p["current_price"]
                pos.pnl           = p["unrealized_pl"]
                pos.pnl_pct       = (pos.current_price - pos.entry_price) / pos.entry_price

        logger.info("Positions synced | open=%d", len(self._open_positions))

    # ------------------------------------------------------------------
    # Read-only accessors
    # ------------------------------------------------------------------

    def get_open_positions(self) -> dict[str, OpenPosition]:
        return dict(self._open_positions)

    def get_position(self, ticker: str) -> Optional[OpenPosition]:
        return self._open_positions.get(ticker)

    def get_trade_history(self) -> list[OrderResult]:
        return list(self._trade_history)
