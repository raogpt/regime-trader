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

## 2026-05-14 — Pre-Market Regime Detection (STALE MODEL — SUPERSEDED)

### Account
- Equity: $109,066.88
- Cash: $-107,980.63
- Buying power: $1,086.25
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: EUPHORIA
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

## 2026-05-14 — Anomalies & Session Notes

### Bugs Fixed This Session
- **IEX feed**: `StockBarsRequest` was missing `feed="iex"` → 403 SIP subscription error. Fixed.
- **API mismatch**: `FeatureEngineer.compute_features()` → renamed to `build_feature_dataframe()`. Fixed.
- **n_bars 60 → 400**: Feature z-score window is 252 bars; 60 bars produced all-NaN features → empty array → HMM crash. Fixed.

### HMM Retrain Triggered
- Stale model: trained 2026-04-25 (19 days ago), exceeds 7-day retrain interval.
- File mtime (May 11 clone) masked the true age — `_model_is_fresh()` uses mtime, not embedded `training_date`.
- **Action**: deleted stale pickle, forced retrain. New model: n_states=5, BIC=1499.36.
- **Critical**: stale model predicted CRASH (100%), fresh model predicts EUPHORIA (100%) — opposite regimes.

### Account Anomaly
- Cash: $-107,980.63 (deeply negative) vs Equity: $109,066.88
- Buying power: $1,086.25 — essentially fully deployed, no room for new positions.
- Pre-market mode does NOT open new trades (market-open mode handles that).

### Decision
- **HOLD** — regime EUPHORIA at 100% confidence but NOT confirmed (1 bar vs 3 required).
- Will reassess at market-open once 3 consecutive bars confirmed.
