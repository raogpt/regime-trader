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

## 2026-05-28 — Regime Detection

### Account
- Equity: $113,115
- Cash: -$108,622 (leveraged; buying power $4,483)
- Open positions: 3 (IWM 287, QQQ 88, SPY 100)

### Regime Signal
- Detected regime: BULL
- Confidence: 100%
- Flickering: no (is_flickering=False)
- HMM: loaded from disk (n_states=5, fresh model)

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: $749.33 | 2×ATR stop: $738.44
- QQQ: $727.52 | 2×ATR stop: $709.36
- IWM: $288.37 | 2×ATR stop: $280.80

### Cross-Enrichment Signal
- Regime gate: OPEN (trading-bot log not populated; default pass-through)
- Sizing modifier: 1.0 (no cross-enrichment conflict)

### Signals Generated
| ETF | Side | Entry | Stop | Conf | Reason |
|-----|------|-------|------|------|--------|
| SPY | LONG | $749.33 | $738.44 | 1.00 | BULL regime |
| QQQ | LONG | $727.52 | $709.36 | 1.00 | BULL regime |
| IWM | LONG | $288.37 | $280.80 | 1.00 | BULL regime |

### Decision
HOLD — all signals LONG/BULL but account fully deployed (196%); insufficient buying power ($4,483) for new orders. Positions intact and profitable (+$8,912 unreal).
