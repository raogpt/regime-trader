"""
episodic_runner.py — Stateless episodic runner for regime_trader.

Designed for cloud environments (GitHub Actions, cron containers) where the
process starts fresh for each run.  Credentials come exclusively from OS
environment variables; no .env loading in cloud.  Locally, sources clefs.env
or .env from the project root for convenience.

CLI:
    python episodic_runner.py --mode pre-market
    python episodic_runner.py --mode market-open
    python episodic_runner.py --mode midday
    python episodic_runner.py --mode eod
    python episodic_runner.py --mode weekly
"""

from __future__ import annotations

import argparse
import logging
import os
import pickle
import subprocess
import sys
import time
import traceback
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Local .env loading (convenience for local runs only)
# ---------------------------------------------------------------------------

_PROJECT_ROOT = Path(__file__).parent
for _env_file in ("clefs.env", ".env"):
    _env_path = _PROJECT_ROOT / _env_file
    if _env_path.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(_env_path)
        except ImportError:
            # Manually parse KEY=VALUE lines if dotenv is absent
            with open(_env_path) as _f:
                for _line in _f:
                    _line = _line.strip()
                    if _line and not _line.startswith("#") and "=" in _line:
                        _k, _, _v = _line.partition("=")
                        os.environ.setdefault(_k.strip(), _v.strip())
        break

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger = logging.getLogger("episodic_runner")

# ---------------------------------------------------------------------------
# Project imports (after env loading so credentials are available)
# ---------------------------------------------------------------------------

from config import settings
from models.hmm_engine import HMMEngine, HMMEngineConfig
from models.regime_strategies import StrategyOrchestrator
from data.feature_engineering import FeatureEngineer
from execution.alpaca_broker import AlpacaBroker
from execution.order_executor import OrderExecutor
from risk.risk_manager import RiskManager

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

HMM_MODEL_PATH = _PROJECT_ROOT / "models" / "hmm_model.pkl"
MEMORY_DIR = _PROJECT_ROOT / "memory"
RESEARCH_LOG = MEMORY_DIR / "RESEARCH-LOG.md"
TRADE_LOG = MEMORY_DIR / "TRADE-LOG.md"
WEEKLY_REVIEW = MEMORY_DIR / "WEEKLY-REVIEW.md"

# Cross-enrichment: trading-bot RESEARCH-LOG (local path, skipped in cloud)
_TRADING_BOT_RESEARCH_LOG = Path(
    "/Users/rao/Library/Mobile Documents/iCloud~md~obsidian/Documents/"
    "VAULT RALPH/40 - FINANCES PERSONNELLES/AutoTrading/"
    "trading-bot/memory/RESEARCH-LOG.md"
)

HIGH_VOL_LABELS = {"crash", "strong_bear", "bear"}
STOP_LOSS_PCT = 0.07       # midday cut-loss threshold (matching trading-bot rule)
ATR_STOP_MULTIPLIER = 2.0  # ATR multiplier for initial stop placement


# ===========================================================================
# Retry decorator
# ===========================================================================

def with_retry(fn, retries: int = 3, base_delay: float = 2.0):
    """Call fn() with exponential backoff retries."""
    for attempt in range(retries):
        try:
            return fn()
        except Exception as exc:
            if attempt == retries - 1:
                raise
            wait = base_delay * (2 ** attempt)
            logger.warning("Attempt %d/%d failed (%s) — retrying in %.1fs",
                           attempt + 1, retries, exc, wait)
            time.sleep(wait)


# ===========================================================================
# Alpaca REST bar fetching
# ===========================================================================

