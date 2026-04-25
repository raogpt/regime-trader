"""
Feature engineering for HMM training and inference.

Computes 14 forward-safe features from raw OHLCV data:
  Returns (3): log_ret_1, log_ret_5, log_ret_20
  Volatility (2): realized_vol, vol_ratio
  Volume (2): norm_volume, volume_trend
  Trend (2): adx_14, sma50_slope
  Mean reversion (2): rsi14_zscore, dist_sma200_pct
  Momentum (2): roc_10, roc_20
  Range (1): norm_atr

All features are standardised with a 252-period rolling z-score
before being passed to the HMM.
"""

from __future__ import annotations

import logging
from collections import deque
from typing import Optional

import numpy as np
import pandas as pd
from scipy.special import logsumexp  # noqa: F401  (imported here; used in hmm_engine)

logger = logging.getLogger(__name__)

FEATURE_NAMES: list[str] = [
    "log_ret_1",
    "log_ret_5",
    "log_ret_20",
    "realized_vol",
    "vol_ratio",
    "norm_volume",
    "volume_trend",
    "adx_14",
    "sma50_slope",
    "rsi14_zscore",
    "dist_sma200_pct",
    "roc_10",
    "roc_20",
    "norm_atr",
]

_ZSCORE_WINDOW = 252   # rolling lookback for standardisation
_MAX_BUFFER    = 300   # bars kept in the live-trading rolling buffer


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _rolling_slope(series: pd.Series, window: int) -> pd.Series:
    """OLS slope of a rolling window (returns NaN when not enough data)."""
    x = np.arange(window, dtype=float)
    x -= x.mean()
    denom = float(np.dot(x, x))

    def _slope(y: np.ndarray) -> float:
        if np.isnan(y).any():
            return np.nan
        return float(np.dot(x, y) / denom)

    return series.rolling(window, min_periods=window).apply(_slope, raw=True)


def _compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta     = close.diff()
    gain      = delta.clip(lower=0.0)
    loss      = (-delta).clip(lower=0.0)
    avg_gain  = gain.ewm(com=period - 1, adjust=False).mean()
    avg_loss  = loss.ewm(com=period - 1, adjust=False).mean()
    rs        = avg_gain / (avg_loss + 1e-10)
    return 100.0 - 100.0 / (1.0 + rs)


