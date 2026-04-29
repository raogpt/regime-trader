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

## 2026-04-29 — Pre-Market Regime Detection

### Account
- Equity: $99,741.38
- Cash: $40,642.32
- Buying power: $140,383.70
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
- CRASH regime at 100% confidence — HIGH_VOL_LABELS group, maps to HighVolDefensiveStrategy
- consecutive_bars=1; regime NOT confirmed (needs 3 stable bars before acting)
- Decision: HOLD — await 2 more confirming bars before any position entry
- No retrain triggered (model fresh, loaded from disk)
- Session fixes applied: data feed switched to IEX (SIP subscription blocked); FeatureEngineer API corrected (compute_features→build_feature_dataframe); n_bars raised 60→250 (sma200 requires ≥100 bars)
