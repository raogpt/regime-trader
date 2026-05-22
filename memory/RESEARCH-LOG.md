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

## 2026-05-22 — Regime Detection

### Account
- Equity: $111,267.17
- Cash: -$108,622.12 (margin in use)
- Open positions: 3 (SPY 100sh, QQQ 88sh, IWM 287sh)
- Buying power: $2,645.05

### Regime Signal
- Detected regime: CRASH
- Confidence: 100%
- Consecutive bars: 1
- Flickering: no
- **Confirmed: NO — need 3 consecutive bars**

### ETF Snapshot (via yfinance — Alpaca SIP blocked on free tier)
- SPY: $747.86 (5d chg: +1.25%)
- QQQ: $720.05 (5d chg: +2.01%)
- IWM: $284.84 (5d chg: +3.21%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: N/A (cross-enrichment returned default/no signal)
- Active earnings/catalyst risk: unknown
- Regime gate: checked (high_vol + catalyst gate logic evaluated)

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | BUY | — | ~$747 | — | 1.00 | REJECTED — insufficient buying power |
| QQQ | BUY | 10 | ~$720 | $649.33 | 1.00 | Submitted (paper async — likely 0 filled) |
| IWM | BUY | — | ~$285 | — | 1.00 | REJECTED — insufficient buying power |

### Decision
ATTEMPTED TRADE — largely blocked by margin/buying power exhaustion.
⚠️ CRASH regime flag: monitor for 2 more consecutive CRASH bars. If confirmed → reduce all positions per hard rules.
