# Trade Log — regime_trader

## Day 0 — Baseline (pre-launch)
**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0
**Regime:** UNKNOWN (HMM not yet run in episodic mode)

No positions. Bot launches Monday Apr 27.

---

## 2026-05-04 — Pre-Market Snapshot
**Portfolio:** $101,265.74 | **Cash:** $-59,383.34 (leveraged) | **Buying Power:** $41,882.40
**Phase P&L:** +$1,265.74 vs baseline
**Regime:** CRASH (conf 100%, 1 bar — NOT confirmed)

### Open Positions
| ETF | Qty | Avg Entry | Mkt Value | Unrealized P&L |
|-----|-----|-----------|-----------|----------------|
| SPY | 91  | $713.65   | $65,247   | +$306.14       |
| QQQ | 62  | $662.13   | $41,577   | +$524.46       |
| IWM | 194 | $275.20   | $53,730   | +$340.79       |

**Action: HOLD** — regime unconfirmed. No new entries.
**Watch:** If CRASH confirmed 3 consecutive bars → consider defensive reduction per HighVolDefensiveStrategy (max 5% position per ETF).
