# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

### 2026-05-06 — Midday Review
**Regime:** CRASH | **Confidence:** 100.0%

**Stops tightened (HIGH_VOL):**
- IWM: stop tightened (HIGH_VOL regime: crash)
- QQQ: stop tightened (HIGH_VOL regime: crash)
- SPY: stop tightened (HIGH_VOL regime: crash)

**Correlation Risk Note:**
- HMM regime = CRASH (100% confidence). All three ETF positions (SPY/QQQ/IWM) are highly correlated in crash regimes.
- trading-bot P&L unavailable, but CRASH regime implies both bots likely in drawdown simultaneously if either holds long ETF exposure.
- Action: circuit breakers active; sizing already reduced via stop-tightening. Monitor for -7% stop triggers.
