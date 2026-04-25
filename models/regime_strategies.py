"""
Volatility-based allocation strategies.

DESIGN INSIGHT
--------------
The HMM detects VOLATILITY ENVIRONMENTS, not direction.
Stocks trend up ~70 % of the time in low-vol periods.
Worst drawdowns cluster in high-vol spikes.
Strategy is therefore simple:
  Low vol  → fully invested (calm markets compound)
  Mid vol  → stay invested if trend intact, reduce if not
  High vol → reduce but stay partially invested (catch V-shaped rebounds)

The edge comes from AVOIDING BIG DRAWDOWNS through vol-based sizing.

THREE STRATEGY CLASSES (keyed by volatility rank, NOT by label):
  LowVolBullStrategy      – bottom third by expected_volatility
  MidVolCautiousStrategy  – middle third
  HighVolDefensiveStrategy– top third

VOLATILITY RANK MAPPING (works for any n_regimes 3-7):
  position = rank / (n_regimes - 1)   # 0.0 = calmest, 1.0 = most volatile
  position <= 0.33  →  LowVolBullStrategy
  position >= 0.67  →  HighVolDefensiveStrategy
  else              →  MidVolCautiousStrategy

The orchestrator sorts by expected_volatility — INDEPENDENT of the
mean-return label sort. "BULL" does NOT mean low vol.
"""

from __future__ import annotations

import abc
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

import numpy as np
import pandas as pd

from models.hmm_engine import RegimeInfo, RegimeState

logger = logging.getLogger(__name__)

MIN_CONFIDENCE: float = 0.55   # below this → uncertainty mode
REBALANCE_THRESHOLD: float = 0.10   # min allocation drift to trigger rebalance


# ---------------------------------------------------------------------------
# Signal dataclass
# ---------------------------------------------------------------------------

@dataclass
class Signal:
    symbol:            str
    direction:         str              # "LONG" | "FLAT"
    confidence:        float
    entry_price:       float
    stop_loss:         float
    take_profit:       Optional[float]
    position_size_pct: float            # 0.60 – 0.95 (or halved in uncertainty)
    leverage:          float            # 1.0 or 1.25
    regime_id:         int
    regime_name:       str
    regime_probability: float
    timestamp:         datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    reasoning:         str = ""
    strategy_name:     str = ""
    metadata:          dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Private bar helpers
# ---------------------------------------------------------------------------

def _ema(series: pd.Series, span: int) -> float:
    """Last value of an EMA."""
    return float(series.ewm(span=span, adjust=False).mean().iloc[-1])


