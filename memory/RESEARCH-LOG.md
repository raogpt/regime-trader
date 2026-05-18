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

## 2026-05-18 — Pre-Market Regime Detection

### Account
- Equity: $106,362.25
- Cash: $9,576.85
- Buying power: $115,939.10
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

### Anomalies / HMM Warnings
- **CRASH label at 100% confidence** — 5-state HMM (loaded from pkl). Confidence=1.0 may indicate model is firmly in lowest-volatility-rank state mapped to "crash". Verify label↔rank mapping matches current market context.
- **Model freshness** — pkl was present at session start; model age unknown. If >7 days, next weekly-review will retrain on full 504-bar history.
- **First live session** — no prior confirmed regime bars; consecutive_bars=1 (need 3 for confirmation). NO trading action triggered.
- **Fix applied** — data fetch upgraded: IEX feed (SIP subscription blocked on paper account), n_bars 60→300 (SMA200 needs min 100 bars to produce valid features).
- **Account positions** — equity $106,362 vs cash $9,577 implies ~$96,785 deployed in existing positions. Review TRADE-LOG for details before market-open.

### Decision
HOLD — regime unconfirmed (1/3 bars)
