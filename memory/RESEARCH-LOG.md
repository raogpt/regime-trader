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

## 2026-05-18 — Regime Detection

### Account
- Equity: $106,516.17
- Cash: -$25,807.54 (fully invested, existing positions)
- Open positions: 3 (SPY 61sh, QQQ 56sh, IWM 172sh)

### Regime Signal
- Detected regime: CRASH (state_id=0)
- Confidence: 100%
- Consecutive bars: 1 (not confirmed — uncertainty mode active, size halved)
- Flickering: no

### ETF Snapshot (from Alpaca REST)
- SPY: $738.57 (1d chg: -0.07%)
- QQQ: $707.82 (1d chg: -0.15%)
- IWM: $276.97 (1d chg: -0.25%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown (trading-bot offline)
- Active earnings/catalyst risk: no
- Regime gate: OPEN (catalyst_gate=False, sizing_modifier=1.0)

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | LONG | 17 | ~738.40 | 698.00 | 1.00 | HighVolDefensive 30% (60%×0.5 uncertainty) |
| QQQ | LONG | 10 | ~707.80 | 641.79 | 1.00 | HighVolDefensive 30% (60%×0.5 uncertainty) |
| IWM | LONG | 57 | ~277.02 | 265.37 | 1.00 | HighVolDefensive 30% (60%×0.5 uncertainty) |

### Decision
TRADE — CRASH regime, high confidence, no catalyst gate. Uncertainty mode (1/3 bars confirmed) → position size halved to 30%. Market orders submitted; fills async in paper trading.
