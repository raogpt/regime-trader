"""
regime_trader — main loop and CLI entry point.

STARTUP (in order):
  1. Parse CLI args
  2. Setup logging
  3. Check lock file
  4. Connect to Alpaca, verify account
  5. Wait for market hours (or exit if --dry-run / market closed)
  6. Load or train HMM (retrain if model >7 days old or missing)
  7. Initialize RiskManager with live portfolio value
  8. Initialize OrderExecutor, sync positions from broker
  9. Recover state_snapshot.json if present
  10. Start WebSocket bar stream
  11. Enter main loop

MAIN LOOP (each bar close):
  1. Receive bar
  2. Compute features (rolling, no future data)
  3. Forward-algorithm HMM prediction
  4. Stability filter (3-bar persistence)
  5. Flicker rate → uncertainty mode
  6. StrategyOrchestrator → target allocation per symbol
  7. For each signal: risk gate → order execution
  8. Update trailing stops per regime
  9. Circuit-breaker check + CB close if triggered
  10. Dashboard refresh
  11. Weekly: retrain HMM

SHUTDOWN (SIGINT / SIGTERM):
  - Close WebSocket
  - Do NOT close positions (stops in place)
  - Save state_snapshot.json
  - Print session summary

CLI:
  python main.py                 Live trading (paper by default)
  python main.py --dry-run       Full pipeline, no orders submitted
  python main.py --backtest      Walk-forward backtest
  python main.py --train-only    Train HMM and exit
  python main.py --stress-test   Run stress tests
  python main.py --compare       Benchmark comparisons
  python main.py --dashboard     Show dashboard for a running instance
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import pickle
import signal
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

from config import settings
from config.credentials import get_alpaca_credentials
from data.feature_engineering import FeatureEngineer
from data.market_data import MarketDataProvider, Bar
from execution.alpaca_broker import AlpacaBroker
from execution.order_executor import OrderExecutor
from models.hmm_engine import HMMEngine, HMMEngineConfig
from models.regime_strategies import StrategyOrchestrator
from monitoring.dashboard import Dashboard, DashboardState, get_dashboard
from monitoring.logger import log_regime_event, log_trade_event
from monitoring.alerts import (
    alert_circuit_breaker, alert_regime_change, alert_hmm_retrained,
    alert_flicker_exceeded, alert_api_lost, alert_lock_file_created,
    alert_data_feed_down,
)
from risk.risk_manager import RiskManager, LOCK_FILE
from utils.alerts import AlertDispatcher
from utils.logger import setup_logging

logger = logging.getLogger(__name__)

HMM_MODEL_PATH   = "models/hmm_model.pkl"
STATE_SNAPSHOT   = "state_snapshot.json"
HMM_MAX_AGE_DAYS = 7


# ---------------------------------------------------------------------------
# Retry decorator (Alpaca API calls)
# ---------------------------------------------------------------------------

def _with_retry(fn, retries: int = 3, backoff: float = 2.0):
    """Call fn with exponential backoff on failure."""
    for attempt in range(retries):
        try:
            return fn()
        except Exception as exc:
            if attempt == retries - 1:
                raise
            wait = backoff ** attempt
            logger.warning("Retry %d/%d in %.0fs: %s", attempt + 1, retries, wait, exc)
            time.sleep(wait)


# ---------------------------------------------------------------------------
# Startup helpers
# ---------------------------------------------------------------------------

def check_lock_file() -> None:
    """Abort with a clear message if the peak-drawdown lock file exists."""
    if os.path.exists(LOCK_FILE):
        content = Path(LOCK_FILE).read_text()
        logger.critical("BOT LOCKED — %s exists. Delete it to resume.\n%s",
                         LOCK_FILE, content)
        sys.exit(1)


def confirm_live_trading() -> None:
    """Require explicit confirmation before live (non-paper) trading."""
    answer = input(
        "\n⚠️  LIVE TRADING MODE.\n"
        "Type 'YES I UNDERSTAND THE RISKS' to confirm: "
    ).strip()
    if answer != "YES I UNDERSTAND THE RISKS":
        print("Confirmation not received. Exiting.")
        sys.exit(0)


def connect_broker() -> AlpacaBroker:
    """Create, connect, and return an AlpacaBroker instance."""
    broker = AlpacaBroker()
    _with_retry(broker.connect)
    if not settings.PAPER_TRADING:
        confirm_live_trading()
    return broker


def build_data_provider(broker: AlpacaBroker) -> MarketDataProvider:
    creds = get_alpaca_credentials()
    dp    = MarketDataProvider(
        api_key    = creds["api_key"],
        secret_key = creds["secret_key"],
        api_client = broker._client,
    )
    dp.connect()
    return dp


def wait_for_market_open(dp: MarketDataProvider, dry_run: bool = False) -> None:
    """Block until NYSE opens. In dry-run mode skip the wait."""
    if dry_run:
        return
    secs = dp.seconds_until_market_open()
    if secs > 0:
        opens_at = datetime.now(timezone.utc) + timedelta(seconds=secs)
        logger.info("Market closed. Opens in %dm at %s UTC",
                     secs // 60, opens_at.strftime("%H:%M"))
        time.sleep(secs)


def load_or_train_hmm(dp: MarketDataProvider,
                       feat_eng: FeatureEngineer,
                       force_retrain: bool = False) -> tuple[HMMEngine, list]:
    """
    Load HMM from disk if fresh (<7 days), otherwise fetch history and retrain.
    Returns (engine, regime_infos).
    """
    model_path = Path(HMM_MODEL_PATH)
    if not force_retrain and model_path.exists():
        mtime    = datetime.fromtimestamp(model_path.stat().st_mtime, tz=timezone.utc)
        age_days = (datetime.now(timezone.utc) - mtime).days
        if age_days < HMM_MAX_AGE_DAYS:
            logger.info("Loading HMM from %s (age=%dd)", HMM_MODEL_PATH, age_days)
            try:
                hmm = HMMEngine.load(HMM_MODEL_PATH)
                regime_infos = [hmm.get_regime_info(lbl) for lbl in hmm.regime_labels]
                return hmm, regime_infos
            except Exception as exc:
                logger.warning("HMM load failed (%s) — retraining", exc)

    return _retrain_hmm(dp, feat_eng)


def _retrain_hmm(dp: MarketDataProvider,
                  feat_eng: FeatureEngineer) -> tuple[HMMEngine, list]:
    logger.info("Training HMM on %d days of daily data …", settings.HMM_TRAINING_DAYS)
    df = _with_retry(lambda: dp.get_daily_bars(settings.PRIMARY_TICKER,
                                                settings.HMM_TRAINING_DAYS))
    feats = feat_eng.build_feature_matrix(df)
    cfg   = HMMEngineConfig(n_states_range=settings.HMM_N_STATES_RANGE, n_init=10)
    hmm   = HMMEngine(config=cfg)
    hmm.fit(feats)

    Path(HMM_MODEL_PATH).parent.mkdir(parents=True, exist_ok=True)
    hmm.save(HMM_MODEL_PATH)

    regime_infos = [hmm.get_regime_info(lbl) for lbl in hmm.regime_labels]
    bic = getattr(hmm, "_best_bic", 0.0)
    alert_hmm_retrained(n_states=hmm.n_states, bic=bic)
    logger.info("HMM trained | states=%d", hmm.n_states)
    return hmm, regime_infos


def recover_state(executor: OrderExecutor, risk: RiskManager) -> None:
    """Restore last known session state from state_snapshot.json if present."""
    if not Path(STATE_SNAPSHOT).exists():
        return
    try:
        snap = json.loads(Path(STATE_SNAPSHOT).read_text())
        logger.info("Recovering from %s (saved %s)",
                     STATE_SNAPSHOT, snap.get("saved_at", "?"))
        # Positions are reconciled via sync_positions() — we just log recovery
    except Exception as exc:
        logger.warning("Could not load state snapshot: %s", exc)


def save_state(executor: OrderExecutor, risk: RiskManager,
                regime_label: str) -> None:
    """Persist minimal session state for crash recovery."""
    state = {
        "saved_at":     datetime.now(timezone.utc).isoformat(),
        "portfolio":    risk._portfolio,
        "regime":       regime_label,
        "daily_pnl":    risk.daily_pnl_pct(),
        "peak_dd":      risk.peak_dd_pct(),
        "open_positions": {
            t: {"qty": p.qty, "entry": p.entry_price, "stop": p.stop_price}
            for t, p in executor.get_open_positions().items()
        },
    }
    Path(STATE_SNAPSHOT).write_text(json.dumps(state, indent=2))
    logger.debug("State snapshot saved")


# ---------------------------------------------------------------------------
# Per-bar pipeline
# ---------------------------------------------------------------------------

class BotState:
    """Mutable shared state passed into the bar callback."""
    def __init__(self) -> None:
        self.hmm:          Optional[HMMEngine]         = None
        self.feat_eng:     Optional[FeatureEngineer]   = None
        self.orchestrator: Optional[StrategyOrchestrator] = None
        self.risk:         Optional[RiskManager]       = None
        self.executor:     Optional[OrderExecutor]     = None
        self.dp:           Optional[MarketDataProvider]= None
        self.dashboard:    Optional[Dashboard]         = None
        self.accumulated:  pd.DataFrame = pd.DataFrame()
        self.prev_regime:  str          = ""
        self.bars_since_retrain: int    = 0
        self.dry_run:      bool         = False
        self.hmm_trained_at: Optional[datetime] = None


def _process_bar(bar: Bar, state: BotState) -> None:
    """Full pipeline for one completed bar."""
    # 1. Append bar to rolling window
    new_row = pd.DataFrame([{
        "open": bar.open, "high": bar.high, "low": bar.low,
        "close": bar.close, "volume": bar.volume,
    }], index=[bar.timestamp])

    state.accumulated = pd.concat([state.accumulated, new_row])
    if len(state.accumulated) > 2000:
        state.accumulated = state.accumulated.iloc[-2000:]

    if len(state.accumulated) < 60:
        return   # not enough data yet

    # 2. Compute features (rolling, no future data)
    feats = state.feat_eng.build_feature_matrix(state.accumulated)
    if len(feats) < 10:
        return

    # 3. Forward HMM prediction
    try:
        regime = state.hmm.predict_regime(feats)
    except Exception as exc:
        logger.warning("HMM predict failed (%s) — holding %s", exc, state.prev_regime)
        return

    # 4. Flicker check
    is_flickering = state.hmm.is_flickering()
    if is_flickering:
        alert_flicker_exceeded(
            rate=state.hmm._flicker_count if hasattr(state.hmm, "_flicker_count") else 0,
            window=settings.HMM_INSTABILITY_WINDOW,
        )

    # 5. Regime change alert
    if regime.label != state.prev_regime and regime.is_confirmed:
        alert_regime_change(state.prev_regime, regime.label, regime.probability)
        state.prev_regime = regime.label

    # 6. Update risk manager with latest equity
    portfolio_value = _with_retry(lambda: state.executor._broker.get_portfolio_value())
    cb_status = state.risk.update_portfolio_value(portfolio_value, regime.label)

    # 7. Circuit-breaker close
    if not cb_status.trading_allowed:
        if cb_status.peak_locked:
            alert_lock_file_created(f"Peak DD {state.risk.peak_dd_pct():.1%}")
        else:
            alert_circuit_breaker("close_all", state.risk.daily_pnl_pct())
        if not state.dry_run:
            closed = state.executor.close_all_positions(reason="circuit_breaker")
            logger.warning("CB triggered — closed %d positions", len(closed))

    # 8. Generate signals
    bars_dict = {settings.PRIMARY_TICKER: state.accumulated.reset_index(drop=True)}
    signals   = state.orchestrator.generate_signals(
        symbols     = settings.TICKERS,
        bars        = bars_dict,
        regime_state= regime,
        is_flickering= is_flickering,
    )

    # 9. Route signals through risk gate → orders
    for sig in signals:
        size = state.risk.calculate_position_size(
            ticker         = sig.symbol,
            entry          = sig.entry_price,
            stop           = sig.stop_loss,
            regime_max_pct = sig.position_size_pct,
        )
        if size.shares == 0:
            logger.debug("Signal skipped (0 shares after sizing): %s", sig.symbol)
            continue

        if not state.dry_run:
            result = state.executor.buy(sig.symbol, size, regime.label)
            if result and result.status not in ("rejected",):
                log_trade_event(
                    order_id = result.order_id,
                    ticker   = result.ticker,
                    side     = result.side,
                    qty      = result.qty,
                    price    = result.filled_price,
                    status   = result.status,
                    regime   = regime.label,
                )
        else:
            logger.info("DRY-RUN: would buy %d %s @ %.2f (stop=%.2f)",
                         size.shares, sig.symbol, sig.entry_price, sig.stop_loss)

    # 10. Check stops
    prices = {bar.ticker: bar.close}
    if not state.dry_run:
        state.executor.check_stops(prices)

    # 11. Log regime event
    log_regime_event(
        regime       = regime.label,
        probability  = regime.probability,
        equity       = portfolio_value,
        positions    = {t: p.qty for t, p in state.executor.get_open_positions().items()},
        daily_pnl    = state.risk.daily_pnl_pct(),
        flicker_rate = state.hmm._flicker_count / max(settings.HMM_INSTABILITY_WINDOW, 1)
                        if hasattr(state.hmm, "_flicker_count") else 0.0,
        is_confirmed = regime.is_confirmed,
    )

    # 12. Dashboard update
    if state.dashboard:
        ds = DashboardState(
            regime_label   = regime.label,
            regime_prob    = regime.probability,
            stability_bars = regime.consecutive_bars,
            equity         = portfolio_value,
            equity_start   = state.risk._day_start,
            daily_dd_pct   = state.risk.daily_pnl_pct() * -100,
            peak_dd_pct    = state.risk.peak_dd_pct() * 100,
            cb_daily_half  = cb_status.daily_half_active,
            cb_daily_halt  = cb_status.daily_halt_active,
            cb_peak_locked = cb_status.peak_locked,
            data_ok        = True,
            api_ok         = True,
            paper_mode     = settings.PAPER_TRADING,
            hmm_trained_ago= _ago(state.hmm_trained_at),
        )
        for t, p in state.executor.get_open_positions().items():
            ds.positions[t] = {
                "side": "LONG", "price": p.current_price,
                "pnl_pct": p.pnl_pct, "stop": p.stop_price,
                "age_h": (datetime.now(timezone.utc) - p.opened_at).seconds / 3600,
            }
        state.dashboard.update(ds)

    # 13. Weekly retrain (every ~5 trading days × 78 bars/day)
    state.bars_since_retrain += 1
    if state.bars_since_retrain >= 390:
        logger.info("Weekly retrain triggered")
        state.hmm, _ = _retrain_hmm(state.dp, state.feat_eng)
        state.bars_since_retrain = 0
        state.hmm_trained_at = datetime.now(timezone.utc)


def _ago(dt: Optional[datetime]) -> str:
    if dt is None:
        return "—"
    delta = datetime.now(timezone.utc) - dt
    if delta.days > 0:
        return f"{delta.days}d ago"
    return f"{delta.seconds // 3600}h ago"


# ---------------------------------------------------------------------------
# Session summary
# ---------------------------------------------------------------------------

def _print_summary(risk: RiskManager, executor: OrderExecutor) -> None:
    history = executor.get_trade_history()
    print("\n" + "=" * 50)
    print("  SESSION SUMMARY")
    print(f"  Total trades  : {len(history)}")
    print(f"  Daily P&L     : {risk.daily_pnl_pct():+.2%}")
    print(f"  Peak drawdown : {risk.peak_dd_pct():.2%}")
    print(f"  Open positions: {len(executor.get_open_positions())}")
    print("=" * 50)


# ---------------------------------------------------------------------------
# CLI sub-commands
# ---------------------------------------------------------------------------

def cmd_backtest(args) -> None:
    from tests.backtester import WalkForwardBacktester, BacktestConfig
    from utils.performance import PerformanceCalculator
    creds = get_alpaca_credentials()
    dp    = MarketDataProvider(api_key=creds["api_key"],
                                secret_key=creds["secret_key"])
    dp.connect()
    symbol = (args.symbols or [settings.PRIMARY_TICKER])[0]
    logger.info("Fetching %s bars for backtest …", symbol)
    df = dp.get_daily_bars(symbol, 252 * 6)   # 6 years
    bt = WalkForwardBacktester(BacktestConfig())
    report = bt.run(df, symbol=symbol)
    _print_backtest_report(report, symbol)
    if getattr(args, "compare", False):
        _print_benchmarks(report)


def _print_backtest_report(report, symbol: str) -> None:
    m = report.core
    print(f"\n{'='*55}")
    print(f"  BACKTEST RESULTS — {symbol}")
    print(f"  Total return  : {m.total_return_pct:+.1f}%")
    print(f"  CAGR          : {m.cagr_pct:+.1f}%")
    print(f"  Sharpe        : {m.sharpe:.2f}")
    print(f"  Sortino       : {m.sortino:.2f}")
    print(f"  Max drawdown  : {m.max_drawdown_pct:.1f}%")
    print(f"  Win rate      : {m.win_rate_pct:.1f}%")
    print(f"  Trades        : {m.total_trades}")
    print(f"{'='*55}")


def _print_benchmarks(report) -> None:
    bh = getattr(report, "benchmark_buy_hold", None)
    sm = getattr(report, "benchmark_sma200",   None)
    rn = getattr(report, "benchmark_random",   None)
    print("\n  BENCHMARKS")
    if bh: print(f"  Buy & Hold    : {bh.total_return_pct:+.1f}% | Sharpe {bh.sharpe:.2f}")
    if sm: print(f"  SMA-200       : {sm.total_return_pct:+.1f}% | Sharpe {sm.sharpe:.2f}")
    if rn: print(f"  Random (mean) : {rn.total_return_pct:+.1f}% | Sharpe {rn.sharpe:.2f}")


def cmd_train_only(args) -> None:
    creds = get_alpaca_credentials()
    dp    = MarketDataProvider(api_key=creds["api_key"],
                                secret_key=creds["secret_key"])
    dp.connect()
    feat_eng = FeatureEngineer()
    _retrain_hmm(dp, feat_eng)
    print("HMM trained and saved to", HMM_MODEL_PATH)


def cmd_stress_test(args) -> None:
    from tests.stress_test import run_all
    creds = get_alpaca_credentials()
    dp    = MarketDataProvider(api_key=creds["api_key"],
                                secret_key=creds["secret_key"])
    dp.connect()
    df = dp.get_daily_bars(settings.PRIMARY_TICKER, 252 * 6)
    run_all(df)


def cmd_dashboard(args) -> None:
    """Attach to a running instance's last state snapshot."""
    if not Path(STATE_SNAPSHOT).exists():
        print(f"No {STATE_SNAPSHOT} found. Is the bot running?")
        return
    snap = json.loads(Path(STATE_SNAPSHOT).read_text())
    print(json.dumps(snap, indent=2))


