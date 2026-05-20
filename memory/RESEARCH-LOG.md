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

## 2026-05-20 — Pre-Market Regime Detection

### Account
- Equity: $106,061.60
- Cash: $-63,382.86
- Buying power: $42,678.74
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

### Anomalies & Runner Fixes (2026-05-20)
- **Bug 1 fixed:** Alpaca data feed `SIP` → `iex` (403 subscription error)
- **Bug 2 fixed:** `FeatureEngineer.compute_features` → `build_feature_dataframe` (AttributeError)
- **Bug 3 fixed:** `n_bars=60` → `300` (dist_sma200_pct z-score requires 163+ bars; 60 yielded empty feature matrix)
- HMM model loaded from disk (fresh, n_states=5) — no retrain triggered
- Regime "CRASH" at 100% confidence is a raw HMM state label; unconfirmed (1 bar < 3 required)
- Cross-enrichment: trading-bot log not mounted → safe defaults used (gate OPEN)
