# Comparison Log — trading-bot vs regime_trader

Weekly side-by-side performance tracking.

| Week | trading-bot | regime_trader | S&P 500 | Winner |
|------|------------|---------------|---------|--------|
| 2026-04-27 | TBD | TBD (bot launched) | +4.27% ITD | — |
| 2026-05-23 | N/A (no cloud access) | ~+3.31% wk / +10.91% ITD | +0.89% wk / +4.27% ITD | regime_trader |

## Notes
- trading-bot: discretionary swing, individual stocks, Claude-driven
- regime_trader: systematic HMM, ETFs, volatility-regime-based
- Both on Alpaca paper accounts (separate $100k each)
- Comparison starts week of Apr 27, 2026
- trading-bot data not available from cloud environment (local path only)
- regime_trader week return estimated from position-level delta (no EOD equity snapshots yet)

## ITD Scorecard (as of 2026-05-23)
| Bot | ITD Return | vs S&P 500 (+4.27%) | Alpha |
|-----|-----------|---------------------|-------|
| regime_trader | +10.91% | +6.64% | ✅ |
| trading-bot | TBD | TBD | — |
| S&P 500 (SPY) | +4.27% | baseline | — |
