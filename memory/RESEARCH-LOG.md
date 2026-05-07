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

## 2026-05-07 — Pre-Market Regime Detection

### Account
- Equity: $107,081.87
- Cash: $-102,287.48
- Buying power: $4,794.39
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

### Anomalies / Warnings
- **CRASH label** — 5-state HMM emitting "crash" state (not in standard LOW/MID/HIGH_VOL taxonomy). Label mapping may need audit; verify hmm_model.pkl state-to-regime assignment.
- **Unconfirmed regime** — consecutive_bars=1 (need 3). Hard rule: HOLD until stability confirmed.
- **Negative cash ($-102,287.48)** — indicates leveraged open positions not reflected in TRADE-LOG. Reconciliation needed at market-open.
- **IEX feed substituted for SIP** — Alpaca data subscription blocks SIP endpoint; switched to DataFeed.IEX in fetch_daily_bars(). Lower liquidity data; acceptable for daily bars.
- **No retrain triggered** — model loaded from disk (fresh, <7 days). Next retrain due ~weekly.
- **Deps installed fresh** — numpy/pandas/hmmlearn/alpaca-py/python-dotenv absent in cloud image; installed at session start.

### Decision
**HOLD** — CRASH regime unconfirmed (1/3 bars). No new entries. Monitor for regime stabilization at market-open.