# ---------------------------------------------------------------------------
# Live trading entry point
# ---------------------------------------------------------------------------

def cmd_live(args) -> None:
    dry_run = getattr(args, "dry_run", False)

    check_lock_file()
    broker = connect_broker()
    dp     = build_data_provider(broker)

    wait_for_market_open(dp, dry_run=dry_run)

    feat_eng = FeatureEngineer()
    hmm, regime_infos = load_or_train_hmm(dp, feat_eng,
                                            force_retrain=False)
    hmm_trained_at = datetime.now(timezone.utc)

    account = _with_retry(broker.get_account)
    risk    = RiskManager(portfolio_value=account.portfolio_value)
    risk.update_portfolio_value(account.portfolio_value)

    executor = OrderExecutor(broker=broker, risk_manager=risk)
    _with_retry(executor.sync_positions)

    recover_state(executor, risk)

    orchestrator = StrategyOrchestrator(
        regime_infos        = regime_infos,
        min_confidence      = settings.BACKTEST.get("min_confidence", 0.55),
        rebalance_threshold = settings.BACKTEST.get("rebalance_threshold", 0.10),
    )

    dash = get_dashboard(refresh_seconds=settings.DASHBOARD_REFRESH_SECONDS)
    dash.start()

    bot = BotState()
    bot.hmm            = hmm
    bot.feat_eng       = feat_eng
    bot.orchestrator   = orchestrator
    bot.risk           = risk
    bot.executor       = executor
    bot.dp             = dp
    bot.dashboard      = dash
    bot.dry_run        = dry_run
    bot.hmm_trained_at = hmm_trained_at

    # Pre-load historical bars into the rolling window
    logger.info("Loading historical bars into rolling window …")
    hist = _with_retry(lambda: dp.get_historical_bars(
        settings.PRIMARY_TICKER,
        settings.BAR_TIMEFRAME,
        start = datetime.now(timezone.utc) - timedelta(days=30),
    ))
    bot.accumulated = hist.rename(columns={"open": "open", "high": "high",
                                            "low": "low", "close": "close",
                                            "volume": "volume"})

    # Graceful shutdown
    def _shutdown(signum, frame):
        logger.info("Shutdown signal received")
        dp.unsubscribe_bars()
        save_state(executor, risk, bot.prev_regime)
        _print_summary(risk, executor)
        dash.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT,  _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    # Subscribe to live bars
    def on_bar(bar: Bar) -> None:
        try:
            _process_bar(bar, bot)
        except Exception as exc:
            logger.error("Unhandled error in bar callback: %s", exc, exc_info=True)
            save_state(executor, risk, bot.prev_regime)

    dp.subscribe_bars(settings.TICKERS, callback=on_bar,
                        timeframe=settings.BAR_TIMEFRAME)

    mode = "DRY-RUN" if dry_run else ("PAPER" if settings.PAPER_TRADING else "LIVE")
    logger.info("System online | mode=%s | tickers=%s", mode, settings.TICKERS)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        _shutdown(None, None)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="regime_trader — HMM-based trading bot")
    parser.add_argument("--dry-run",     action="store_true",
                        help="Full pipeline, no orders submitted")
    parser.add_argument("--backtest",    action="store_true",
                        help="Walk-forward backtest")
    parser.add_argument("--train-only",  action="store_true",
                        help="Train HMM and exit")
    parser.add_argument("--stress-test", action="store_true",
                        help="Run stress test scenarios")
    parser.add_argument("--compare",     action="store_true",
                        help="Show benchmark comparisons (use with --backtest)")
    parser.add_argument("--dashboard",   action="store_true",
                        help="Show last state snapshot")
    parser.add_argument("--symbols",     nargs="+", default=None,
                        help="Override tickers (e.g. --symbols SPY QQQ)")

    args = parser.parse_args()

    setup_logging()

    if args.backtest:
        cmd_backtest(args)
    elif args.train_only:
        cmd_train_only(args)
    elif args.stress_test:
        cmd_stress_test(args)
    elif args.dashboard:
        cmd_dashboard(args)
    else:
        cmd_live(args)


if __name__ == "__main__":
    main()