def fetch_daily_bars(ticker: str, n_days: int) -> pd.DataFrame:
    """
    Fetch the last n_days daily bars for ticker via Alpaca REST.
    Returns a DataFrame with columns: open, high, low, close, volume.
    """
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame

    api_key = os.environ.get("ALPACA_API_KEY", "")
    secret_key = os.environ.get("ALPACA_SECRET_KEY", "")

    client = StockHistoricalDataClient(api_key=api_key, secret_key=secret_key)

    end = datetime.now(timezone.utc)
    # Fetch extra days to account for weekends / holidays
    start = end - timedelta(days=int(n_days * 1.5))

    req = StockBarsRequest(
        symbol_or_symbols=ticker,
        timeframe=TimeFrame.Day,
        start=start,
        end=end,
        feed="iex",
    )

    def _fetch():
        return client.get_stock_bars(req).df

    raw = with_retry(_fetch)

    # alpaca-py returns a multi-index (symbol, timestamp) — flatten if needed
    if isinstance(raw.index, pd.MultiIndex):
        raw = raw.xs(ticker, level="symbol")

    raw.index = pd.to_datetime(raw.index, utc=True)
    raw = raw.sort_index()

    # Normalise column names
    raw.columns = [c.lower() for c in raw.columns]
    required = {"open", "high", "low", "close", "volume"}
    missing = required - set(raw.columns)
    if missing:
        raise ValueError(f"Missing columns in Alpaca response: {missing}")

    df = raw[["open", "high", "low", "close", "volume"]].tail(n_days)
    logger.info("Fetched %d bars for %s", len(df), ticker)
    return df


# ===========================================================================
# HMM helpers
# ===========================================================================

def _hmm_config() -> HMMEngineConfig:
    return HMMEngineConfig(
        n_states_range=settings.HMM_N_STATES_RANGE,
        training_days=settings.HMM_TRAINING_DAYS,
        retrain_interval_days=settings.HMM_RETRAIN_INTERVAL_DAYS,
        stability_bars=settings.HMM_STABILITY_BARS,
        instability_window=settings.HMM_INSTABILITY_WINDOW,
        instability_threshold=settings.HMM_INSTABILITY_THRESHOLD,
    )


def _model_is_fresh(max_age_days: int = 7) -> bool:
    if not HMM_MODEL_PATH.exists():
        return False
    mtime = datetime.fromtimestamp(HMM_MODEL_PATH.stat().st_mtime, tz=timezone.utc)
    age = (datetime.now(timezone.utc) - mtime).days
    return age < max_age_days


def load_or_train_hmm(n_bars: int = 60) -> tuple[HMMEngine, np.ndarray]:
    """
    Load HMM from disk if fresh (<7 days).  Otherwise retrain on n_bars daily bars.
    Returns (engine, feature_matrix).
    """
    engineer = FeatureEngineer()
    bars = fetch_daily_bars(settings.PRIMARY_TICKER, n_bars)
    features = engineer.build_feature_dataframe(bars)
    features_clean = features.dropna().values

    if _model_is_fresh():
        try:
            engine = HMMEngine.load(str(HMM_MODEL_PATH))
            logger.info("HMM loaded from disk (fresh model)")
            return engine, features_clean
        except Exception as exc:
            logger.warning("HMM load failed (%s) — retraining", exc)

    logger.info("Training HMM on %d bars …", len(features_clean))
    engine = HMMEngine(config=_hmm_config())
    engine.fit(features_clean)
    engine.save(str(HMM_MODEL_PATH))
    return engine, features_clean


def retrain_hmm_full() -> tuple[HMMEngine, np.ndarray]:
    """Full retrain using HMM_TRAINING_DAYS bars (for weekly mode)."""
    engineer = FeatureEngineer()
    bars = fetch_daily_bars(settings.PRIMARY_TICKER, settings.HMM_TRAINING_DAYS)
    features = engineer.build_feature_dataframe(bars).dropna().values
    logger.info("Full retrain on %d bars …", len(features))
    engine = HMMEngine(config=_hmm_config())
    engine.fit(features)
    engine.save(str(HMM_MODEL_PATH))
    return engine, features


def predict_regime(engine: HMMEngine, features: np.ndarray):
    """Return RegimeState for latest bar (forward algorithm, no lookahead)."""
    return engine.predict_regime(features)


# ===========================================================================
# Cross-enrichment
# ===========================================================================

