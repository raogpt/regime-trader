"""
HMM regime-detection engine.

Classifies the current market environment into labelled regimes using a
Gaussian HMM trained on 14 forward-safe features.

Key design choices
------------------
* BIC-based automatic selection of n_states ∈ [3, 7].
* FORWARD ALGORITHM ONLY for inference — never model.predict() (Viterbi),
  which would introduce look-ahead bias.
* Stability filter: regime change confirmed only after N consecutive bars.
* Flickering detection: uncertainty mode when regime flips too often.
"""

from __future__ import annotations

import logging
import pickle
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import numpy as np
from scipy.special import logsumexp
from scipy.stats import multivariate_normal

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Regime label maps
# ---------------------------------------------------------------------------

_LABEL_MAP: dict[int, list[str]] = {
    3: ["bear",        "neutral",     "bull"],
    4: ["crash",       "bear",        "bull",        "euphoria"],
    5: ["crash",       "bear",        "neutral",     "bull",        "euphoria"],
    6: ["crash",       "strong_bear", "weak_bear",   "weak_bull",   "strong_bull", "euphoria"],
    7: ["crash",       "strong_bear", "weak_bear",   "neutral",     "weak_bull",   "strong_bull", "euphoria"],
}

# Default RegimeInfo parameters keyed by label name
_REGIME_DEFAULTS: dict[str, dict] = {
    "crash":       dict(expected_return=-0.25, expected_volatility=0.50, recommended_strategy="cash",        max_leverage=1.0, max_pos_pct=0.05, min_conf=0.70),
    "strong_bear": dict(expected_return=-0.15, expected_volatility=0.35, recommended_strategy="defensive",   max_leverage=1.0, max_pos_pct=0.20, min_conf=0.65),
    "bear":        dict(expected_return=-0.10, expected_volatility=0.25, recommended_strategy="defensive",   max_leverage=1.0, max_pos_pct=0.25, min_conf=0.60),
    "weak_bear":   dict(expected_return=-0.05, expected_volatility=0.20, recommended_strategy="reduced",     max_leverage=1.0, max_pos_pct=0.35, min_conf=0.55),
    "neutral":     dict(expected_return= 0.05, expected_volatility=0.15, recommended_strategy="moderate",    max_leverage=1.0, max_pos_pct=0.55, min_conf=0.50),
    "weak_bull":   dict(expected_return= 0.10, expected_volatility=0.15, recommended_strategy="growth",      max_leverage=1.1, max_pos_pct=0.70, min_conf=0.50),
    "bull":        dict(expected_return= 0.18, expected_volatility=0.12, recommended_strategy="aggressive",  max_leverage=1.25,max_pos_pct=0.90, min_conf=0.45),
    "strong_bull": dict(expected_return= 0.22, expected_volatility=0.12, recommended_strategy="aggressive",  max_leverage=1.25,max_pos_pct=0.90, min_conf=0.45),
    "euphoria":    dict(expected_return= 0.08, expected_volatility=0.20, recommended_strategy="cautious",    max_leverage=1.0, max_pos_pct=0.45, min_conf=0.60),
}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class RegimeInfo:
    regime_id:             int
    regime_name:           str
    expected_return:       float
    expected_volatility:   float
    recommended_strategy:  str
    max_leverage_allowed:  float
    max_position_size_pct: float
    min_confidence_to_act: float


@dataclass
class RegimeState:
    label:              str
    state_id:           int           # rank after sort by mean return
    probability:        float         # P(state_t | obs_1:t)
    state_probabilities: np.ndarray   # full posterior vector over all states
    timestamp:          datetime
    is_confirmed:       bool          # passed stability filter
    consecutive_bars:   int

    def __eq__(self, other: object) -> bool:
        if isinstance(other, RegimeState):
            return self.label == other.label and self.state_id == other.state_id
        return NotImplemented

    def __repr__(self) -> str:
        return (f"RegimeState(label={self.label!r}, prob={self.probability:.2f}, "
                f"confirmed={self.is_confirmed}, bars={self.consecutive_bars})")