def _atr(bars: pd.DataFrame, period: int = 14) -> float:
    """ATR(period) from an OHLCV DataFrame."""
    h, l, c = bars["high"], bars["low"], bars["close"]
    prev_c  = c.shift(1)
    tr      = pd.concat([h - l, (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    return float(tr.rolling(period, min_periods=period // 2).mean().iloc[-1])


# ---------------------------------------------------------------------------
# Base strategy
# ---------------------------------------------------------------------------

class BaseStrategy(abc.ABC):
    """Abstract base for all vol-regime strategies."""

    @abc.abstractmethod
    def generate_signal(self, symbol: str, bars: pd.DataFrame,
                         regime: RegimeState) -> Optional[Signal]:
        """
        Generate a Signal for `symbol` given recent OHLCV `bars` and
        the current RegimeState.  Return None if no signal.
        """


# ---------------------------------------------------------------------------
# Strategy 1 — Low volatility (bottom third)
# ---------------------------------------------------------------------------

class LowVolBullStrategy(BaseStrategy):
    """
    Calm markets trend upward. Be fully invested with modest leverage.
    Stop: max(close - 3*ATR, 50EMA - 0.5*ATR).
    """

    def generate_signal(self, symbol: str, bars: pd.DataFrame,
                         regime: RegimeState) -> Optional[Signal]:
        if len(bars) < 50:
            return None

        price   = float(bars["close"].iloc[-1])
        ema50   = _ema(bars["close"], 50)
        atr_val = _atr(bars)

        stop = max(price - 3.0 * atr_val, ema50 - 0.5 * atr_val)
        stop = min(stop, price - atr_val)   # must always be below current price

        return Signal(
            symbol            = symbol,
            direction         = "LONG",
            confidence        = regime.probability,
            entry_price       = price,
            stop_loss         = stop,
            take_profit       = None,
            position_size_pct = 0.95,
            leverage          = 1.25,
            regime_id         = regime.state_id,
            regime_name       = regime.label,
            regime_probability= regime.probability,
            reasoning         = f"Low-vol bull: price={price:.2f} ema50={ema50:.2f} atr={atr_val:.2f}",
            strategy_name     = "LowVolBullStrategy",
        )


# ---------------------------------------------------------------------------
# Strategy 2 — Mid volatility (middle third)
# ---------------------------------------------------------------------------

class MidVolCautiousStrategy(BaseStrategy):
    """
    Stay invested if trend intact (price > 50 EMA), reduce if not.
    Stop: 50EMA - 0.5*ATR.
    """

    def generate_signal(self, symbol: str, bars: pd.DataFrame,
                         regime: RegimeState) -> Optional[Signal]:
        if len(bars) < 50:
            return None

        price   = float(bars["close"].iloc[-1])
        ema50   = _ema(bars["close"], 50)
        atr_val = _atr(bars)
        stop    = ema50 - 0.5 * atr_val

        trend_intact    = price > ema50
        allocation      = 0.95 if trend_intact else 0.60
        trend_label     = "trend intact → stay invested" if trend_intact else "trend broken → reduce"

        return Signal(
            symbol            = symbol,
            direction         = "LONG",
            confidence        = regime.probability,
            entry_price       = price,
            stop_loss         = stop,
            take_profit       = None,
            position_size_pct = allocation,
            leverage          = 1.0,
            regime_id         = regime.state_id,
            regime_name       = regime.label,
            regime_probability= regime.probability,
            reasoning         = f"Mid-vol cautious: {trend_label} price={price:.2f} ema50={ema50:.2f}",
            strategy_name     = "MidVolCautiousStrategy",
        )


# ---------------------------------------------------------------------------
# Strategy 3 — High volatility (top third)
# ---------------------------------------------------------------------------

class HighVolDefensiveStrategy(BaseStrategy):
    """
    Reduce exposure but stay partially invested to catch V-shaped rebounds.
    Direction is LONG (never short). Stop: 50EMA - 1.0*ATR.
    """

    def generate_signal(self, symbol: str, bars: pd.DataFrame,
                         regime: RegimeState) -> Optional[Signal]:
        if len(bars) < 50:
            return None

        price   = float(bars["close"].iloc[-1])
        ema50   = _ema(bars["close"], 50)
        atr_val = _atr(bars)
        stop    = ema50 - 1.0 * atr_val   # wider stop for volatile conditions

        return Signal(
            symbol            = symbol,
            direction         = "LONG",
            confidence        = regime.probability,
            entry_price       = price,
            stop_loss         = stop,
            take_profit       = None,
            position_size_pct = 0.60,
            leverage          = 1.0,
            regime_id         = regime.state_id,
            regime_name       = regime.label,
            regime_probability= regime.probability,
            reasoning         = f"High-vol defensive: 60 % invested, wider stop. price={price:.2f} ema50={ema50:.2f}",
            strategy_name     = "HighVolDefensiveStrategy",
        )


# ---------------------------------------------------------------------------
# Backward-compatible aliases (label-named → vol-class)
# ---------------------------------------------------------------------------

CrashDefensiveStrategy    = HighVolDefensiveStrategy
BearTrendStrategy         = HighVolDefensiveStrategy
MeanReversionStrategy     = MidVolCautiousStrategy
BullTrendStrategy         = LowVolBullStrategy
EuphoriaCautiousStrategy  = LowVolBullStrategy

LABEL_TO_STRATEGY: dict[str, type[BaseStrategy]] = {
    "crash":       HighVolDefensiveStrategy,
    "strong_bear": HighVolDefensiveStrategy,
    "bear":        HighVolDefensiveStrategy,
    "weak_bear":   MidVolCautiousStrategy,
    "neutral":     MidVolCautiousStrategy,
    "weak_bull":   MidVolCautiousStrategy,
    "bull":        LowVolBullStrategy,
    "strong_bull": LowVolBullStrategy,
    "euphoria":    LowVolBullStrategy,
}


# ---------------------------------------------------------------------------
# Strategy Orchestrator
# ---------------------------------------------------------------------------

def _vol_rank_to_strategy(position: float) -> type[BaseStrategy]:
    """Map normalised vol position [0,1] to strategy class."""
    if position <= 0.33:
        return LowVolBullStrategy
    if position >= 0.67:
        return HighVolDefensiveStrategy
    return MidVolCautiousStrategy


class StrategyOrchestrator:
    """
    Selects the right strategy class based on volatility rank (NOT label).

    Vol rank is computed by sorting the HMM's RegimeInfo objects by
    expected_volatility (ascending).  This is INDEPENDENT of the
    mean-return label sort used by HMMEngine.

    After HMM retrain call update_regime_infos() to rebuild the mapping.
    """

    def __init__(self, regime_infos: list[RegimeInfo],
                 min_confidence: float = MIN_CONFIDENCE,
                 rebalance_threshold: float = REBALANCE_THRESHOLD) -> None:
        self._min_confidence      = min_confidence
        self._rebalance_threshold = rebalance_threshold
        self._id_to_strategy: dict[int, BaseStrategy] = {}
        self.update_regime_infos(regime_infos)

    # ------------------------------------------------------------------
    # Mapping rebuild
    # ------------------------------------------------------------------

    def update_regime_infos(self, regime_infos: list[RegimeInfo]) -> None:
        """Sort by expected_volatility and map regime_id → strategy instance."""
        if not regime_infos:
            return
        n = len(regime_infos)
        sorted_by_vol = sorted(regime_infos, key=lambda ri: ri.expected_volatility)
        self._id_to_strategy = {}
        for rank, info in enumerate(sorted_by_vol):
            position = rank / max(n - 1, 1)
            cls      = _vol_rank_to_strategy(position)
            self._id_to_strategy[info.regime_id] = cls()
            logger.debug("regime_id=%d (%s) vol=%.3f position=%.2f → %s",
                         info.regime_id, info.regime_name,
                         info.expected_volatility, position, cls.__name__)

    # ------------------------------------------------------------------
    # Signal generation
    # ------------------------------------------------------------------

    def generate_signals(self, symbols: list[str],
                          bars: dict[str, pd.DataFrame],
                          regime_state: RegimeState,
                          is_flickering: bool = False) -> list[Signal]:
        """
        Generate a Signal for each symbol.
        Applies uncertainty mode (halve size, force 1.0x leverage) when
        confidence < threshold or regime is flickering.
        """
        uncertainty = (
            regime_state.probability < self._min_confidence
            or is_flickering
            or not regime_state.is_confirmed
        )

        strategy = self._id_to_strategy.get(regime_state.state_id)
        if strategy is None:
            logger.warning("No strategy mapped for regime_id=%d", regime_state.state_id)
            return []

        signals: list[Signal] = []
        for sym in symbols:
            sym_bars = bars.get(sym)
            if sym_bars is None or len(sym_bars) < 50:
                continue

            sig = strategy.generate_signal(sym, sym_bars, regime_state)
            if sig is None:
                continue

            if uncertainty:
                sig.position_size_pct = sig.position_size_pct * 0.5
                sig.leverage          = 1.0
                sig.reasoning        += " [UNCERTAINTY — size halved]"

            signals.append(sig)

        return signals

    # ------------------------------------------------------------------
    # Rebalance check
    # ------------------------------------------------------------------

    def needs_rebalance(self, current_allocation: float,
                         target_allocation: float) -> bool:
        """True when allocation drift > rebalance_threshold (default 10 %)."""
        return abs(target_allocation - current_allocation) > self._rebalance_threshold

    # ------------------------------------------------------------------
    # Simple single-symbol helper (used by backtester)
    # ------------------------------------------------------------------

    def get_target_allocation(self, bars: pd.DataFrame,
                               regime_state: RegimeState,
                               is_flickering: bool = False) -> tuple[float, float, str]:
        """
        Return (target_allocation, leverage, strategy_name) for a single symbol.
        Convenience wrapper used by the walk-forward backtester.
        """
        uncertainty = (
            regime_state.probability < self._min_confidence
            or is_flickering
            or not regime_state.is_confirmed
        )

        strategy = self._id_to_strategy.get(regime_state.state_id)
        if strategy is None or len(bars) < 50:
            return 0.0, 1.0, "none"

        sig = strategy.generate_signal("__backtest__", bars, regime_state)
        if sig is None:
            return 0.0, 1.0, "none"

        alloc     = sig.position_size_pct
        leverage  = sig.leverage
        if uncertainty:
            alloc    *= 0.5
            leverage  = 1.0

        return alloc * leverage, leverage, sig.strategy_name