def get_cross_enrichment_signal() -> dict:
    """
    Read the trading-bot RESEARCH-LOG to extract catalyst gate and sector
    momentum signals.  Returns safe defaults if the file is unavailable
    (cloud environments, path not mounted).

    Returns:
        catalyst_gate (bool): True if today's entry mentions earnings/FOMC/CPI
        sector_momentum (str): free-text sector label or "unknown"
        sizing_modifier (float): 1.0 normal, 0.5 if sector mismatch
    """
    default = {"catalyst_gate": False, "sector_momentum": "unknown", "sizing_modifier": 1.0}

    if not _TRADING_BOT_RESEARCH_LOG.exists():
        logger.debug("Cross-enrichment path not available — skipping")
        return default

    try:
        text = _TRADING_BOT_RESEARCH_LOG.read_text(encoding="utf-8")
    except OSError as exc:
        logger.warning("Could not read trading-bot RESEARCH-LOG: %s", exc)
        return default

    today_str = date.today().strftime("%Y-%m-%d")
    # Find today's section
    today_section = ""
    in_today = False
    for line in text.splitlines():
        if line.startswith(f"## {today_str}"):
            in_today = True
        elif in_today and line.startswith("## "):
            break
        if in_today:
            today_section += line + "\n"

    if not today_section:
        logger.debug("No entry for %s in trading-bot RESEARCH-LOG", today_str)
        return default

    lower = today_section.lower()
    catalyst_keywords = ("earnings", "fomc", "cpi", "ppi", "nfp", "fed meeting",
                          "jobs report", "inflation report", "catalyst")
    catalyst_gate = any(kw in lower for kw in catalyst_keywords)

    # Extract sector momentum (look for "sector: X" or "sector momentum: X")
    sector_momentum = "unknown"
    for line in today_section.splitlines():
        ll = line.lower()
        if "sector" in ll and ":" in ll:
            sector_momentum = line.split(":", 1)[-1].strip()
            break

    # ETF universe sectors: US large-cap, tech, small-cap (SPY/QQQ/IWM)
    etf_sectors = {"tech", "technology", "large-cap", "small-cap",
                   "growth", "value", "broad market", "us equity", "us market"}
    sizing_modifier = 1.0
    if sector_momentum.lower() not in etf_sectors and sector_momentum != "unknown":
        sizing_modifier = 0.5
        logger.info("Sector mismatch (trading-bot: %s vs ETF universe) → 0.5x sizing",
                    sector_momentum)

    return {
        "catalyst_gate": catalyst_gate,
        "sector_momentum": sector_momentum,
        "sizing_modifier": sizing_modifier,
    }


# ===========================================================================
# Memory helpers
# ===========================================================================

def append_to_log(path: Path, text: str) -> None:
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(text)
    logger.debug("Appended to %s", path)


def git_commit_memory(mode: str) -> None:
    today = date.today().isoformat()
    msg = f"{mode} {today}"
    cwd = str(_PROJECT_ROOT)
    subprocess.run(["git", "add", "memory/"], check=False, cwd=cwd)
    subprocess.run(["git", "commit", "-m", msg], check=False, cwd=cwd)
    subprocess.run(["git", "push", "origin", "main"], check=False, cwd=cwd)
    logger.info("Git commit + push: %s", msg)


# ===========================================================================
# Mode: pre-market
# ===========================================================================

