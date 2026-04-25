"""
Unit tests for regime strategies and StrategyOrchestrator.

Covers:
  - LowVol: 95% allocation + 1.25x leverage
  - HighVol: 60% allocation + 1.0x leverage
  - MidVol: 95% when price > 50 EMA, 60% when below
  - Uncertainty mode halves position size + forces 1.0x leverage
  - Rebalance threshold prevents unnecessary trades
  - Vol rank mapping works for 3-7 regimes
  - All LABEL_TO_STRATEGY keys map to a valid strategy
  - Backward-compatible aliases resolve correctly
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from models.hmm_engine import RegimeInfo, RegimeState
from models.regime_strategies import (
    LowVolBullStrategy,
    MidVolCautiousStrategy,
    HighVolDefensiveStrategy,
    StrategyOrchestrator,
    LABEL_TO_STRATEGY,
    BullTrendStrategy,
    CrashDefensiveStrategy,
    MeanReversionStrategy,
    MIN_CONFIDENCE,
    REBALANCE_THRESHOLD,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_bars(n: int = 100, trend: str = "up") -> pd.DataFrame:
    """Synthetic OHLCV bars with configurable trend direction."""
    rng   = np.random.default_rng(0)
    drift = 0.001 if trend == "up" else -0.001
    close = 400.0 * np.exp(np.cumsum(rng.normal(drift, 0.01, n)))
    high  = close * rng.uniform(1.000, 1.008, n)
    low   = close * rng.uniform(0.992, 1.000, n)
    open_ = close * rng.uniform(0.998, 1.002, n)
    vol   = rng.integers(1_000_000, 5_000_000, n).astype(float)
    return pd.DataFrame({"open": open_, "high": high, "low": low,
                          "close": close, "volume": vol})


def _make_regime(label: str = "bull", state_id: int = 3,
                  prob: float = 0.80, confirmed: bool = True) -> RegimeState:
    probs = np.zeros(5)
    probs[state_id] = prob
    probs[(state_id + 1) % 5] = 1.0 - prob
    return RegimeState(
        label=label, state_id=state_id, probability=prob,
        state_probabilities=probs, timestamp=__import__("datetime").datetime.now(__import__("datetime").timezone.utc),
        is_confirmed=confirmed, consecutive_bars=5,
    )


def _make_regime_infos(labels: list[str],
                        vols:   list[float]) -> list[RegimeInfo]:
    return [
        RegimeInfo(
            regime_id=i, regime_name=lbl, expected_return=0.1,
            expected_volatility=v, recommended_strategy="test",
            max_leverage_allowed=1.25, max_position_size_pct=0.95,
            min_confidence_to_act=0.55,
        )
        for i, (lbl, v) in enumerate(zip(labels, vols))
    ]


# ---------------------------------------------------------------------------
# Strategy allocation tests
# ---------------------------------------------------------------------------

class TestLowVolBullStrategy:

    def test_allocation_is_95_pct(self):
        bars  = _make_bars(100, "up")
        s     = LowVolBullStrategy()
        sig   = s.generate_signal("SPY", bars, _make_regime("bull"))
        assert sig is not None
        assert sig.position_size_pct == pytest.approx(0.95)

    def test_leverage_is_1_25(self):
        sig = LowVolBullStrategy().generate_signal("SPY", _make_bars(), _make_regime())
        assert sig.leverage == pytest.approx(1.25)

    def test_direction_is_long(self):
        sig = LowVolBullStrategy().generate_signal("SPY", _make_bars(), _make_regime())
        assert sig.direction == "LONG"

    def test_stop_below_price(self):
        sig = LowVolBullStrategy().generate_signal("SPY", _make_bars(), _make_regime())
        assert sig.stop_loss < sig.entry_price

    def test_insufficient_bars_returns_none(self):
        sig = LowVolBullStrategy().generate_signal("SPY", _make_bars(10), _make_regime())
        assert sig is None


class TestHighVolDefensiveStrategy:

    def test_allocation_is_60_pct(self):
        sig = HighVolDefensiveStrategy().generate_signal("SPY", _make_bars(), _make_regime("crash"))
        assert sig.position_size_pct == pytest.approx(0.60)

    def test_leverage_is_1_0(self):
        sig = HighVolDefensiveStrategy().generate_signal("SPY", _make_bars(), _make_regime("crash"))
        assert sig.leverage == pytest.approx(1.0)

    def test_direction_is_long_not_short(self):
        sig = HighVolDefensiveStrategy().generate_signal("SPY", _make_bars(), _make_regime("crash"))
        assert sig.direction == "LONG"


class TestMidVolCautiousStrategy:

    def test_above_ema_gives_95_pct(self):
        # Strongly uptrending bars → price will be above 50 EMA
        bars = _make_bars(100, "up")
        sig  = MidVolCautiousStrategy().generate_signal("SPY", bars, _make_regime("neutral"))
        assert sig is not None
        assert sig.position_size_pct == pytest.approx(0.95)

    def test_below_ema_gives_60_pct(self):
        # Strongly downtrending bars → price will be below 50 EMA
        bars = _make_bars(100, "down")
        sig  = MidVolCautiousStrategy().generate_signal("SPY", bars, _make_regime("neutral"))
        assert sig is not None
        assert sig.position_size_pct == pytest.approx(0.60)

    def test_leverage_is_always_1_0(self):
        for trend in ("up", "down"):
            sig = MidVolCautiousStrategy().generate_signal("SPY", _make_bars(100, trend),
                                                            _make_regime())
            assert sig.leverage == pytest.approx(1.0)


# ---------------------------------------------------------------------------
# Uncertainty mode
# ---------------------------------------------------------------------------

class TestUncertaintyMode:

    def _orchestrator(self) -> StrategyOrchestrator:
        infos = _make_regime_infos(
            ["crash", "bear", "neutral", "bull", "euphoria"],
            [0.50,    0.25,   0.15,     0.12,  0.20],
        )
        return StrategyOrchestrator(infos)

    def test_low_confidence_halves_size(self):
        orch   = self._orchestrator()
        regime = _make_regime("bull", state_id=3, prob=0.40)  # below MIN_CONFIDENCE
        bars   = {"SPY": _make_bars(100, "up")}
        sigs   = orch.generate_signals(["SPY"], bars, regime, is_flickering=False)
        assert len(sigs) == 1
        assert sigs[0].position_size_pct <= 0.95 * 0.5 + 1e-6

    def test_flickering_halves_size(self):
        orch   = self._orchestrator()
        regime = _make_regime("bull", state_id=3, prob=0.80)  # high confidence
        bars   = {"SPY": _make_bars(100, "up")}
        sigs   = orch.generate_signals(["SPY"], bars, regime, is_flickering=True)
        assert len(sigs) == 1
        assert "[UNCERTAINTY" in sigs[0].reasoning

    def test_uncertainty_forces_leverage_1_0(self):
        orch   = self._orchestrator()
        regime = _make_regime("bull", state_id=3, prob=0.40)
        bars   = {"SPY": _make_bars(100, "up")}
        sigs   = orch.generate_signals(["SPY"], bars, regime)
        assert sigs[0].leverage == pytest.approx(1.0)


# ---------------------------------------------------------------------------
# Rebalance threshold
# ---------------------------------------------------------------------------

class TestRebalanceThreshold:

    def test_small_drift_no_rebalance(self):
        orch = StrategyOrchestrator(_make_regime_infos(["bull"], [0.12]))
        assert not orch.needs_rebalance(0.90, 0.95)   # 5 % drift < 10 %

    def test_large_drift_triggers_rebalance(self):
        orch = StrategyOrchestrator(_make_regime_infos(["bull"], [0.12]))
        assert orch.needs_rebalance(0.95, 0.60)        # 35 % drift > 10 %

    def test_exact_threshold_no_rebalance(self):
        orch = StrategyOrchestrator(_make_regime_infos(["bull"], [0.12]))
        assert not orch.needs_rebalance(0.90, 1.00 - 1e-9)   # just under


# ---------------------------------------------------------------------------
# Volatility rank mapping
# ---------------------------------------------------------------------------

class TestVolRankMapping:

    def _orch(self, n: int) -> StrategyOrchestrator:
        labels = ["crash", "bear", "neutral", "bull", "euphoria",
                  "strong_bear", "weak_bear"][:n]
        vols   = np.linspace(0.50, 0.10, n).tolist()  # ascending vol order reversed
        return StrategyOrchestrator(_make_regime_infos(labels, sorted(vols)))

    def test_lowest_vol_regime_is_lowvol_strategy(self):
        orch = self._orch(5)
        # regime_id 0 = lowest expected_vol after sort → LowVolBullStrategy
        strat = orch._id_to_strategy.get(0)
        assert isinstance(strat, LowVolBullStrategy)

    def test_highest_vol_regime_is_highvol_strategy(self):
        orch = self._orch(5)
        strat = orch._id_to_strategy.get(4)
        assert isinstance(strat, HighVolDefensiveStrategy)

    @pytest.mark.parametrize("n", [3, 4, 5, 6, 7])
    def test_mapping_covers_all_regimes(self, n: int):
        orch = self._orch(n)
        assert len(orch._id_to_strategy) == n


# ---------------------------------------------------------------------------
# Label coverage and aliases
# ---------------------------------------------------------------------------

class TestLabelCoverage:

    def test_all_known_labels_have_strategy(self):
        known = ["crash", "strong_bear", "bear", "weak_bear",
                  "neutral", "weak_bull", "bull", "strong_bull", "euphoria"]
        for lbl in known:
            assert lbl in LABEL_TO_STRATEGY, f"{lbl!r} missing from LABEL_TO_STRATEGY"

    def test_aliases_resolve_correctly(self):
        assert CrashDefensiveStrategy is HighVolDefensiveStrategy
        assert BullTrendStrategy       is LowVolBullStrategy
        assert MeanReversionStrategy   is MidVolCautiousStrategy
