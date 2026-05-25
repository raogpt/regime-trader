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

## 2026-05-25 — Regime Detection

### Account
- Equity: $100,000.00 (baseline, no trades yet)
- Cash: $100,000.00
- Open positions: 0

### Regime Signal
- Detected regime: N/A
- Confidence: N/A
- Consecutive bars: N/A
- Flickering: N/A

### ETF Snapshot
- SPY: N/A (market closed — Memorial Day)
- QQQ: N/A
- IWM: N/A

### Cross-Enrichment Signal
- Sector momentum: N/A
- Active earnings/catalyst risk: N/A
- Regime gate: BLOCKED (market holiday)

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| — | — | — | — | — | — | Market closed (Memorial Day) |

### Decision
HOLD — Market closed (US Memorial Day holiday, 2026-05-25)
