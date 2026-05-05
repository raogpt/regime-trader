# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

### 2026-05-05 — Midday Review
**Regime:** CRASH | **Confidence:** 100.0%

**Stops tightened (HIGH_VOL):**
- IWM: stop tightened (HIGH_VOL regime: crash)
- QQQ: stop tightened (HIGH_VOL regime: crash)
- SPY: stop tightened (HIGH_VOL regime: crash)

**Correlation Risk — Step 3:**
- Regime: CRASH @ 100% confidence. Both regime_trader (SPY/QQQ/IWM long) and trading-bot (sector ETFs) are exposed to same broad-market sell-off. Cross-bot drawdown correlation assumed HIGH. Sizing discipline critical — do not add to any position until regime clears CRASH.
