# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

## 2026-05-07 — Market Open
**Regime:** CRASH | **Confidence:** 100.0% | **Portfolio:** $106,971.17
**Cash:** -$102,287 (negative — margin used) | **Buying Power:** $4,659

### Existing Positions (discovered, not logged previously)
| ETF | Qty | Market Value |
|-----|-----|-------------|
| SPY | 127 | $93,291 |
| QQQ | 73  | $50,905 |
| IWM | 228 | $65,080 |
**Total exposure:** ~$209,276 (~1.95× leverage)

### HOLD — insufficient buying power
- All three BUY orders rejected by Alpaca: insufficient buying power
- Account already ~1.95× leveraged (limit: 1.25×) from prior sessions
- CRASH regime at 100% confidence — no new entries warranted
- Action: hold existing positions, no new orders