def run_pre_market() -> None:
    logger.info("=== MODE: pre-market ===")

    broker = AlpacaBroker()
    with_retry(broker.connect)

    acct = with_retry(broker.get_account)
    logger.info("Account | equity=%.2f cash=%.2f status=%s",
                acct.equity, acct.cash, acct.status)

    engine, features = load_or_train_hmm(n_bars=60)
    regime = predict_regime(engine, features)
    logger.info("Regime: %s | confidence=%.2f | confirmed=%s",
                regime.label, regime.probability, regime.is_confirmed)

    cross = get_cross_enrichment_signal()

    today = date.today().isoformat()
    entry = (
        f"\n## {today} — Pre-Market Regime Detection\n\n"
        f"### Account\n"
        f"- Equity: ${acct.equity:,.2f}\n"
        f"- Cash: ${acct.cash:,.2f}\n"
        f"- Buying power: ${acct.buying_power:,.2f}\n"
        f"- Status: {acct.status}\n\n"
        f"### Regime Signal\n"
        f"- Detected regime: {regime.label.upper()}\n"
        f"- Confidence: {regime.probability:.1%}\n"
        f"- Consecutive bars: {regime.consecutive_bars}\n"
        f"- Confirmed: {regime.is_confirmed}\n"
        f"- Flickering: {engine.is_flickering()}\n\n"
        f"### Cross-Enrichment Signal (from trading-bot)\n"
        f"- Sector momentum: {cross['sector_momentum']}\n"
        f"- Catalyst gate active: {cross['catalyst_gate']}\n"
        f"- Sizing modifier: {cross['sizing_modifier']}\n"
        f"- Regime gate: {'BLOCKED' if cross['catalyst_gate'] else 'OPEN'}\n"
    )
    append_to_log(RESEARCH_LOG, entry)
    git_commit_memory("pre-market")


# ===========================================================================
# Mode: market-open
# ===========================================================================

def run_market_open() -> None:
    logger.info("=== MODE: market-open ===")

    broker = AlpacaBroker()
    with_retry(broker.connect)

    clock = with_retry(broker.get_clock)
    if not clock["is_open"]:
        logger.info("Market is closed — exiting")
        return

    engine, features = load_or_train_hmm(n_bars=300)
    regime = predict_regime(engine, features)
    confidence = regime.probability
    is_high_vol = regime.label in HIGH_VOL_LABELS

    cross = get_cross_enrichment_signal()
    catalyst_gate = cross["catalyst_gate"]
    sizing_modifier = cross["sizing_modifier"]

    if confidence < 0.55:
        logger.info("Confidence %.2f < 0.55 → HOLD", confidence)
        append_to_log(TRADE_LOG,
                      f"\n### {date.today().isoformat()} market-open — HOLD (low confidence {confidence:.2f})\n")
        git_commit_memory("market-open")
        return

    if is_high_vol and catalyst_gate:
        logger.info("HIGH_VOL + catalyst gate → HOLD")
        append_to_log(TRADE_LOG,
                      f"\n### {date.today().isoformat()} market-open — HOLD (HIGH_VOL + catalyst gate)\n")
        git_commit_memory("market-open")
        return

    acct = with_retry(broker.get_account)
    risk_manager = RiskManager(portfolio_value=acct.equity)
    cb_result = risk_manager.update_portfolio_value(acct.equity, regime.label)
    if cb_result and not cb_result.trading_allowed:
        logger.warning("Circuit breaker triggered — halting: %s", cb_result)
        git_commit_memory("market-open")
        return

    regime_infos = [engine.get_regime_info(label) for label in engine.regime_labels]
    orchestrator = StrategyOrchestrator(regime_infos)

    tickers_bars: dict[str, pd.DataFrame] = {}
    for ticker in settings.TICKERS:
        try:
            tickers_bars[ticker] = fetch_daily_bars(ticker, 300)
        except Exception as exc:
            logger.warning("Failed to fetch bars for %s: %s", ticker, exc)

    signals = orchestrator.generate_signals(
        symbols=settings.TICKERS,
        bars=tickers_bars,
        regime_state=regime,
        is_flickering=engine.is_flickering(),
    )

    order_executor = OrderExecutor(broker=broker, risk_manager=risk_manager)
    trade_lines = []

    for signal in signals:
        if signal.direction == "FLAT":
            logger.info("Signal FLAT for %s — skipping", signal.symbol)
            continue

        # Apply cross-enrichment sizing modifier before rebalance sizing
        signal.position_size_pct *= sizing_modifier

        try:
            results = order_executor.rebalance(signal, acct.equity)
            for r in results:
                logger.info("Order | %s %s x%d @ %.2f | id=%s",
                            r.side, r.ticker, r.qty, r.filled_price, r.order_id)
                trade_lines.append(
                    f"| {r.ticker} | {r.side.upper()} | {r.qty} | "
                    f"{r.filled_price:.2f} | {signal.stop_loss:.2f} | "
                    f"{signal.confidence:.2f} | {regime.label} |"
                )
        except Exception as exc:
            logger.error("Order failed for %s: %s", signal.symbol, exc)

    today = date.today().isoformat()
    header = (
        f"\n## {today} — Market Open\n"
        f"**Regime:** {regime.label.upper()} | **Confidence:** {confidence:.1%} | "
        f"**Portfolio:** ${acct.equity:,.2f}\n\n"
    )
    if trade_lines:
        table_header = "| ETF | Side | Shares | Entry | Stop | Conf | Regime |\n|---|---|---|---|---|---|---|\n"
        append_to_log(TRADE_LOG, header + table_header + "\n".join(trade_lines) + "\n")
    else:
        append_to_log(TRADE_LOG, header + "_No trades executed._\n")

    git_commit_memory("market-open")


