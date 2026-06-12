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

## 2026-06-12 — Pre-Market Regime Detection

### Account
- Equity: $107,877.64
- Cash: $9,214.06
- Buying power: $313,114.26
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: STRONG_BEAR
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

### HMM Training Note
- **RETRAIN: first-ever fit** (no prior model on disk)
- n_states selected: 6 (BIC-optimal over 3–7)
- Training bars: 343 clean (from 504 fetched)
- BIC: 5378.27 | log-likelihood: -502.91
- Convergence warnings: multiple (numeric precision only, delta < 1e-4 — benign)

### Anomalies / Startup Fixes Applied This Session
1. **SIP feed → IEX**: free-tier Alpaca account blocked SIP; switched `StockBarsRequest(feed="iex")`
2. **Method rename**: `engineer.compute_features()` → `engineer.build_feature_dataframe()`
3. **Insufficient bars**: `load_or_train_hmm(n_bars=60)` → `n_bars=settings.HMM_TRAINING_DAYS` (504); with only 60 bars all features dropped on `dropna()` due to `_ZSCORE_WINDOW=252` and `sma200(min_periods=100)`

### Decision
HOLD — regime STRONG_BEAR confirmed=False (1/3 consecutive bars required)
