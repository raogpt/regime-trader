"""
Performance metrics calculator.

Computes all core, regime-specific, confidence-bucketed, and benchmark
metrics from an equity curve + trade log.

Used by both the walk-forward backtester and the live dashboard.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

TRADING_DAYS_PER_YEAR: int = 252


# ---------------------------------------------------------------------------
# Result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class CoreMetrics:
    total_return_pct:       float = 0.0
    cagr_pct:               float = 0.0
    sharpe:                 float = 0.0
    sortino:                float = 0.0
    calmar:                 float = 0.0
    max_drawdown_pct:       float = 0.0
    max_drawdown_days:      int   = 0
    win_rate_pct:           float = 0.0
    avg_win_pct:            float = 0.0
    avg_loss_pct:           float = 0.0
    profit_factor:          float = 0.0
    total_trades:           int   = 0
    avg_holding_days:       float = 0.0


@dataclass
class PerformanceReport:
    core:               CoreMetrics               = field(default_factory=CoreMetrics)
    regime_table:       pd.DataFrame              = field(default_factory=pd.DataFrame)
    confidence_table:   pd.DataFrame              = field(default_factory=pd.DataFrame)
    benchmark_buy_hold: CoreMetrics               = field(default_factory=CoreMetrics)
    benchmark_sma200:   CoreMetrics               = field(default_factory=CoreMetrics)
    benchmark_random:   CoreMetrics               = field(default_factory=CoreMetrics)
    equity_curve:       pd.Series                 = field(default_factory=pd.Series)
    trade_log:          pd.DataFrame              = field(default_factory=pd.DataFrame)


# ---------------------------------------------------------------------------
# PerformanceCalculator
# ---------------------------------------------------------------------------

class PerformanceCalculator:
    """
    Computes performance metrics from:
      equity_curve : pd.Series  (daily or bar equity, DatetimeIndex)
      trade_log    : pd.DataFrame with columns:
                       date, regime, confidence, allocation_before,
                       allocation_after, pnl_pct
    """

    # ------------------------------------------------------------------
    # Core metrics
    # ------------------------------------------------------------------

    def compute_core(self, equity_curve: pd.Series,
                      trade_log: pd.DataFrame) -> CoreMetrics:
        if len(equity_curve) < 2:
            return CoreMetrics()

        returns = equity_curve.pct_change().dropna()
        n_days  = len(equity_curve)

        total_ret  = self._total_return(equity_curve)
        cagr       = self._cagr(equity_curve, n_days)
        sharpe     = self._sharpe(returns)
        sortino    = self._sortino(returns)
        mdd, mdd_d = self._max_drawdown(equity_curve)
        calmar     = cagr / max(abs(mdd), 1e-6)

        wr, avg_w, avg_l, pf, n_trades, avg_hold = self._trade_stats(trade_log)

        return CoreMetrics(
            total_return_pct  = total_ret * 100,
            cagr_pct          = cagr * 100,
            sharpe            = sharpe,
            sortino           = sortino,
            calmar            = calmar,
            max_drawdown_pct  = mdd * 100,
            max_drawdown_days = mdd_d,
            win_rate_pct      = wr * 100,
            avg_win_pct       = avg_w * 100,
            avg_loss_pct      = avg_l * 100,
            profit_factor     = pf,
            total_trades      = n_trades,
            avg_holding_days  = avg_hold,
        )

    # ------------------------------------------------------------------
    # Math helpers
    # ------------------------------------------------------------------

    def _total_return(self, eq: pd.Series) -> float:
        return (eq.iloc[-1] - eq.iloc[0]) / eq.iloc[0]

    def _cagr(self, eq: pd.Series, n_days: int) -> float:
        if n_days < 2:
            return 0.0
        years = n_days / TRADING_DAYS_PER_YEAR
        return (eq.iloc[-1] / eq.iloc[0]) ** (1.0 / years) - 1.0

    def _sharpe(self, returns: pd.Series, rf: float = 0.0) -> float:
        excess = returns - rf / TRADING_DAYS_PER_YEAR
        std    = excess.std()
        return float(excess.mean() / std * np.sqrt(TRADING_DAYS_PER_YEAR)) if std > 0 else 0.0

    def _sortino(self, returns: pd.Series, rf: float = 0.0) -> float:
        excess   = returns - rf / TRADING_DAYS_PER_YEAR
        neg      = excess[excess < 0]
        down_std = neg.std() if len(neg) > 1 else 1e-9
        return float(excess.mean() / down_std * np.sqrt(TRADING_DAYS_PER_YEAR))

    def _max_drawdown(self, eq: pd.Series) -> tuple[float, int]:
        """Return (max_drawdown_fraction, duration_in_bars)."""
        peak     = eq.cummax()
        drawdown = (eq - peak) / peak
        mdd      = float(drawdown.min())

        # Duration: longest consecutive period below peak
        underwater = (drawdown < 0).astype(int)
        groups     = (underwater != underwater.shift()).cumsum()
        durations  = underwater.groupby(groups).sum()
        mdd_days   = int(durations.max()) if len(durations) > 0 else 0
        return mdd, mdd_days

    def _trade_stats(self, tlog: pd.DataFrame) -> tuple[float, float, float, float, int, float]:
        """Return (win_rate, avg_win, avg_loss, profit_factor, n_trades, avg_hold)."""
        if tlog is None or len(tlog) == 0:
            return 0.0, 0.0, 0.0, 0.0, 0, 0.0

        pnls   = tlog["pnl_pct"].dropna()
        n      = len(pnls)
        if n == 0:
            return 0.0, 0.0, 0.0, 0.0, 0, 0.0

        wins   = pnls[pnls > 0]
        losses = pnls[pnls <= 0]

        win_rate     = len(wins) / n
        avg_win      = float(wins.mean())  if len(wins)   > 0 else 0.0
        avg_loss     = float(losses.mean()) if len(losses) > 0 else 0.0
        gross_profit = wins.sum()
        gross_loss   = abs(losses.sum())
        profit_factor= gross_profit / gross_loss if gross_loss > 0 else np.inf

        avg_hold = float(tlog["holding_days"].mean()) if "holding_days" in tlog.columns else 0.0
        return win_rate, avg_win, avg_loss, profit_factor, n, avg_hold

    # ------------------------------------------------------------------
    # Regime breakdown table
    # ------------------------------------------------------------------

    def regime_table(self, equity_curve: pd.Series,
                      trade_log: pd.DataFrame) -> pd.DataFrame:
        """
        Returns a DataFrame:
        Regime | % Time In | Return Contribution | Avg Trade P&L | Win Rate | Sharpe
        """
        if trade_log is None or len(trade_log) == 0:
            return pd.DataFrame()

        rows = []
        total_bars = len(equity_curve)

        for regime, grp in trade_log.groupby("regime"):
            pnls      = grp["pnl_pct"].dropna()
            n_bars    = int(grp["bars_in_regime"].sum()) if "bars_in_regime" in grp.columns else len(grp)
            pct_time  = n_bars / max(total_bars, 1) * 100
            ret_contrib = float(pnls.sum()) * 100
            avg_pnl   = float(pnls.mean()) * 100  if len(pnls) > 0 else 0.0
            wr        = float((pnls > 0).mean()) * 100 if len(pnls) > 0 else 0.0
            # Regime-level Sharpe (annualised)
            sharpe = self._sharpe(pnls) if len(pnls) > 1 else 0.0
            rows.append(dict(
                regime=regime,
                pct_time_in=round(pct_time, 1),
                return_contribution=round(ret_contrib, 2),
                avg_trade_pnl_pct=round(avg_pnl, 2),
                win_rate_pct=round(wr, 1),
                sharpe=round(sharpe, 2),
            ))

        return pd.DataFrame(rows).set_index("regime") if rows else pd.DataFrame()

    # ------------------------------------------------------------------
    # Confidence-bucketed table
    # ------------------------------------------------------------------

    def confidence_table(self, trade_log: pd.DataFrame) -> pd.DataFrame:
        """
        Confidence | Trades | Sharpe | Win Rate | Avg P&L
        Buckets: <50%, 50-60%, 60-70%, 70%+
        """
        if trade_log is None or len(trade_log) == 0 or "confidence" not in trade_log.columns:
            return pd.DataFrame()

        buckets = [
            ("<50%",  0.00, 0.50),
            ("50-60%",0.50, 0.60),
            ("60-70%",0.60, 0.70),
            ("70%+",  0.70, 1.01),
        ]
        rows = []
        for label, lo, hi in buckets:
            mask  = (trade_log["confidence"] >= lo) & (trade_log["confidence"] < hi)
            grp   = trade_log[mask]
            pnls  = grp["pnl_pct"].dropna() if len(grp) > 0 else pd.Series(dtype=float)
            n     = len(pnls)
            wr    = float((pnls > 0).mean()) * 100 if n > 0 else 0.0
            avg_p = float(pnls.mean()) * 100        if n > 0 else 0.0
            sharpe= self._sharpe(pnls) if n > 1 else 0.0
            rows.append(dict(
                confidence_bucket=label,
                trades=n,
                sharpe=round(sharpe, 2),
                win_rate_pct=round(wr, 1),
                avg_pnl_pct=round(avg_p, 2),
            ))
        return pd.DataFrame(rows).set_index("confidence_bucket")

    # ------------------------------------------------------------------
    # Benchmarks
    # ------------------------------------------------------------------

    def benchmark_buy_hold(self, price_series: pd.Series,
                            initial_cash: float = 100_000.0) -> CoreMetrics:
        """Buy at first bar, hold to last."""
        shares = initial_cash / price_series.iloc[0]
        eq     = price_series * shares
        return self.compute_core(eq, pd.DataFrame())

    def benchmark_sma200(self, price_series: pd.Series,
                          initial_cash: float = 100_000.0) -> CoreMetrics:
        """Long when price > 200 SMA, cash otherwise."""
        sma    = price_series.rolling(200, min_periods=100).mean()
        signal = (price_series > sma).astype(float)
        ret    = price_series.pct_change().fillna(0) * signal.shift(1).fillna(0)
        eq     = initial_cash * (1 + ret).cumprod()
        tlog   = self._returns_to_tradelog(ret, signal)
        return self.compute_core(eq, tlog)

    def benchmark_random(self, price_series: pd.Series, n_seeds: int = 100,
                          initial_cash: float = 100_000.0,
                          avg_frequency: int = 21) -> tuple[CoreMetrics, float]:
        """
        Random allocation changes at same frequency as strategy.
        Returns (mean_metrics, std_sharpe).
        """
        sharpes, returns = [], []
        for seed in range(n_seeds):
            rng   = np.random.default_rng(seed)
            alloc = np.zeros(len(price_series))
            # Random rebalance every avg_frequency bars
            for t in range(0, len(price_series), avg_frequency):
                alloc[t:t + avg_frequency] = rng.uniform(0.0, 1.0)
            ret   = price_series.pct_change().fillna(0) * np.roll(alloc, 1)
            eq    = initial_cash * (1 + ret).cumprod()
            m     = self.compute_core(pd.Series(eq, index=price_series.index), pd.DataFrame())
            sharpes.append(m.sharpe)
            returns.append(m.total_return_pct)

        avg_m        = CoreMetrics()
        avg_m.sharpe = float(np.mean(sharpes))
        avg_m.total_return_pct = float(np.mean(returns))
        return avg_m, float(np.std(sharpes))

    # ------------------------------------------------------------------
    # Private helper
    # ------------------------------------------------------------------

    def _returns_to_tradelog(self, returns: pd.Series,
                              signal: pd.Series) -> pd.DataFrame:
        changes = signal.diff().fillna(0)
        trades  = []
        for idx in changes[changes != 0].index:
            trades.append(dict(
                date=idx, regime="benchmark", confidence=1.0,
                pnl_pct=float(returns.loc[idx]),
                allocation_before=0.0, allocation_after=float(signal.loc[idx]),
            ))
        return pd.DataFrame(trades)

    # ------------------------------------------------------------------
    # Full report
    # ------------------------------------------------------------------

    def full_report(self, equity_curve: pd.Series,
                     trade_log: pd.DataFrame,
                     price_series: pd.Series) -> PerformanceReport:
        return PerformanceReport(
            core             = self.compute_core(equity_curve, trade_log),
            regime_table     = self.regime_table(equity_curve, trade_log),
            confidence_table = self.confidence_table(trade_log),
            benchmark_buy_hold= self.benchmark_buy_hold(price_series),
            benchmark_sma200 = self.benchmark_sma200(price_series),
            equity_curve     = equity_curve,
            trade_log        = trade_log,
        )

    # ------------------------------------------------------------------
    # Rich terminal output
    # ------------------------------------------------------------------

    def print_report(self, report: PerformanceReport) -> None:
        c = report.core
        print("\n" + "=" * 60)
        print("  PERFORMANCE REPORT")
        print("=" * 60)
        print(f"  Total Return : {c.total_return_pct:+.1f}%")
        print(f"  CAGR         : {c.cagr_pct:+.1f}%")
        print(f"  Sharpe       : {c.sharpe:.2f}")
        print(f"  Sortino      : {c.sortino:.2f}")
        print(f"  Calmar       : {c.calmar:.2f}")
        print(f"  Max Drawdown : {c.max_drawdown_pct:.1f}%  ({c.max_drawdown_days} days)")
        print(f"  Win Rate     : {c.win_rate_pct:.1f}%")
        print(f"  Profit Factor: {c.profit_factor:.2f}")
        print(f"  Total Trades : {c.total_trades}")
        print(f"  Avg Hold     : {c.avg_holding_days:.1f} days")

        if not report.regime_table.empty:
            print("\n--- REGIME BREAKDOWN ---")
            print(report.regime_table.to_string())

        if not report.confidence_table.empty:
            print("\n--- CONFIDENCE BUCKETS ---")
            print(report.confidence_table.to_string())

        bh = report.benchmark_buy_hold
        sm = report.benchmark_sma200
        print(f"\n--- BENCHMARKS ---")
        print(f"  Buy & Hold   : {bh.total_return_pct:+.1f}%  Sharpe={bh.sharpe:.2f}")
        print(f"  SMA200 Trend : {sm.total_return_pct:+.1f}%  Sharpe={sm.sharpe:.2f}")
        print("=" * 60)
