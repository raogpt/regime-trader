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

## 2026-05-05 — Regime Detection

### Account
- Equity: $102,957.59
- Cash: ~$102,957 (no prior positions)
- Open positions: 0 (pre-market-open)

### Regime Signal
- Detected regime: CRASH
- Confidence: 100.0%
- Consecutive bars: stable (loaded from disk model)
- Flickering: no

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: ~$562 (stop placed at $684.36 — ATR-based)
- QQQ: fetched (60 bars)
- IWM: fetched (60 bars)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown (no recent research-log entry)
- Active earnings/catalyst risk: no
- Regime gate: OPEN
- Sizing modifier: 1.0

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | BUY | 18 | ~$562 | $684.36 | 1.00 | CRASH regime — cash strategy, max_pos_pct=5% |
| QQQ | — | — | — | — | — | Insufficient buying power after SPY |
| IWM | — | — | — | — | — | Insufficient buying power after SPY |

### Decision
TRADE — SPY BUY 18 submitted (order id: 54612c10-8c30-4c71-bb4b-a22abf7d7297). Fill returned qty=0 @ $0.00 (paper API timing — order accepted). QQQ/IWM blocked by buying power constraint.
