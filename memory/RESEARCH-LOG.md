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

## 2026-05-20 — Regime Detection (market-open)

### Account
- Equity: $105,525.53
- Cash: (pending fills)
- Open positions: 3 orders submitted (fills async)

### Regime Signal
- Detected regime: CRASH
- Confidence: 100.0%
- Consecutive bars: (HMM model from disk, 5-state)
- Flickering: no

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: ~$735.59
- QQQ: ~$800+ (est.)
- IWM: ~$195+ (est.)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: neutral (trading-bot log absent)
- Active earnings/catalyst risk: no
- Regime gate: OPEN (no catalyst gate active)

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | LONG | 20 | ~735 | 700.14 | 1.00 | HighVolDefensive 60% |
| QQQ | LONG | 11 | ~est | 645.00 | 1.00 | HighVolDefensive 60% |
| IWM | LONG | 57 | ~est | 265.64 | 1.00 | HighVolDefensive 60% |

### Decision
TRADE — CRASH regime, confidence 100%, no catalyst gate. HighVolDefensive strategy (60% invested, wider stops). Orders submitted to Alpaca paper; fills async.