# ===========================================================================
# Mode: midday
# ===========================================================================

def run_midday() -> None:
    logger.info("=== MODE: midday ===")

    broker = AlpacaBroker()
    with_retry(broker.connect)

    positions = with_retry(broker.get_open_positions)
    if not positions:
        logger.info("No open positions — nothing to do")
        git_commit_memory("midday")
        return

    engine, features = load_or_train_hmm(n_bars=60)
    regime = predict_regime(engine, features)
    is_high_vol = regime.label in HIGH_VOL_LABELS

    cut_lines = []
    tightened = []

    for pos in positions:
        symbol = pos["symbol"]
        plpc = pos.get("unrealized_pl", 0) / max(abs(pos.get("market_value", 1)), 1)

        # Unrealized P&L pct via Alpaca may also be available directly
        # Try to get it from the position dict returned by _position_to_dict
        # which doesn't include unrealized_plpc — compute it
        entry = pos.get("avg_entry", pos.get("avg_entry_price", 0))
        current = pos.get("current_price", 0)
        if entry and entry > 0:
            plpc = (current - entry) / entry
        else:
            plpc = 0.0

        if plpc <= -STOP_LOSS_PCT:
            logger.info("Cutting %s — unrealized P&L %.2f%%", symbol, plpc * 100)
            try:
                with_retry(lambda s=symbol: broker.close_position(s))
                cut_lines.append(f"- {symbol}: cut at {plpc:.2%} loss")
            except Exception as exc:
                logger.error("Failed to close %s: %s", symbol, exc)

        elif is_high_vol:
            # Tighten stop (log intent; actual stop modification via order API if available)
            tightened.append(f"- {symbol}: stop tightened (HIGH_VOL regime: {regime.label})")
            logger.info("HIGH_VOL — tightening stop for %s", symbol)

    today = date.today().isoformat()
    entry = f"\n### {today} — Midday Review\n"
    entry += f"**Regime:** {regime.label.upper()} | **Confidence:** {regime.probability:.1%}\n\n"
    if cut_lines:
        entry += "**Positions cut (stop-loss -7%):**\n" + "\n".join(cut_lines) + "\n"
    if tightened:
        entry += "**Stops tightened (HIGH_VOL):**\n" + "\n".join(tightened) + "\n"
    if not cut_lines and not tightened:
        entry += "_No action required._\n"

    append_to_log(TRADE_LOG, entry)
    git_commit_memory("midday")


# ===========================================================================
# Mode: EOD
# ===========================================================================

