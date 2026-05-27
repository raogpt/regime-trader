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

## 2026-05-27 — Pre-Market Regime Detection

### Account
- Equity: $115,275.08
- Cash: $-108,622.12
- Buying power: $6,652.96
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: BULL
- Confidence: 74.9%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

### Anomalies & Fixes (2026-05-27)
- **BUG FIXED** `feed="iex"`: Alpaca free-tier blocked SIP data feed (403 Forbidden). Fixed in `fetch_daily_bars()`.
- **BUG FIXED** `build_feature_dataframe`: `compute_features()` method did not exist on `FeatureEngineer`; corrected to `build_feature_dataframe()`.
- **BUG FIXED** `n_bars 60→300`: sma200 requires min_periods=100; 60-bar fetch yielded empty feature matrix after dropna(). All modes now fetch 300 bars → ~137 valid feature rows.
- **HMM MODEL**: Loaded from disk (5 states, fresh — no retrain triggered). Last trained: <7 days ago.
- ⚠️ **CASH WARNING**: Cash is deeply negative (-$108,622) with only $6,652 buying power. Existing positions consuming nearly all margin. NO new entries advisable until positions are reviewed.
- **REGIME NOT CONFIRMED**: BULL at 74.9% confidence but only 1 consecutive bar (need 3). Rule: HOLD until regime stable.

### Decision
HOLD — regime not confirmed (1/3 bars). Low buying power. Await market-open check.
