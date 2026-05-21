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

## 2026-05-21 — Pre-Market Regime Detection

### Account
- Equity: $108,587.07
- Cash: $-101,428.52
- Buying power: $7,158.55
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

### Open Positions (from Alpaca)
| ETF | Shares | Avg Entry | Mkt Val | Unreal P&L |
|-----|--------|-----------|---------|------------|
| IWM | 287 | $275.30 | $80,288 | +$1,276 |
| QQQ | 78 | $687.90 | $55,568 | +$1,912 |
| SPY | 100 | $729.51 | $74,150 | +$1,199 |
- Total mkt val: ~$210,006 | Account leverage: ~1.93x
- Total unrealized P&L: +$4,387

### Decision
HOLD — Regime not confirmed (1/3 bars required)

### Anomalies & Notes
- **CRASH regime (100% conf)** — 5-state HMM labelled this bar as "crash" state, not standard LOW/MID/HIGH_VOL. Watch: if confirmed over next 2 bars, consider reducing to 60% allocation per HIGH_VOL rules.
- **Account 1.93x leveraged** — existing long positions in all 3 ETFs. Positions are profitable (+$4,387). Negative cash ($-101k) is margin usage.
- **Cross-enrichment unavailable** — trading-bot RESEARCH-LOG not accessible; sector momentum defaults to unknown.
- **Bug fixes applied this session:**
  - Data feed switched to IEX (free tier; SIP blocked at current subscription)
  - n_bars 60→300 to satisfy _ZSCORE_WINDOW=252 (min_periods=63)
  - FeatureEngineer method: compute_features → build_feature_dataframe
- **Model age:** loaded from disk (fresh, <7 days) — no retrain triggered