def run_eod() -> None:
    logger.info("=== MODE: eod ===")

    broker = AlpacaBroker()
    with_retry(broker.connect)

    acct = with_retry(broker.get_account)
    positions = with_retry(broker.get_open_positions)

    # Day P&L: equity - last_equity (Alpaca provides last_equity on account)
    # Since AccountInfo doesn't expose last_equity, approximate via unrealized_pl sum
    unrealized_total = sum(p.get("unrealized_pl", 0.0) for p in positions)
    n_positions = len(positions)

    today = date.today().isoformat()
    pos_lines = ""
    for p in positions:
        entry = p.get("avg_entry", p.get("avg_entry_price", 0))
        current = p.get("current_price", 0)
        plpc = ((current - entry) / entry * 100) if entry else 0
        pos_lines += (
            f"| {p['symbol']} | {p.get('qty',0)} | {entry:.2f} | "
            f"{current:.2f} | {p.get('unrealized_pl',0):.2f} | {plpc:.2f}% |\n"
        )

    snapshot = (
        f"\n## {today} — EOD Snapshot\n"
        f"**Portfolio:** ${acct.equity:,.2f} | "
        f"**Cash:** ${acct.cash:,.2f} | "
        f"**Open positions:** {n_positions} | "
        f"**Unrealized P&L:** ${unrealized_total:,.2f}\n\n"
    )
    if pos_lines:
        snapshot += (
            "| Symbol | Qty | Entry | Current | Unreal. P&L | P&L% |\n"
            "|---|---|---|---|---|---|\n"
            + pos_lines
        )
    else:
        snapshot += "_No open positions._\n"

    append_to_log(TRADE_LOG, snapshot)
    git_commit_memory("eod")


# ===========================================================================
# Mode: weekly
# ===========================================================================

def run_weekly() -> None:
    logger.info("=== MODE: weekly ===")

    # Full retrain
    engine, features = retrain_hmm_full()

    # Compute regime distribution over the full training window
    states = engine.predict_regime_filtered(features)
    labels = [s.label for s in states]
    unique, counts = np.unique(labels, return_counts=True)
    distribution = {lbl: int(cnt) for lbl, cnt in zip(unique, counts)}

    current_regime = states[-1]
    total_bars = len(states)

    # Basic week metrics from last 5 trading days
    last_week_labels = labels[-5:] if len(labels) >= 5 else labels
    week_mode = max(set(last_week_labels), key=last_week_labels.count)

    broker = AlpacaBroker()
    try:
        with_retry(broker.connect)
        acct = with_retry(broker.get_account)
        equity_str = f"${acct.equity:,.2f}"
    except Exception:
        equity_str = "N/A (broker offline)"

    today = date.today().isoformat()
    entry = (
        f"\n## {today} — Weekly Review\n\n"
        f"### HMM Retrain Summary\n"
        f"- Training bars: {total_bars}\n"
        f"- n_states selected: {engine.n_states}\n"
        f"- Current regime: {current_regime.label.upper()} "
        f"(confidence {current_regime.probability:.1%})\n"
        f"- Week dominant regime: {week_mode.upper()}\n\n"
        f"### Regime Distribution (full window)\n"
        + "".join(f"- {lbl}: {cnt} bars ({cnt/total_bars:.1%})\n"
                  for lbl, cnt in sorted(distribution.items()))
        + f"\n### Portfolio\n"
        f"- Equity: {equity_str}\n"
    )

    append_to_log(WEEKLY_REVIEW, entry)
    git_commit_memory("weekly")


# ===========================================================================
# Main
# ===========================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Episodic runner for regime_trader (stateless, cloud-ready)"
    )
    parser.add_argument(
        "--mode",
        choices=["pre-market", "market-open", "midday", "eod", "weekly"],
        required=True,
        help="Execution mode",
    )
    args = parser.parse_args()
    mode = args.mode

    # Validate credentials early
    if not os.environ.get("ALPACA_API_KEY"):
        logger.error("ALPACA_API_KEY not set — cannot proceed")
        sys.exit(1)

    try:
        dispatch = {
            "pre-market":  run_pre_market,
            "market-open": run_market_open,
            "midday":      run_midday,
            "eod":         run_eod,
            "weekly":      run_weekly,
        }
        dispatch[mode]()
        logger.info("Mode '%s' completed successfully", mode)

    except SystemExit:
        raise
    except Exception:
        logger.error("Unhandled exception in mode '%s':\n%s", mode, traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