def _compute_atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    h, l, c   = df["high"], df["low"], df["close"]
    prev_c    = c.shift(1)
    tr        = pd.concat([h - l, (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    return tr.rolling(period, min_periods=period).mean()


def _compute_adx(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """Average Directional Index using Wilder's smoothing."""
    h, l, c   = df["high"], df["low"], df["close"]
    prev_c    = c.shift(1)
    prev_h    = h.shift(1)
    prev_l    = l.shift(1)

    tr        = pd.concat([h - l, (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)

    up_move   = h - prev_h
    down_move = prev_l - l

    plus_dm   = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm  = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)
    plus_dm   = pd.Series(plus_dm,  index=df.index)
    minus_dm  = pd.Series(minus_dm, index=df.index)

    alpha     = 1.0 / period
    atr_w     = tr.ewm(alpha=alpha, adjust=False).mean()
    plus_di   = 100.0 * plus_dm.ewm(alpha=alpha,  adjust=False).mean() / (atr_w + 1e-10)
    minus_di  = 100.0 * minus_dm.ewm(alpha=alpha, adjust=False).mean() / (atr_w + 1e-10)

    dx        = 100.0 * (plus_di - minus_di).abs() / (plus_di + minus_di + 1e-10)
    return dx.ewm(alpha=alpha, adjust=False).mean()


def _rolling_zscore(series: pd.Series, window: int = _ZSCORE_WINDOW) -> pd.Series:
    min_p = max(30, window // 4)
    mu    = series.rolling(window, min_periods=min_p).mean()
    sigma = series.rolling(window, min_periods=min_p).std()
    return (series - mu) / (sigma + 1e-10)


# ---------------------------------------------------------------------------
# FeatureEngineer
# ---------------------------------------------------------------------------

class FeatureEngineer:
    """
    Transforms raw OHLCV DataFrames into the feature matrix consumed by
    HMMEngine.  All computations are forward-safe (no future data leaks).

    Expected DataFrame columns (case-sensitive):
        open, high, low, close, volume
    """

    def __init__(self) -> None:
        # Rolling buffer for incremental live updates
        self._buffer: Optional[pd.DataFrame] = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def build_feature_matrix(self, df: pd.DataFrame) -> np.ndarray:
        """
        Return a (n_samples × 14) float64 array.
        Rows with NaN in any feature are dropped.
        """
        fdf = self.build_feature_dataframe(df)
        return fdf.values.astype(np.float64)

    def build_feature_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Same as build_feature_matrix but returns a labelled DataFrame
        (index aligned with the input df after NaN rows are dropped).
        """
        df = df.copy()
        df.columns = [c.lower() for c in df.columns]

        c = df["close"]
        h = df["high"]
        l = df["low"]
        v = df["volume"]

        raw: dict[str, pd.Series] = {}

        # --- Returns ---
        raw["log_ret_1"]  = np.log(c / c.shift(1))
        raw["log_ret_5"]  = np.log(c / c.shift(5))
        raw["log_ret_20"] = np.log(c / c.shift(20))

        # --- Volatility ---
        raw["realized_vol"] = raw["log_ret_1"].rolling(20, min_periods=10).std()
        vol5               = raw["log_ret_1"].rolling(5,  min_periods=3).std()
        vol20              = raw["log_ret_1"].rolling(20, min_periods=10).std()
        raw["vol_ratio"]   = vol5 / (vol20 + 1e-10)

        # --- Volume ---
        vol_mean50         = v.rolling(50, min_periods=25).mean()
        vol_std50          = v.rolling(50, min_periods=25).std()
        raw["norm_volume"] = (v - vol_mean50) / (vol_std50 + 1e-10)
        raw["volume_trend"]= _rolling_slope(v.rolling(10, min_periods=5).mean(), 10)

        # --- Trend ---
        raw["adx_14"]      = _compute_adx(df, 14)
        sma50              = c.rolling(50, min_periods=25).mean()
        raw["sma50_slope"] = _rolling_slope(sma50, 10) / (c + 1e-10)

        # --- Mean reversion ---
        rsi14              = _compute_rsi(c, 14)
        raw["rsi14_zscore"]= _rolling_zscore(rsi14, _ZSCORE_WINDOW)
        sma200             = c.rolling(200, min_periods=100).mean()
        raw["dist_sma200_pct"] = (c - sma200) / (c + 1e-10)

        # --- Momentum ---
        raw["roc_10"] = (c / c.shift(10) - 1.0)
        raw["roc_20"] = (c / c.shift(20) - 1.0)

        # --- Range ---
        raw["norm_atr"] = _compute_atr(df, 14) / (c + 1e-10)

        # Assemble and apply rolling z-score standardisation
        feat_df = pd.DataFrame(raw, index=df.index)
        for col in FEATURE_NAMES:
            feat_df[col] = _rolling_zscore(feat_df[col], _ZSCORE_WINDOW)

        feat_df = feat_df[FEATURE_NAMES].replace([np.inf, -np.inf], np.nan).dropna()
        return feat_df

    # ------------------------------------------------------------------
    # Incremental update for live trading
    # ------------------------------------------------------------------

    def update_with_new_bar(self, new_bar: dict) -> Optional[np.ndarray]:
        """
        Append a single new bar to the internal rolling buffer and return
        the feature vector for that bar (shape: (1, 14)).

        `new_bar` must have keys: open, high, low, close, volume.
        Returns None if the buffer does not yet have enough history.
        """
        row = pd.DataFrame([{k.lower(): v for k, v in new_bar.items()}])

        if self._buffer is None:
            self._buffer = row
        else:
            self._buffer = pd.concat([self._buffer, row], ignore_index=True)
            if len(self._buffer) > _MAX_BUFFER:
                self._buffer = self._buffer.iloc[-_MAX_BUFFER:].reset_index(drop=True)

        feat_df = self.build_feature_dataframe(self._buffer)
        if len(feat_df) == 0:
            return None

        return feat_df.iloc[-1:].values.astype(np.float64)

    def reset_buffer(self) -> None:
        """Clear the internal rolling buffer (e.g. on reconnect)."""
        self._buffer = None
