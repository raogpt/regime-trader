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

## 2026-05-12 — Pre-Market Regime Detection

### Account
- Equity: $107,918.81
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

### Decision
HOLD — regime unconfirmed (1/3 bars required)

### Anomalies / Warnings
- **CRASH regime at 100% confidence** — HMM state labeled "crash" maps to HIGH_VOL behavior; with only 1 bar not actionable
- **Buying power = $0.00** — account fully deployed or margin exhausted; verify open positions before market-open
- **Negative cash ($-107,980.63)** — leveraged or margin positions exist; monitor closely
- Runner bugs fixed this session: (1) SIP data → switched to IEX feed; (2) `compute_features` → `build_feature_dataframe`; (3) n_bars=60 → 350 to satisfy _ZSCORE_WINDOW=252

### Model Status
- HMM model age: 1.0 days (last retrained 2026-05-11) — fresh, no retrain triggered
