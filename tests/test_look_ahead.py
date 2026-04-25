"""
MANDATORY look-ahead bias test.

Verifies that predict_regime_filtered(data[0:T])[-1]
== predict_regime_filtered(data[0:T+100])[T-1].

If they differ, the forward algorithm is using future data.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from data.feature_engineering import FeatureEngineer
from models.hmm_engine import HMMEngine, HMMEngineConfig, RegimeState


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_synthetic_ohlcv(n: int = 700, seed: int = 42) -> pd.DataFrame:
    """Generate a plausible synthetic OHLCV DataFrame of length n."""
    rng    = np.random.default_rng(seed)
    close  = 400.0 * np.exp(np.cumsum(rng.normal(0.0003, 0.012, n)))
    noise  = rng.uniform(0.995, 1.005, n)
    high   = close * noise * rng.uniform(1.000, 1.015, n)
    low    = close * noise * rng.uniform(0.985, 1.000, n)
    open_  = close * rng.uniform(0.995, 1.005, n)
    volume = rng.integers(1_000_000, 10_000_000, n).astype(float)
    return pd.DataFrame({
        "open": open_, "high": high, "low": low,
        "close": close, "volume": volume,
    })


def _train_hmm(features: np.ndarray, n_states: int = 4) -> HMMEngine:
    """Train an HMMEngine with fixed n_states (fast, for testing)."""
    from hmmlearn.hmm import GaussianHMM
    cfg    = HMMEngineConfig(n_states_range=(n_states, n_states), n_init=3, random_state=0)
    engine = HMMEngine(config=cfg)
    engine.fit(features)
    return engine


# ---------------------------------------------------------------------------
# Core look-ahead bias test  (from the video spec)
# ---------------------------------------------------------------------------

class TestNoLookAheadBias:

    @pytest.fixture(scope="class")
    def setup(self):
        fe      = FeatureEngineer()
        df      = _make_synthetic_ohlcv(700)
        feats   = fe.build_feature_matrix(df)
        engine  = _train_hmm(feats)
        return engine, feats

    def test_prediction_at_T_identical_with_short_and_long_sequence(self, setup):
        """
        predict_regime_filtered(data[0:T])[-1]
        must equal
        predict_regime_filtered(data[0:T+100])[T-1].

        Any difference means the algorithm looked into the future.
        """
        engine, feats = setup
        T = 400

        short_states = engine.predict_regime_filtered(feats[:T])
        long_states  = engine.predict_regime_filtered(feats[:T + 100])

        regime_at_T_short = short_states[-1]          # last element of short run
        regime_at_T_long  = long_states[T - 1]        # element T-1 of long run

        assert regime_at_T_short == regime_at_T_long, (
            f"LOOK-AHEAD BIAS DETECTED: "
            f"short={regime_at_T_short.label!r} "
            f"long={regime_at_T_long.label!r}"
        )

    def test_probabilities_at_T_identical_with_short_and_long_sequence(self, setup):
        """Posterior probabilities must also be identical — not just the argmax."""
        engine, feats = setup
        T = 300

        short = engine.predict_regime_filtered(feats[:T])[-1]
        long  = engine.predict_regime_filtered(feats[:T + 150])[T - 1]

        np.testing.assert_allclose(
            short.state_probabilities,
            long.state_probabilities,
            atol=1e-6,
            err_msg="LOOK-AHEAD BIAS: posterior probabilities differ when future data added.",
        )

    def test_multiple_cut_points(self, setup):
        """Spot-check 5 random cut points throughout the sequence."""
        engine, feats = setup
        rng = np.random.default_rng(99)
        cut_points = rng.integers(200, len(feats) - 50, size=5)

        for T in cut_points:
            short = engine.predict_regime_filtered(feats[:T])[-1]
            long  = engine.predict_regime_filtered(feats[:T + 50])[T - 1]
            assert short == long, (
                f"LOOK-AHEAD BIAS at T={T}: "
                f"short={short.label!r}, long={long.label!r}"
            )
