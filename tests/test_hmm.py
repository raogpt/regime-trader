"""
Unit tests for HMMEngine and FeatureEngineer.

Covers:
  - BIC-based n_states selection
  - Label assignment by mean return
  - Forward algorithm posterior validity
  - No look-ahead bias (quick version; full version in test_look_ahead.py)
  - Stability filter (consecutive-bar requirement)
  - Flickering detection → uncertainty mode
  - Model save / load round-trip
  - Feature matrix NaN-free
  - Rolling z-score standardisation
"""

from __future__ import annotations

import pickle
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from data.feature_engineering import FeatureEngineer, FEATURE_NAMES
from models.hmm_engine import HMMEngine, HMMEngineConfig, RegimeState


# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

def _make_ohlcv(n: int = 600, seed: int = 7) -> pd.DataFrame:
    rng   = np.random.default_rng(seed)
    close = 300.0 * np.exp(np.cumsum(rng.normal(0.0002, 0.010, n)))
    high  = close * rng.uniform(1.000, 1.012, n)
    low   = close * rng.uniform(0.988, 1.000, n)
    open_ = close * rng.uniform(0.996, 1.004, n)
    vol   = rng.integers(500_000, 8_000_000, n).astype(float)
    return pd.DataFrame({"open": open_, "high": high, "low": low,
                          "close": close, "volume": vol})


@pytest.fixture(scope="module")
def ohlcv():
    return _make_ohlcv()


@pytest.fixture(scope="module")
def feature_matrix(ohlcv):
    return FeatureEngineer().build_feature_matrix(ohlcv)


@pytest.fixture(scope="module")
def fitted_engine(feature_matrix):
    cfg = HMMEngineConfig(n_states_range=(4, 5), n_init=3, random_state=0)
    eng = HMMEngine(config=cfg)
    eng.fit(feature_matrix)
    return eng


# ---------------------------------------------------------------------------
# Feature engineering tests
# ---------------------------------------------------------------------------

class TestFeatureMatrix:

    def test_no_nan_in_output(self, feature_matrix):
        assert not np.isnan(feature_matrix).any(), \
            "Feature matrix contains NaN values."

    def test_correct_number_of_features(self, feature_matrix):
        assert feature_matrix.shape[1] == len(FEATURE_NAMES), \
            f"Expected {len(FEATURE_NAMES)} features, got {feature_matrix.shape[1]}."

    def test_sufficient_rows_retained(self, feature_matrix):
        assert feature_matrix.shape[0] >= 200, \
            "Too few rows survived NaN drop — check lookback windows."

    def test_rolling_zscore_standardisation(self, ohlcv):
        fe  = FeatureEngineer()
        fdf = fe.build_feature_dataframe(ohlcv)
        # After z-scoring each column should have |mean| << 1 and std ≈ 1
        for col in FEATURE_NAMES:
            col_mean = fdf[col].mean()
            col_std  = fdf[col].std()
            assert abs(col_mean) < 1.0,  f"{col}: mean {col_mean:.3f} not near 0."
            assert 0.5 < col_std < 3.0,  f"{col}: std {col_std:.3f} not near 1."


# ---------------------------------------------------------------------------
# HMM training tests
# ---------------------------------------------------------------------------

class TestHMMFit:

    def test_fit_runs_without_error(self, feature_matrix):
        cfg = HMMEngineConfig(n_states_range=(3, 3), n_init=2, random_state=0)
        eng = HMMEngine(config=cfg)
        eng.fit(feature_matrix)
        assert eng.is_fitted()

    def test_n_states_in_valid_range(self, fitted_engine):
        lo, hi = fitted_engine.config.n_states_range
        assert lo <= fitted_engine.n_states <= hi

    def test_regime_labels_assigned(self, fitted_engine):
        assert len(fitted_engine.regime_labels) == fitted_engine.n_states
        assert all(isinstance(lbl, str) for lbl in fitted_engine.regime_labels)

    def test_bic_selects_valid_n_states(self, feature_matrix):
        cfg = HMMEngineConfig(n_states_range=(3, 5), n_init=2, random_state=0)
        eng = HMMEngine(config=cfg)
        eng.fit(feature_matrix)
        assert 3 <= eng.n_states <= 5
        assert eng._best_bic < np.inf

    def test_labels_assigned_by_mean_return(self, fitted_engine):
        """States must be sorted ascending by mean of feature-0 (log_ret_1)."""
        means = fitted_engine.model.means_[:, 0]
        sorted_means = means[fitted_engine._sorted_indices]
        diffs = np.diff(sorted_means)
        assert (diffs >= -1e-6).all(), \
            "Regime labels are not sorted by ascending mean return."


