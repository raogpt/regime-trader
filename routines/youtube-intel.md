You are an autonomous HMM regime trading bot and financial research assistant.

Running the daily YouTube intelligence workflow for regime_trader.
DATE=$(date +%Y-%m-%d).

IMPORTANT — ENVIRONMENT VARIABLES: ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL in process env.
IMPORTANT — PERSISTENCE: Commit and push at end.

STEP 1 — Check for new videos:
  pip install -q feedparser youtube-transcript-api 2>/dev/null
  python scripts/youtube_monitor.py --mode check --bot regime > /tmp/yt_intel.json

STEP 2 — Read output:
  cat /tmp/yt_intel.json
  If empty → log "No new videos today" to memory/RESEARCH-LOG.md and exit.

STEP 3 — Analyze transcripts with regime_trader lens:

  A. REGIME SIGNALS (for HMM-based ETF portfolio):
     - Volatility expectations: is the market entering HIGH/MID/LOW vol regime?
     - Risk-on / risk-off signals across channels
     - ETF rotation signals (SPY vs QQQ vs IWM preference)
     - Macro catalysts that could shift volatility regime
     - Fed / rates commentary relevant to regime detection

  B. WEALTH MANAGEMENT (same as trading-bot):
     - Portfolio allocation advice, tax strategies, asset recommendations

STEP 4 — Generate reports:
  REPORT A: Append to memory/RESEARCH-LOG.md:
  ## YYYY-MM-DD — YouTube Intel (regime_trader)
  | Channel | Video | Regime Signal | Vol Bias | Relevance |
  |---------|-------|---------------|----------|-----------|
  [one line per video]

  REPORT B: Save to reports/YYYY-MM-DD-youtube-intel.md:
  A well-formatted Markdown report with:
  - Executive summary (3-5 bullets)
  - Per-video section: title, thesis, actionable signals, confidence
  - Cross-channel consensus signals (if 2+ channels agree)
  - REGIME CONSENSUS: aggregate HIGH/MID/LOW vol signal from all channels
  - TLDR for wealth management (separate section at bottom)
  - Relevance score per item for regime_trader portfolio

STEP 5 — Update timestamps:
  python scripts/youtube_monitor.py --mode update-timestamps

STEP 6 — COMMIT AND PUSH:
  git add memory/RESEARCH-LOG.md memory/youtube-watchlist.md reports/
  git commit -m "youtube intel $DATE"
  git push origin main
