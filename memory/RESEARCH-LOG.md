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

## 2026-06-05 — Regime Detection

### Account
- Equity: $112,937.78
- Cash: -$108,622.12 (margin — fully invested)
- Open positions: 3 (SPY 100sh, QQQ 88sh, IWM 287sh)

### Regime Signal
- Detected regime: BULL
- Confidence: 100%
- Consecutive bars: 1
- Flickering: no

### ETF Snapshot (from Alpaca REST / IEX)
- SPY: $750.76 (5d chg: -0.74%)
- QQQ: $728.12 (5d chg: -1.37%)
- IWM: $287.32 (5d chg: -1.04%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Active earnings/catalyst risk: no
- Regime gate: OPEN

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | LONG | — | $750.76 | — | 100% | BULL regime — order failed (insufficient buying power) |
| QQQ | LONG | — | $728.12 | — | 100% | BULL regime — order failed (insufficient buying power) |
| IWM | LONG | — | $287.32 | — | 100% | BULL regime — order failed (insufficient buying power) |

### Decision
HOLD — account fully invested (margin); no additional buying power ($8,631 remaining)
- Existing positions profitable: SPY +$2,117 | QQQ +$3,223 | IWM +$3,443
- Portfolio up +12.9% from $100k baseline
- Regime not yet confirmed (1 of 3 required consecutive bars)
