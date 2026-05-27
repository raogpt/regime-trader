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

## 2026-05-27 — Regime Detection

### Account
- Equity: $113,848.21
- Cash: -$108,622.12
- Open positions: 3 (IWM 287, QQQ 88, SPY 100)

### Regime Signal
- Detected regime: BULL
- Confidence: 100%
- Consecutive bars: ≥3 (confirmed)
- Flickering: no

### ETF Snapshot (from Alpaca REST — IEX feed)
- SPY: $750.11
- QQQ: $729.59
- IWM: $290.04

### Cross-Enrichment Signal
- Sector momentum: unknown (trading-bot log not mounted)
- Active earnings/catalyst risk: no
- Sizing modifier: 1.0x
- Regime gate: OPEN

### Signals Generated
All three ETFs → LONG (BULL strategy). Orders rejected by broker: insufficient buying power.

### Decision
HOLD — Existing LONG positions maintained. No new entries possible (BP exhausted).
Regime aligned with open positions. No action required.