@dataclass
class HMMEngineConfig:
    n_states_range:         tuple = (3, 7)
    n_init:                 int   = 10
    training_days:          int   = 504
    retrain_interval_days:  int   = 21
    stability_bars:         int   = 3
    instability_window:     int   = 20
    instability_threshold:  int   = 4
    random_state:           int   = 42


# ---------------------------------------------------------------------------
# HMMEngine
# ---------------------------------------------------------------------------

class HMMEngine:
    """
    Trains a Gaussian HMM on market features and detects the current regime
    using the forward algorithm only (no look-ahead bias).
    """

    def __init__(self, config: Optional[HMMEngineConfig] = None) -> None:
        self.config         = config or HMMEngineConfig()
        self.model          = None          # fitted hmmlearn.GaussianHMM
        self.n_states: int  = 0
        self.regime_labels: list[str] = []
        self._sorted_indices: Optional[np.ndarray] = None   # rank → raw state
        self._state_to_rank:  Optional[np.ndarray] = None   # raw state → rank
        self._best_bic: float = np.inf

        # Stability filter state
        self._confirmed_state:  Optional[RegimeState] = None
        self._pending_label:    Optional[str]          = None
        self._pending_bars:     int                    = 0
        self._consecutive_bars: int                    = 0
        self._recent_labels:    deque                  = deque(maxlen=self.config.instability_window)

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def fit(self, features: np.ndarray) -> None:
        """
        Fit the HMM on a 2-D feature matrix (n_samples × n_features).
        Automatically selects n_states via BIC.
        Logs likelihood, BIC, convergence, and iteration count.
        """
        try:
            from hmmlearn.hmm import GaussianHMM
        except ImportError as e:
            raise ImportError("hmmlearn is required: pip install hmmlearn") from e

        best_n, best_bic, best_model = self._select_n_states(features)

        self.model        = best_model
        self.n_states     = best_n
        self._best_bic    = best_bic
        self._sort_states_by_mean_return(features)
        self._assign_labels()

        logger.info(
            "HMM fitted | n_states=%d | BIC=%.2f | monitor=%s | iters=%d",
            self.n_states, best_bic,
            "converged" if best_model.monitor_.converged else "NOT converged",
            best_model.monitor_.iter,
        )

    def _select_n_states(self, features: np.ndarray):
        """Test each n in config range; return (best_n, best_bic, best_model)."""
        from hmmlearn.hmm import GaussianHMM

        lo, hi = self.config.n_states_range
        best_n, best_bic, best_model = lo, np.inf, None
        bic_scores: dict[int, float] = {}

        for n in range(lo, hi + 1):
            candidate_model, candidate_ll = None, -np.inf

            for seed in range(self.config.n_init):
                try:
                    m = GaussianHMM(
                        n_components=n,
                        covariance_type="full",
                        n_iter=100,
                        tol=1e-4,
                        random_state=self.config.random_state + seed,
                    )
                    m.fit(features)
                    ll = m.score(features)
                    if ll > candidate_ll:
                        candidate_ll    = ll
                        candidate_model = m
                except Exception as exc:
                    logger.debug("n_states=%d seed=%d failed: %s", n, seed, exc)

            if candidate_model is None:
                logger.warning("All initialisations failed for n_states=%d — skipping", n)
                continue

            bic = self._compute_bic(candidate_model, features)
            bic_scores[n] = bic
            logger.info("n_states=%d | BIC=%.2f | log-likelihood=%.2f", n, bic, candidate_ll)

            if bic < best_bic:
                best_bic   = bic
                best_n     = n
                best_model = candidate_model

        logger.info("BIC scores: %s → selected n_states=%d", bic_scores, best_n)
        return best_n, best_bic, best_model

    def _compute_bic(self, model, features: np.ndarray) -> float:
        """
        BIC = -2 × log_likelihood + n_params × log(n_samples)

        For GaussianHMM with covariance_type="full":
          n_params = (n-1)           # start probabilities
                   + n*(n-1)        # transition matrix rows
                   + n*d            # means
                   + n*d*(d+1)//2   # unique entries per full covariance
        """
        n, d = model.n_components, features.shape[1]
        n_params = (
            (n - 1)
            + n * (n - 1)
            + n * d
            + n * d * (d + 1) // 2
        )
        ll = model.score(features)
        return -2.0 * ll + n_params * np.log(len(features))

    def _sort_states_by_mean_return(self, features: np.ndarray) -> None:
        """
        Sort HMM states by their mean of feature-0 (log_ret_1, ascending).
        Populates _sorted_indices (rank → raw state) and
                  _state_to_rank  (raw state → rank).
        """
        mean_returns       = self.model.means_[:, 0]
        self._sorted_indices = np.argsort(mean_returns)          # rank→raw
        self._state_to_rank  = np.argsort(self._sorted_indices)  # raw→rank

    def _assign_labels(self) -> None:
        """Map sorted rank indices to human-readable regime labels."""
        self.regime_labels = _LABEL_MAP.get(self.n_states, [str(i) for i in range(self.n_states)])

    # ------------------------------------------------------------------
    # Forward-only inference  (*** NO look-ahead bias ***)
    # ------------------------------------------------------------------

    def predict_regime_filtered(self, features: np.ndarray) -> list[RegimeState]:
        """
        Compute P(state_t | obs_1:t) using the forward algorithm only.
        Returns one RegimeState per time step (no stability filter applied).

        *** NEVER calls model.predict() (Viterbi) — that uses future data. ***
        """
        if not self.is_fitted():
            raise RuntimeError("HMMEngine must be fitted before prediction.")

        log_alpha  = self._forward_algorithm(features)    # (T, K) log posteriors
        posteriors = np.exp(log_alpha)                    # (T, K) normalised

        states: list[RegimeState] = []
        now = datetime.now(timezone.utc)

        for t in range(len(features)):
            probs      = posteriors[t]
            raw_best   = int(np.argmax(probs))
            rank       = int(self._state_to_rank[raw_best])
            label      = self.regime_labels[rank]

            # Remap probabilities to sorted-rank order
            sorted_probs = probs[self._sorted_indices]

            states.append(RegimeState(
                label               = label,
                state_id            = rank,
                probability         = float(probs[raw_best]),
                state_probabilities = sorted_probs,
                timestamp           = now,
                is_confirmed        = False,
                consecutive_bars    = 0,
            ))

        return states

    def _forward_algorithm(self, features: np.ndarray) -> np.ndarray:
        """
        Manual forward pass in log space for numerical stability.

        Algorithm:
          alpha_0    = log(pi) + log_emit(obs_0)
          alpha_t[j] = logsumexp_i(alpha_{t-1}[i] + log A[i,j]) + log_emit_t[j]
          Normalise each row so rows stay interpretable as log-posteriors.

        Returns log_alpha of shape (T, n_states).
        """
        T          = len(features)
        K          = self.n_states
        log_A      = np.log(self.model.transmat_ + 1e-300)     # (K, K)
        log_pi     = np.log(self.model.startprob_ + 1e-300)    # (K,)
        log_alpha  = np.empty((T, K), dtype=np.float64)

        # t = 0
        log_emit_0     = self._log_emission_probs(features[0])
        log_alpha[0]   = log_pi + log_emit_0
        log_alpha[0]  -= logsumexp(log_alpha[0])

        # t = 1 … T-1  (vectorised over states j)
        for t in range(1, T):
            log_emit_t = self._log_emission_probs(features[t])
            # For each j: logsumexp_i(alpha[t-1,i] + log A[i,j])
            # = logsumexp over axis=0 of (alpha[t-1].reshape(K,1) + log_A)
            log_alpha[t]  = logsumexp(
                log_alpha[t - 1].reshape(-1, 1) + log_A, axis=0
            ) + log_emit_t
            log_alpha[t] -= logsumexp(log_alpha[t])

        return log_alpha

    def _log_emission_probs(self, obs: np.ndarray) -> np.ndarray:
        """Return log P(obs | state_i) for all i using Gaussian density."""
        log_probs = np.empty(self.n_states, dtype=np.float64)
        for i in range(self.n_states):
            try:
                log_probs[i] = multivariate_normal.logpdf(
                    obs,
                    mean=self.model.means_[i],
                    cov=self.model.covars_[i],
                    allow_singular=True,
                )
            except Exception:
                log_probs[i] = -1e300
        return log_probs

    # ------------------------------------------------------------------
    # Stability filter
    # ------------------------------------------------------------------

    def predict_regime(self, features: np.ndarray) -> RegimeState:
        """
        Main entry point for live trading.
        Runs predict_regime_filtered on `features`, then applies the
        stability filter to the last bar.
        """
        raw_states = self.predict_regime_filtered(features)
        candidate  = raw_states[-1]
        return self._apply_stability_filter(candidate)

    def _apply_stability_filter(self, candidate: RegimeState) -> RegimeState:
        """
        Confirm a regime only after `stability_bars` consecutive identical
        predictions.  During transition keep the previous confirmed label.
        If flickering, mark is_confirmed=False regardless.
        """
        self._recent_labels.append(candidate.label)

        # First-ever prediction
        if self._confirmed_state is None:
            self._pending_label    = candidate.label
            self._pending_bars     = 1
            self._consecutive_bars = 1
            candidate.is_confirmed    = False
            candidate.consecutive_bars = 1
            self._confirmed_state  = candidate
            return candidate

        confirmed_label = self._confirmed_state.label

        if candidate.label == confirmed_label:
            # Continuing in confirmed regime
            self._consecutive_bars += 1
            self._pending_label     = None
            self._pending_bars      = 0
            candidate.is_confirmed    = not self._is_flickering()
            candidate.consecutive_bars = self._consecutive_bars
            self._confirmed_state   = candidate

        elif candidate.label == self._pending_label:
            # Building towards a new regime
            self._pending_bars += 1
            if self._pending_bars >= self.config.stability_bars:
                # Regime change confirmed
                self.log_regime_change(self._confirmed_state, candidate)
                self._consecutive_bars = self._pending_bars
                self._pending_label    = None
                self._pending_bars     = 0
                candidate.is_confirmed    = not self._is_flickering()
                candidate.consecutive_bars = self._consecutive_bars
                self._confirmed_state  = candidate
            else:
                # Still transitioning — return previous confirmed regime
                return self._transition_state(candidate)

        else:
            # Brand-new candidate, reset pending
            self._pending_label = candidate.label
            self._pending_bars  = 1
            return self._transition_state(candidate)

        return candidate

    def _transition_state(self, candidate: RegimeState) -> RegimeState:
        """Return a copy of the confirmed state stamped with the current timestamp."""
        cs = self._confirmed_state
        return RegimeState(
            label               = cs.label,
            state_id            = cs.state_id,
            probability         = cs.probability,
            state_probabilities = cs.state_probabilities,
            timestamp           = candidate.timestamp,
            is_confirmed        = False,
            consecutive_bars    = self._consecutive_bars,
        )

    def _is_flickering(self) -> bool:
        """True if regime flipped more than instability_threshold times in the window."""
        labels = list(self._recent_labels)
        if len(labels) < 2:
            return False
        flips = sum(1 for a, b in zip(labels, labels[1:]) if a != b)
        return flips > self.config.instability_threshold

    # ------------------------------------------------------------------
    # Additional public methods
    # ------------------------------------------------------------------

    def predict_regime_proba(self, features: np.ndarray) -> np.ndarray:
        """Return the posterior probability distribution for the last bar."""
        raw_states = self.predict_regime_filtered(features)
        return raw_states[-1].state_probabilities

    def get_regime_stability(self) -> int:
        """Return the number of consecutive bars in the current confirmed regime."""
        return self._consecutive_bars

    def get_transition_matrix(self) -> np.ndarray:
        """Return the learned transition probability matrix (n_states × n_states)."""
        if not self.is_fitted():
            raise RuntimeError("Model not fitted.")
        # Re-order rows and columns to match sorted-rank labelling
        idx = self._sorted_indices
        return self.model.transmat_[np.ix_(idx, idx)]

    def detect_regime_change(self) -> bool:
        """Return True only when the most recent bar confirmed a new regime."""
        if self._confirmed_state is None:
            return False
        return (
            self._confirmed_state.is_confirmed
            and self._consecutive_bars == self.config.stability_bars
        )

    def get_regime_flicker_rate(self) -> float:
        """Return the number of regime flips in the current instability window."""
        labels = list(self._recent_labels)
        if len(labels) < 2:
            return 0.0
        return float(sum(1 for a, b in zip(labels, labels[1:]) if a != b))

    def is_flickering(self) -> bool:
        """True if flicker rate exceeds instability_threshold."""
        return self._is_flickering()

    def get_regime_info(self, label: str) -> RegimeInfo:
        """Return the RegimeInfo metadata for a given regime label."""
        defaults = _REGIME_DEFAULTS.get(label, _REGIME_DEFAULTS["neutral"])
        rank     = self.regime_labels.index(label) if label in self.regime_labels else -1
        return RegimeInfo(
            regime_id             = rank,
            regime_name           = label,
            expected_return       = defaults["expected_return"],
            expected_volatility   = defaults["expected_volatility"],
            recommended_strategy  = defaults["recommended_strategy"],
            max_leverage_allowed  = defaults["max_leverage"],
            max_position_size_pct = defaults["max_pos_pct"],
            min_confidence_to_act = defaults["min_conf"],
        )

    def get_current_regime(self) -> Optional[RegimeState]:
        """Return the most recent confirmed RegimeState, or None if not fitted."""
        return self._confirmed_state

    def log_regime_change(self, previous: RegimeState, current: RegimeState) -> None:
        logger.warning(
            "REGIME CHANGE: %s → %s (confidence=%.2f)",
            previous.label, current.label, current.probability,
        )

    def is_fitted(self) -> bool:
        return self.model is not None

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, path: str) -> None:
        """Pickle the model and metadata to `path`."""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "model":          self.model,
            "n_states":       self.n_states,
            "regime_labels":  self.regime_labels,
            "sorted_indices": self._sorted_indices,
            "state_to_rank":  self._state_to_rank,
            "bic":            self._best_bic,
            "training_date":  datetime.now(timezone.utc).isoformat(),
            "config":         self.config,
            "feature_names":  None,  # populated by caller if needed
        }
        with open(path, "wb") as fh:
            pickle.dump(payload, fh)
        logger.info("Model saved → %s  (n_states=%d, BIC=%.2f)", path, self.n_states, self._best_bic)

    @classmethod
    def load(cls, path: str) -> "HMMEngine":
        """Load a previously saved HMMEngine from `path`."""
        with open(path, "rb") as fh:
            payload = pickle.load(fh)
        engine                   = cls(config=payload.get("config"))
        engine.model             = payload["model"]
        engine.n_states          = payload["n_states"]
        engine.regime_labels     = payload["regime_labels"]
        engine._sorted_indices   = payload["sorted_indices"]
        engine._state_to_rank    = payload["state_to_rank"]
        engine._best_bic         = payload["bic"]
        logger.info("Model loaded ← %s  (n_states=%d)", path, engine.n_states)
        return engine
