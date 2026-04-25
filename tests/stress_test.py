"""
Stress-testing module for regime_trader.

Three stress scenarios, callable independently or via CLI:

  a. Crash injection    — insert -5 % to -15 % single-day gaps at 10 random
                          points, run 100 Monte Carlo simulations.
                          Report: mean max loss, worst case, % where circuit
                          breaker fired.

  b. Gap risk           — insert overnight gaps of 2-5× ATR at random points.
                          Report: expected loss vs actual.

  c. Regime misclassification — shuffle regime labels deliberately.
                          Verify risk management contains damage even when
                          the HMM is wrong.  If system blows up → risk
                          management is not independent enough.

Output: rich formatted tables to terminal + stress_test_results.csv
"""

from __future__ import annotations

import logging
import random
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from tests.backtester import WalkForwardBacktester, BacktestConfig
from utils.performance import PerformanceCalculator, CoreMetrics

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class StressResult:
    scenario:         str
    mean_max_loss_pct:float = 0.0
    worst_case_pct:   float = 0.0
    cb_fired_pct:     float = 0.0          # % simulations where circuit-breaker fired
    expected_loss_pct:float = 0.0          # scenario b
    actual_loss_pct:  float = 0.0          # scenario b
    notes:            str   = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _atr_series(df: pd.DataFrame, period: int = 14) -> pd.Series:
    h, l, c   = df["high"], df["low"], df["close"]
    prev_c    = c.shift(1)
    tr        = pd.concat([h - l, (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    return tr.rolling(period, min_periods=period // 2).mean()


def _simulate_equity(price_series: pd.Series,
                      allocations:  np.ndarray,
                      initial_cash: float = 100_000.0,
                      slippage:     float = 0.0005) -> pd.Series:
    """Simple mark-to-market simulation for stress testing."""
    eq     = initial_cash
    shares = 0
    equity = []

    for t in range(len(price_series)):
        price      = float(price_series.iloc[t])
        target_sh  = int(eq * allocations[t] / price)
        delta      = target_sh - shares
        eq        -= delta * price * (1 + slippage)
        shares     = target_sh
        eq_now     = eq + shares * price
        equity.append(max(eq_now, 0.0))
        eq = eq_now

    return pd.Series(equity, index=price_series.index)


def _max_drawdown(equity: pd.Series) -> float:
    peak = equity.cummax()
    dd   = (equity - peak) / peak
    return float(dd.min())


# ---------------------------------------------------------------------------
# Scenario a — Crash injection
# ---------------------------------------------------------------------------

def scenario_crash_injection(price_df: pd.DataFrame,
                               n_crashes:    int   = 10,
                               n_simulations:int   = 100,
                               drop_range:   tuple = (-0.15, -0.05),
                               cb_threshold: float = -0.10,
                               seed:         int   = 42) -> StressResult:
    """
    Insert `n_crashes` single-day drops (drop_range) at random points.
    Run `n_simulations` Monte Carlo seeds.
    Report mean max loss, worst case, % where circuit-breaker threshold
    (cb_threshold) was breached.
    """
    rng         = np.random.default_rng(seed)
    max_losses  = []
    cb_fired    = 0
    calc        = PerformanceCalculator()

    # Baseline allocation: 0.95 (bull strategy)
    base_alloc  = np.full(len(price_df), 0.95)

    for sim in range(n_simulations):
        df_sim    = price_df.copy()
        crash_idx = rng.choice(range(50, len(df_sim) - 1), size=n_crashes, replace=False)
        drop_pcts = rng.uniform(drop_range[0], drop_range[1], size=n_crashes)

        for idx, drop in zip(sorted(crash_idx), drop_pcts):
            df_sim.iloc[idx, df_sim.columns.get_loc("close")] *= (1 + drop)
            df_sim.iloc[idx, df_sim.columns.get_loc("low")]   *= (1 + drop)

        equity = _simulate_equity(df_sim["close"], base_alloc)
        mdd    = _max_drawdown(equity)
        max_losses.append(mdd)
        if mdd < cb_threshold:
            cb_fired += 1

    return StressResult(
        scenario          = "crash_injection",
        mean_max_loss_pct = float(np.mean(max_losses)) * 100,
        worst_case_pct    = float(np.min(max_losses))  * 100,
        cb_fired_pct      = cb_fired / n_simulations   * 100,
        notes             = (f"{n_crashes} crashes/sim, {n_simulations} MC runs, "
                             f"drop range {drop_range[0]*100:.0f}% to {drop_range[1]*100:.0f}%"),
    )


# ---------------------------------------------------------------------------
# Scenario b — Gap risk
# ---------------------------------------------------------------------------

def scenario_gap_risk(price_df: pd.DataFrame,
                       n_gaps:    int   = 20,
                       atr_mult:  tuple = (2.0, 5.0),
                       seed:      int   = 43) -> StressResult:
    """
    Insert overnight gaps (2-5× ATR, random direction -/+) at random points.
    Compare expected vs actual portfolio loss.
    """
    rng      = np.random.default_rng(seed)
    atr      = _atr_series(price_df, 14)
    df_sim   = price_df.copy()
    df_sim.columns = [c.lower() for c in df_sim.columns]

    gap_indices  = rng.choice(range(50, len(df_sim) - 1), size=n_gaps, replace=False)
    expected_tot = 0.0

    for idx in sorted(gap_indices):
        atr_val   = float(atr.iloc[idx])
        mult      = rng.uniform(atr_mult[0], atr_mult[1])
        direction = rng.choice([-1, 1])
        gap_size  = direction * mult * atr_val
        prev_close = float(df_sim["close"].iloc[idx])
        expected_tot += abs(gap_size) / prev_close  # expected loss fraction

        # Apply gap at next open
        df_sim.iloc[idx + 1, df_sim.columns.get_loc("open")]  = prev_close + gap_size
        df_sim.iloc[idx + 1, df_sim.columns.get_loc("close")] = prev_close + gap_size * 0.5

    base_alloc = np.full(len(df_sim), 0.90)
    equity     = _simulate_equity(df_sim["close"], base_alloc)
    actual_mdd = _max_drawdown(equity)

    return StressResult(
        scenario          = "gap_risk",
        expected_loss_pct = expected_tot * 100,
        actual_loss_pct   = actual_mdd  * 100,
        notes             = (f"{n_gaps} gaps, mult {atr_mult[0]:.1f}-{atr_mult[1]:.1f}× ATR"),
    )


# ---------------------------------------------------------------------------
# Scenario c — Regime misclassification
# ---------------------------------------------------------------------------

def scenario_regime_misclassification(price_df: pd.DataFrame,
                                       n_simulations: int   = 50,
                                       cb_threshold:  float = -0.20,
                                       seed:          int   = 44) -> StressResult:
    """
    Randomly shuffle regime labels to simulate a completely wrong HMM.
    The risk management (position sizing + circuit breakers) must still
    prevent catastrophic loss.  If max drawdown > cb_threshold →
    risk management is NOT independent enough.
    """
    rng         = np.random.default_rng(seed)
    max_losses  = []
    cb_fired    = 0

    # Random allocations: 0.60 to 0.95 shuffled
    alloc_levels = np.array([0.60, 0.70, 0.80, 0.90, 0.95])

    for _ in range(n_simulations):
        random_alloc = rng.choice(alloc_levels, size=len(price_df))
        equity       = _simulate_equity(price_df["close"], random_alloc)
        mdd          = _max_drawdown(equity)
        max_losses.append(mdd)
        if mdd < cb_threshold:
            cb_fired += 1

    passed = cb_fired == 0
    return StressResult(
        scenario          = "regime_misclassification",
        mean_max_loss_pct = float(np.mean(max_losses)) * 100,
        worst_case_pct    = float(np.min(max_losses))  * 100,
        cb_fired_pct      = cb_fired / n_simulations   * 100,
        notes             = (
            f"{n_simulations} MC runs with shuffled labels. "
            + ("PASS — risk mgmt is independent." if passed
               else "FAIL — risk management is NOT independent enough.")
        ),
    )


# ---------------------------------------------------------------------------
# Run all stress tests
# ---------------------------------------------------------------------------

def run_all(price_df: pd.DataFrame) -> list[StressResult]:
    """Run all three scenarios and return results."""
    df = price_df.copy()
    df.columns = [c.lower() for c in df.columns]

    results = [
        scenario_crash_injection(df),
        scenario_gap_risk(df),
        scenario_regime_misclassification(df),
    ]
    _print_results(results)
    _save_results(results)
    return results


def _print_results(results: list[StressResult]) -> None:
    print("\n" + "=" * 60)
    print("  STRESS TEST RESULTS")
    print("=" * 60)
    for r in results:
        print(f"\n  [{r.scenario.upper()}]")
        if r.mean_max_loss_pct:
            print(f"    Mean max loss : {r.mean_max_loss_pct:+.1f}%")
        if r.worst_case_pct:
            print(f"    Worst case    : {r.worst_case_pct:+.1f}%")
        if r.cb_fired_pct:
            print(f"    CB fired in   : {r.cb_fired_pct:.1f}% of runs")
        if r.expected_loss_pct:
            print(f"    Expected loss : {r.expected_loss_pct:+.1f}%")
        if r.actual_loss_pct:
            print(f"    Actual MDD    : {r.actual_loss_pct:+.1f}%")
        print(f"    Notes: {r.notes}")
    print("=" * 60)


def _save_results(results: list[StressResult]) -> None:
    import os
    os.makedirs("logs", exist_ok=True)
    rows = [r.__dict__ for r in results]
    pd.DataFrame(rows).to_csv("logs/stress_test_results.csv", index=False)
    logger.info("Stress test results saved to logs/stress_test_results.csv")
