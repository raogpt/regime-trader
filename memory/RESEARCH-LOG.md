# Research Log — regime_trader

Daily regime detection entries appended here.
Format:

## YYYY-MM-DD — Regime Detection

### Account
- Equity: $X
- Cash: $X
- Open positions: N

### Regime Signal
- Detected regime: LOW_VOL / MID_VOL / HIGH_VOL
- Confidence: X%
- Consecutive bars: N
- Flickering: yes/no

### ETF Snapshot (from Alpaca REST)
- SPY: $X (Xd chg: X%)
- QQQ: $X (Xd chg: X%)
- IWM: $X (Xd chg: X%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: X
- Active earnings/catalyst risk: yes/no (detail)
- Regime gate: OPEN / BLOCKED

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|

### Decision
TRADE or HOLD

---

## 2026-05-15 — Regime Detection

### Account
- Equity: $106,657
- Cash: $9,577
- Open positions: 3 (SPY 44sh · QQQ 46sh · IWM 115sh)

### Regime Signal
- Detected regime: CRASH
- Confidence: 100%
- HMM model: loaded from disk (5-state, fresh)
- Strategy: HighVolDefensiveStrategy (60% target allocation per ticker)

### ETF Snapshot (from Alpaca IEX feed)
- SPY: $739.20 (stop: $696.46)
- QQQ: $707.35 (stop: $639.16)
- IWM: $278.40 (stop: $265.11)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown (trading-bot log not mounted)
- Active earnings/catalyst risk: no
- Regime gate: OPEN
- Sizing modifier: 1.0×

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | SELL | 83 | 739.13 | 696.46 | 1.00 | Reduce to 60% target; crash regime |
| QQQ | SELL | 35 | 707.18 | 639.16 | 1.00 | Reduce to 60% target; crash regime |
| IWM | SELL | 113 | 278.39 | 265.11 | 1.00 | Reduce to 60% target; crash regime |

### Decision
TRADE — Deleveraged from ~2× to ~1× (CRASH regime, 100% confidence)
