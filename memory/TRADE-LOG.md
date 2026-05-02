# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## Week 1 EOW Snapshot (2026-05-02)
**Portfolio:** $102,173.43 | **Cash:** -$59,383.34 (leveraged) | **Phase P&L:** +$2,173.43 (+2.17%)
**Regime:** EUPHORIA (confidence 100%, 6-state HMM, BIC-optimal)

### Open Positions Discovered at EOW Review
| ETF | Shares | Avg Entry | Current | Unrealized P&L | P&L% | Regime at Entry |
|-----|--------|-----------|---------|----------------|------|-----------------|
| IWM | 194 | $275.20 | $279.28 | +$790.87 | +1.48% | EUPHORIA |
| QQQ | 62 | $662.13 | $674.15 | +$745.18 | +1.82% | EUPHORIA |
| SPY | 91 | $713.65 | $720.65 | +$637.38 | +0.98% | EUPHORIA |

> Note: Intra-week trade entries were not captured in this log (cloud session isolation gap). Positions verified live via Alpaca API 2026-05-02.

### Stops (from regime strategy — EUPHORIA / ATR-based)
- IWM stop: ~$263.82 (entry - 2× ATR est.)
- QQQ stop: ~$635.24 (entry - 2× ATR est.)
- SPY stop: ~$685.10 (entry - 2× ATR est.)
