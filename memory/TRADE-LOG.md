# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

---

## 2026-05-11 — Pre-Market Snapshot
**Portfolio:** $107,909.79 | **Cash:** $-102,287.48 | **Long Exposure:** $210,197 | **Leverage:** ~1.95x
**Regime (latest bar):** CRASH (100% conf) — NOT confirmed (1/3 bars) → HOLD
**Phase P&L:** +$7,909.79 (+7.91% from $100k baseline)

### Open Positions
| ETF | Qty | Avg Entry | Price (approx) | Market Val | Unrealized PnL | PnL% | Stop |
|-----|-----|-----------|----------------|------------|----------------|------|------|
| SPY | 127 | $715.80 | ~$736.97 | $93,595 | +$2,688 | +2.96% | TBD |
| QQQ | 73  | $664.05 | ~$710.40 | $51,859 | +$3,383 | +6.98% | TBD |
| IWM | 228 | $275.90 | ~$284.05 | $64,743 | +$1,838 | +2.92% | TBD |

### Notes
- CRASH regime detected at 1 consecutive bar — insufficient for confirmation (need 3)
- If CRASH confirms over next 2 bars: HighVolDefensiveStrategy activates (max 5% pos, reduce to cash)
- Leverage ~1.95x is aggressive — risk elevated if regime confirms bearish shift
- No stops logged on entry; need to establish stops before market open
