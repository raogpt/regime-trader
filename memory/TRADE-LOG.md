# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

### 2026-05-25 — Midday Review
**Regime:** CRASH | **Confidence:** 100.0%

**Stops tightened (HIGH_VOL):**
- IWM: stop tightened (HIGH_VOL regime: crash)
- QQQ: stop tightened (HIGH_VOL regime: crash)
- SPY: stop tightened (HIGH_VOL regime: crash)

**⚠️ Correlation Risk Note (Step 3):**
- HMM regime: CRASH at 100% confidence — broad market stress signal
- All 3 ETF positions (SPY, QQQ, IWM) are highly correlated in a crash regime
- trading-bot comparison data unavailable (COMPARISON-LOG TBD); cannot confirm cross-bot drawdown
- If trading-bot is also in drawdown: combined portfolio exposure amplified — consider sizing reduction per hard rules (50% if sector momentum conflicts)
