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

## 2026-06-03 — Pre-Market Regime Detection

### Account
- Equity: $116,644.30
- Cash: $-108,622.12
- Buying power: $8,022.18
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: BULL
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

### ETF Snapshot (live positions)
- SPY: 100 shares @ $729.51 avg → MV $75,920 | unrealized +$2,969
- QQQ: 88 shares @ $691.47 avg → MV $65,802 | unrealized +$4,952
- IWM: 287 shares @ $275.30 avg → MV $83,500 | unrealized +$4,487

### Anomalies
1. **LEVERAGE BREACH**: Long MV $225,222 / Equity $116,644 = 1.93x. Hard rule max is 1.25x for LOW_VOL, 1.0x for MID/HIGH_VOL. Positions appear to have been opened in a prior session with no TRADE-LOG record.
2. **HMM state label**: Regime detected as "BULL" — not a standard LOW_VOL/MID_VOL/HIGH_VOL label. Saved model (n_states=5) uses raw HMM state names. State-to-volatility-regime mapping should be verified.
3. **Confirmation gate**: Only 1 consecutive bar. Hard rule requires 3 before acting. No new entries today.
4. **Session fixes applied**: (a) IEX feed substituted for SIP (subscription limit); (b) `compute_features` → `build_feature_dataframe`; (c) `fetch_daily_bars` now fetches +300 warmup bars for rolling windows.

### Decision
HOLD — regime unconfirmed (1/3 bars). Leverage already breached; no new entries.
Existing positions: HOLD, monitor stops.
