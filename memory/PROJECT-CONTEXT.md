# Project Context — regime_trader

## Overview
- What: Autonomous HMM-based regime trading bot
- Account: Alpaca paper #2 (separate from trading-bot)
- Universe: SPY, QQQ, IWM (ETF only — no individual stocks)
- Strategy: Volatility-regime detection via Gaussian HMM, 3-7 states
- Bar size: 5-minute (episodic mode via REST) and daily (HMM training)

## Architecture
- models/hmm_engine.py — HMM with BIC-based state selection (3-7 states)
- models/regime_strategies.py — 3 strategies: LowVol/MidVol/HighVol
- data/feature_engineering.py — 14 rolling features, forward-safe
- execution/order_executor.py — Alpaca REST orders
- risk/risk_manager.py — circuit breakers, position sizing
- episodic_runner.py — stateless cloud-compatible runner (no WebSocket)

## Regime Labels (volatility-ranked)
- LOW_VOL → 95% allocation, 1.25x leverage
- MID_VOL → 60-95% allocation, 1.0x leverage
- HIGH_VOL → 60% allocation, 1.0x leverage, wide stops

## Cross-Enrichment (from trading-bot)
- Earnings/catalyst filter: avoid entry 2 days before FOMC, CPI, major ETF earnings
- Sector momentum bias: if trading-bot is in Materials/Energy → prefer IWM

## Key Files
- memory/PROJECT-CONTEXT.md (this file)
- memory/TRADE-LOG.md
- memory/RESEARCH-LOG.md
- memory/WEEKLY-REVIEW.md
- memory/COMPARISON-LOG.md (shared with trading-bot)

## Rules
- NEVER share API keys externally
- Every trade logged BEFORE execution
- HMM retrained weekly (or if model > 7 days old)
- Circuit breakers are HARD stops — never override

## Market Intel Routine (weekly)
Canonical entry point — if a scheduled-task prompt naming a different script
disagrees with this, this file wins (scripts get renamed; this file is the
thing to keep current):
- Install deps fresh each session:
  `pip install --no-deps feedparser && pip install requests youtube-transcript-api`
  — feedparser's own `sgmllib3k` dependency fails to build here (unrelated
  distutils/setuptools issue), so install feedparser with `--no-deps`;
  `scripts/vendor/sgmllib.py` covers the runtime import it would have provided.
- `python scripts/intel_monitor.py --mode check --bot regime` — 23-source
  RSS check (7 YouTube + 16 blog/official, incl. UEMOA: Sika Finance, BCEAO,
  Financial Afrik). Outputs JSON (new items, VIX snapshot, per-item
  relevance tier) to stdout; also live-fetches/drains YouTube transcripts
  inline (see scripts/intel_monitor.py's module docstring).
- Append findings to `memory/RESEARCH-LOG.md`, save a full report to
  `reports/YYYY-MM-DD-market-intel.md`.
- `python scripts/intel_monitor.py --mode update-timestamps` when done.
- Commit + push `memory/RESEARCH-LOG.md memory/intel-watchlist.md
  memory/transcript-queue.json reports/` to this repo's active branch (not
  necessarily `main` — check current branch/task instructions).
- `scripts/fetch_transcripts.py` and `.github/workflows/fetch-transcripts.yml`
  are an optional fallback transcript drain, not a dependency — the main
  script above is self-sufficient.
