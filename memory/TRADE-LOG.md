# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

### 2026-05-01 — Midday Review
**Regime:** CRASH | **Confidence:** 100.0%

**Stops tightened (HIGH_VOL):**
- IWM: stop tightened (HIGH_VOL regime: crash)
- QQQ: stop tightened (HIGH_VOL regime: crash)
- SPY: stop tightened (HIGH_VOL regime: crash)

**Cross-bot correlation check:**
- trading-bot RESEARCH-LOG: inaccessible (iCloud path not mounted in cloud env)
- regime_trader status: CRASH regime → positions likely in drawdown
- ⚠️ CORRELATION RISK NOTE: With CRASH regime active, assume both bots are in drawdown simultaneously. Full correlation risk present — no diversification benefit. Do not add size.