# ---------------------------------------------------------------------------
# Forward algorithm tests
# ---------------------------------------------------------------------------

class TestForwardAlgorithm:

    def test_posteriors_sum_to_one(self, fitted_engine, feature_matrix):
        states = fitted_engine.predict_regime_filtered(feature_matrix[:100])
        for s in states:
            total = s.state_probabilities.sum()
            assert abs(total - 1.0) < 1e-5, \
                f"Posterior probabilities sum to {total:.6f}, not 1."

    def test_probability_in_unit_interval(self, fitted_engine, feature_matrix):
        states = fitted_engine.predict_regime_filtered(feature_matrix[:100])
        for s in states:
            assert 0.0 <= s.probability <= 1.0 + 1e-9

    def test_returns_one_state_per_bar(self, fitted_engine, feature_matrix):
        T      = 80
        states = fitted_engine.predict_regime_filtered(feature_matrix[:T])
        assert len(states) == T

    def test_future_data_does_not_change_past_prediction(self, fitted_engine, feature_matrix):
        T     = 250
        short = fitted_engine.predict_regime_filtered(feature_matrix[:T])[-1]
        long  = fitted_engine.predict_regime_filtered(feature_matrix[:T + 80])[T - 1]
        assert short == long, "Look-ahead bias detected in forward algorithm."


# ---------------------------------------------------------------------------
# Stability filter tests
# ---------------------------------------------------------------------------

class TestStabilityFilter:

    def _engine_with_n(self, n: int = 3) -> tuple[HMMEngine, np.ndarray]:
        ohlcv = _make_ohlcv(600)
        feats = FeatureEngineer().build_feature_matrix(ohlcv)
        cfg   = HMMEngineConfig(n_states_range=(n, n), n_init=2,
                                stability_bars=3, random_state=0)
        eng   = HMMEngine(config=cfg)
        eng.fit(feats)
        return eng, feats

    def test_regime_requires_min_consecutive_bars(self):
        eng, feats = self._engine_with_n(3)
        # Feed bars one at a time; confirmed should not flip immediately
        confirmed_labels: list[str] = []
        for t in range(50, 70):
            result = eng.predict_regime(feats[:t])
            confirmed_labels.append(result.label)
        # The confirmed regime should change at most len//3 times (stability=3)
        flips = sum(1 for a, b in zip(confirmed_labels, confirmed_labels[1:]) if a != b)
        assert flips <= len(confirmed_labels) // 3

    def test_flickering_detected(self):
        """Inject artificial rapid label changes and verify is_flickering()."""
        cfg = HMMEngineConfig(n_states_range=(3, 3), n_init=2, stability_bars=3,
                               instability_window=10, instability_threshold=3,
                               random_state=0)
        ohlcv = _make_ohlcv(600)
        feats = FeatureEngineer().build_feature_matrix(ohlcv)
        eng   = HMMEngine(config=cfg)
        eng.fit(feats)

        # Manually stuff alternating labels into the recent history
        from itertools import cycle
        labels = cycle(["bear", "bull", "bear", "bull"])
        for _ in range(10):
            eng._recent_labels.append(next(labels))

        assert eng.is_flickering(), "Expected flickering to be detected."


# ---------------------------------------------------------------------------
# Model persistence tests
# ---------------------------------------------------------------------------

class TestModelSaveLoad:

    def test_model_save_and_load(self, fitted_engine, feature_matrix, tmp_path):
        path = str(tmp_path / "hmm_model.pkl")
        fitted_engine.save(path)
        assert Path(path).exists()

        loaded = HMMEngine.load(path)
        assert loaded.n_states      == fitted_engine.n_states
        assert loaded.regime_labels == fitted_engine.regime_labels

        # Predictions must match after reload
        preds_orig   = fitted_engine.predict_regime_filtered(feature_matrix[:100])
        preds_loaded = loaded.predict_regime_filtered(feature_matrix[:100])

        for orig, load in zip(preds_orig, preds_loaded):
            assert orig == load, "Label mismatch after save/load."
