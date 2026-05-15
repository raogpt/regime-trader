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

## 2026-05-15 — Pre-Market Regime Detection

### Account
- Equity: $107,729.54
- Cash: $-107,980.63
- Buying power: $0.00
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: CRASH
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

### ETF Snapshot (from Alpaca IEX)
- SPY: $748.10 (1d chg: +0.78%, 5d chg: +2.27%)
- QQQ: $719.75 (1d chg: +0.73%, 5d chg: +3.57%)
- IWM: $284.46 (1d chg: +0.63%, 5d chg: +0.77%)

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| — | — | — | — | — | — | CRASH regime unconfirmed (1/3 bars) |

### Anomalies / HMM Warnings
- CRASH regime detected (5th HMM state, outside LOW/MID/HIGH_VOL labels)
- `confirmed=False` — only 1 consecutive bar; hard rule requires 3 before acting
- Account cash: -$107,980.63 / buying_power: $0.00 — suggests existing open margin exposure; investigate in market-open

### Decision
**HOLD** — CRASH regime not yet confirmed (1/3 bars required). No new entries.
