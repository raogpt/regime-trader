"""
Walk-forward backtesting engine (allocation-based).

This is NOT a trade-entry/exit backtester.
It sets a TARGET PORTFOLIO ALLOCATION each bar based on the detected
volatility regime and rebalances when allocation drifts > 10 %.
This mirrors how real systematic strategies operate.

Walk-forward windows
--------------------
  In-Sample  (IS):  252 trading bars  (1 year)  — HMM training
  Out-of-Sample (OOS): 126 trading bars (6 months) — blind evaluation
  Step:             126 trading bars  (6 months)

Allocation math (exact)
-----------------------
  equity         = cash + shares * price
  target_shares  = int(equity * target_alloc / price)
  delta          = target_shares - current_shares
  cash          -= delta * fill_price       # fill_price includes slippage
  shares         = target_shares

When leverage > 1.0, target_alloc > 1.0 → cash goes negative (margin).
equity = cash + shares * price is still correct.

Realistic simulation
--------------------
  Slippage          : 0.05 % per rebalance side (configurable)
  Rebalance threshold: 10 % allocation drift (prevents churn)
  Fill delay        : 1 bar  (signal at bar N → fill at bar N+1 open)
  No individual stops in backtester (stops are live-only)
  Commission        : $0 default (Alpaca is free)

CLI usage (via main.py)
-----------------------
  python main.py backtest --symbols SPY --start 2019-01-01 --end 2024-12-31
  python main.py backtest --symbols SPY --start 2019-01-01 --end 2024-12-31 --compare
  python main.py backtest --stress-test
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from data.feature_engineering import FeatureEngineer
from models.hmm_engine import HMMEngine, HMMEngineConfig, RegimeInfo
from models.regime_strategies import StrategyOrchestrator
from utils.performance import PerformanceCalculator, PerformanceReport, CoreMetrics

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass
class BacktestConfig:
    is_bars:            int   = 252       # in-sample window
    oos_bars:           int   = 126       # out-of-sample window
    step_bars:          int   = 126       # slide per window
    initial_cash:       float = 100_000.0
    slippage_pct:       float = 0.0005   # 0.05 % per side
    rebalance_threshold:float = 0.10
    min_confidence:     float = 0.55
    hmm_n_states_range: tuple = (3, 7)
    hmm_n_init:         int   = 5
    run_benchmarks:     bool  = True


# ---------------------------------------------------------------------------
# Bar-level portfolio state
# ---------------------------------------------------------------------------

@dataclass
class PortfolioState:
    cash:       float
    shares:     int   = 0
    allocation: float = 0.0   # current allocation fraction (may exceed 1 = margin)


# ---------------------------------------------------------------------------
# Window result
# ---------------------------------------------------------------------------

@dataclass
class WindowResult:
    window_id:    int
    is_start:     int
    is_end:       int
    oos_start:    int
    oos_end:      int
    equity_curve: pd.Series          = field(default_factory=pd.Series)
    trade_log:    pd.DataFrame       = field(default_factory=pd.DataFrame)
    regime_history: pd.DataFrame     = field(default_factory=pd.DataFrame)
    core_metrics: CoreMetrics        = field(default_factory=CoreMetrics)


# ---------------------------------------------------------------------------
# WalkForwardBacktester
# ---------------------------------------------------------------------------

class WalkForwardBacktester:
    """
    Allocation-based walk-forward backtest.
    """

    def __init__(self, config: BacktestConfig | None = None) -> None:
        self.config = config or BacktestConfig()
        self._calc  = PerformanceCalculator()
        self._feat  = FeatureEngineer()

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------

    def run(self, price_df: pd.DataFrame,
             symbol: str = "SPY") -> PerformanceReport:
        """
        Execute full walk-forward test on `price_df` (OHLCV DataFrame).
        Returns a PerformanceReport aggregated across all windows.
        """
        price_df = price_df.copy()
        price_df.columns = [c.lower() for c in price_df.columns]

        windows = self._create_windows(len(price_df))
        if not windows:
            raise ValueError("Not enough data for even one walk-forward window.")

        all_equity:   list[float] = [self.config.initial_cash]
        all_trades:   list[dict]  = []
        all_regimes:  list[dict]  = []
        window_results: list[WindowResult] = []

        for w in windows:
            logger.info("Window %d: IS[%d:%d] OOS[%d:%d]",
                        w.window_id, w.is_start, w.is_end, w.oos_start, w.oos_end)
            wr = self._run_window(price_df, w, symbol,
                                   start_cash=all_equity[-1])
            window_results.append(wr)

            if len(wr.equity_curve) > 0:
                all_equity.extend(wr.equity_curve.tolist()[1:])

            if len(wr.trade_log) > 0:
                all_trades.append(wr.trade_log)

            if len(wr.regime_history) > 0:
                all_regimes.append(wr.regime_history)

        # Aggregate
        idx        = price_df.index[self.config.is_bars:]
        equity_len = min(len(all_equity), len(idx) + 1)
        equity_s   = pd.Series(all_equity[:equity_len],
                                index=pd.RangeIndex(equity_len))

        trade_log   = pd.concat(all_trades,  ignore_index=True) if all_trades  else pd.DataFrame()
        regime_hist = pd.concat(all_regimes, ignore_index=True) if all_regimes else pd.DataFrame()

        price_s = price_df["close"].iloc[self.config.is_bars:]

        report = self._calc.full_report(equity_s, trade_log,
                                         price_s.reset_index(drop=True))
        report.trade_log = trade_log

        # Save CSVs
        self._save_outputs(equity_s, trade_log, regime_hist, symbol)

        if self.config.run_benchmarks:
            report.benchmark_buy_hold = self._calc.benchmark_buy_hold(
                price_s.reset_index(drop=True), self.config.initial_cash)
            report.benchmark_sma200   = self._calc.benchmark_sma200(
                price_s.reset_index(drop=True), self.config.initial_cash)
            avg_freq = max(1, len(trade_log) // max(len(price_s) // 252, 1))
            report.benchmark_random, _ = self._calc.benchmark_random(
                price_s.reset_index(drop=True), initial_cash=self.config.initial_cash,
                avg_frequency=avg_freq)

        return report

    # ------------------------------------------------------------------
    # Window creation
    # ------------------------------------------------------------------

    def _create_windows(self, n_bars: int) -> list[WindowResult]:
        cfg     = self.config
        windows = []
        wid     = 0
        is_start = 0
        while True:
            is_end   = is_start + cfg.is_bars
            oos_end  = is_end   + cfg.oos_bars
            if oos_end > n_bars:
                break
            w = WindowResult(
                window_id = wid,
                is_start  = is_start,
                is_end    = is_end,
                oos_start = is_end,
                oos_end   = oos_end,
            )
            windows.append(w)
            is_start += cfg.step_bars
            wid      += 1
        return windows

    # ------------------------------------------------------------------
    # Single window execution
    # ------------------------------------------------------------------

    def _run_window(self, price_df: pd.DataFrame, w: WindowResult,
                     symbol: str, start_cash: float) -> WindowResult:
        cfg    = self.config
        is_df  = price_df.iloc[w.is_start : w.is_end]
        oos_df = price_df.iloc[w.oos_start: w.oos_end]

        # a. Train HMM on IS data
        is_feats = self._feat.build_feature_matrix(is_df)
        if len(is_feats) < 50:
            logger.warning("Window %d: not enough IS features (%d), skipping.",
                           w.window_id, len(is_feats))
            return w

        hmm_cfg = HMMEngineConfig(
            n_states_range = cfg.hmm_n_states_range,
            n_init         = cfg.hmm_n_init,
        )
        hmm = HMMEngine(config=hmm_cfg)
        try:
            hmm.fit(is_feats)
        except Exception as exc:
            logger.error("Window %d HMM fit failed: %s", w.window_id, exc)
            return w

        # b. Build regime_infos from HMM labels and pass to orchestrator
        regime_infos = [hmm.get_regime_info(lbl) for lbl in hmm.regime_labels]
        orchestrator = StrategyOrchestrator(
            regime_infos       = regime_infos,
            min_confidence     = cfg.min_confidence,
            rebalance_threshold= cfg.rebalance_threshold,
        )

        # c. Walk through OOS bar by bar
        state    = PortfolioState(cash=start_cash)
        equity_vals: list[float]  = [start_cash]
        trades:      list[dict]   = []
        regimes:     list[dict]   = []

        # We grow the feature window by prepending IS data
        accumulated = is_df.copy()

        for t in range(len(oos_df)):
            bar_data = oos_df.iloc[t]

            # Append current OOS bar to accumulated window
            accumulated = pd.concat([accumulated, oos_df.iloc[t:t+1]])

            # Compute features on ALL data up to current bar (no future data)
            feats = self._feat.build_feature_matrix(accumulated)
            if len(feats) < 10:
                equity_vals.append(equity_vals[-1])
                continue

            # Run forward HMM
            try:
                regime = hmm.predict_regime(feats)
            except Exception:
                equity_vals.append(equity_vals[-1])
                continue

            # Get target allocation
            bars_so_far = accumulated.reset_index(drop=True)
            target_alloc, leverage, strat_name = orchestrator.get_target_allocation(
                bars_so_far, regime, is_flickering=hmm.is_flickering()
            )

            current_price = float(bar_data["close"])
            equity        = state.cash + state.shares * current_price

            # Fill delay: execute at next bar's open (N+1)
            if t + 1 < len(oos_df) and orchestrator.needs_rebalance(
                state.allocation, target_alloc
            ):
                fill_price = float(oos_df.iloc[t + 1]["open"])
                fill_price *= (1 + cfg.slippage_pct)  # conservative: always pay slippage

                new_shares  = int(equity * target_alloc / fill_price)
                delta       = new_shares - state.shares
                old_alloc   = state.allocation

                state.cash  -= delta * fill_price
                state.shares = new_shares
                state.allocation = target_alloc

                # Record P&L as change in equity (approximate)
                pnl_pct = (equity - equity_vals[-1]) / equity_vals[-1] if equity_vals[-1] > 0 else 0.0

                trades.append(dict(
                    bar           = w.oos_start + t,
                    date          = oos_df.index[t] if hasattr(oos_df.index[t], 'isoformat') else t,
                    regime        = regime.label,
                    confidence    = regime.probability,
                    allocation_before = old_alloc,
                    allocation_after  = target_alloc,
                    leverage      = leverage,
                    strategy      = strat_name,
                    pnl_pct       = pnl_pct,
                    holding_days  = 1,
                ))

            # Mark to market at close
            equity = state.cash + state.shares * current_price
            equity_vals.append(max(equity, 0.0))

            regimes.append(dict(
                bar    = w.oos_start + t,
                regime = regime.label,
                prob   = regime.probability,
                confirmed = regime.is_confirmed,
                equity = equity,
            ))

        w.equity_curve   = pd.Series(equity_vals)
        w.trade_log      = pd.DataFrame(trades)
        w.regime_history = pd.DataFrame(regimes)
        if len(equity_vals) > 1:
            eq_s = pd.Series(equity_vals)
            w.core_metrics = self._calc.compute_core(eq_s,
                                                       w.trade_log)
        return w

    # ------------------------------------------------------------------
    # CSV output
    # ------------------------------------------------------------------

    def _save_outputs(self, equity: pd.Series, trades: pd.DataFrame,
                       regimes: pd.DataFrame, symbol: str) -> None:
        import os
        os.makedirs("logs", exist_ok=True)
        try:
            equity.to_csv(f"logs/equity_curve_{symbol}.csv",  header=["equity"])
            if len(trades)  > 0: trades.to_csv(f"logs/trade_log_{symbol}.csv",        index=False)
            if len(regimes) > 0: regimes.to_csv(f"logs/regime_history_{symbol}.csv",  index=False)
            logger.info("Backtest CSVs saved to logs/")
        except Exception as exc:
            logger.warning("Could not save CSVs: %s", exc)
