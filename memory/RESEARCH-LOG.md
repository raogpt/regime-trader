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

## 2026-05-19 — Pre-Market Regime Detection

### Account
- Equity: $105,596.03
- Cash: $-25,807.54
- Buying power: $79,788.49
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

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| — | — | — | — | — | — | CRASH not confirmed (1/3 bars) |

### Decision
**HOLD** — CRASH regime not yet confirmed (need 3 consecutive bars). No new entries.

### Anomalies / Warnings
- **CRASH confidence 100%**: HMM emitting maximum certainty on crash state. Atypical — warrants monitoring.
- **Negative cash -$25,807.54**: Open positions on margin exist (account equity $105,596.03 vs. baseline $100k). TRADE-LOG.md not yet updated to reflect live positions — investigate at market-open.
- **Model not retrained**: Loaded from disk (fresh < 7 days). No retrain triggered.

### Session Bootstrap Fixes Applied
- Switched Alpaca data feed SIP → IEX (free-tier paper account constraint)
- Fixed `engineer.compute_features` → `engineer.build_feature_dataframe` (method rename mismatch)
- Fixed `load_or_train_hmm(n_bars=60)` → `n_bars=settings.HMM_TRAINING_DAYS (504)` across all 3 call sites — 60 bars produced all-NaN features due to `_ZSCORE_WINDOW=252` and `sma200 min_periods=100`
