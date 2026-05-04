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

## 2026-05-04 — Pre-Market Regime Detection

### Account
- Equity: $101,265.74
- Cash: $-59,383.34
- Buying power: $41,882.40
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: CRASH
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### ETF Snapshot (IEX feed)
- SPY: $720.49 (1d chg: +0.29%)
- QQQ: $674.10 (1d chg: +0.97%)
- IWM: $279.30 (1d chg: +0.49%)

### Open Positions (pre-market)
- SPY: 91 shares @ avg $713.65 | mkt $65,247 | unrealized P&L +$306.14
- QQQ: 62 shares @ avg $662.13 | mkt $41,576 | unrealized P&L +$524.46
- IWM: 194 shares @ avg $275.20 | mkt $53,730 | unrealized P&L +$340.79

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| — | — | — | — | — | — | CRASH regime not confirmed (1/3 bars) |

### Decision
**HOLD** — CRASH regime detected but NOT confirmed (1 consecutive bar, need 3). No new entries. Existing positions monitored.

### Anomalies / HMM Warnings
- **CRASH label**: HMM 5-state model assigned "crash" (maps to HighVolDefensiveStrategy). Unusually decisive 100% confidence; may reflect genuine risk-off signal given negative cash/leveraged account.
- **100% confidence**: Suspiciously high — model may be in a degenerate attractor state. Watch for flickering on next bar.
- **Account leverage**: Cash = -$59,383 (margin in use). Total position value ≈ $160,554 across SPY/QQQ/IWM. Risk elevated if CRASH signal persists.
- **Bug fixes applied this session**: (1) SIP→IEX data feed fix; (2) `compute_features`→`build_feature_dataframe`; (3) `n_bars` 60→300 for z-score warmup.
- **Model**: Loaded from disk, age 0 days — no retrain triggered.
