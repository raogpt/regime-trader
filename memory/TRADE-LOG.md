# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## 2026-05-22 — Market Open
**Regime:** CRASH | **Confidence:** 100.0% | **Portfolio:** $111,267.17 | **Cash:** -$108,622 (margin)
**Consecutive bars:** 1/3 (NOT YET CONFIRMED — await 3 bars before regime action)

### Open Positions
| ETF | Qty | Avg Entry | Current | Mkt Val | Unreal P&L |
|-----|-----|-----------|---------|---------|-----------|
| IWM | 287 | $275.30 | $284.71 | $81,710 | +$2,698 |
| QQQ | 88  | $691.47 | $719.80 | $63,342 | +$2,493 |
| SPY | 100 | $729.51 | $747.78 | $74,778 | +$1,826 |
**Total unrealized P&L: +$7,017 | Leverage: ~2x (margin account)**

### Today's Execution
- CRASH regime detected — confidence 100%, but only 1 consecutive bar (need 3)
- SPY BUY: REJECTED — insufficient buying power ($9,554 available, $11,956 required)
- QQQ BUY 10 shares: submitted — paper fill returned 0 shares (async timing); position unchanged at 88
- IWM BUY: REJECTED — insufficient buying power ($2,363 available, $11,655 required)
- ⚠️ WATCH: If CRASH regime persists for 2 more bars → trigger defensive exit per hard rules
