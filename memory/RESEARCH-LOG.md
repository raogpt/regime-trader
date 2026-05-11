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

## 2026-05-11 — Pre-Market Regime Detection

### Account
- Equity: $107,910.89
- Cash: $-102,287.48
- Buying power: $5,623.41
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

### Open Positions (live)
| ETF | Qty | Avg Entry | Market Val | Unrealized PnL | PnL% |
|-----|-----|-----------|------------|----------------|------|
| SPY | 127 | $715.80 | $93,595 | +$2,688 | +2.96% |
| QQQ | 73  | $664.05 | $51,859 | +$3,383 | +6.98% |
| IWM | 228 | $275.90 | $64,743 | +$1,838 | +2.92% |
- Total long exposure: $210,197 (~1.95x equity leverage)

### Decision
**HOLD** — CRASH regime not confirmed (1/3 bars). No new entries. Monitor existing positions.

### Anomalies & Warnings
- **CRASH regime at 100% confidence**: HMM model (5-state) mapping crash/bear/neutral/bull/euphoria — "crash" is the highest-vol state. 100% confidence may indicate regime transition rather than gradual shift.
- **Negative cash $-102,287**: Account is 1.95x leveraged (long $210k on $108k equity). All 3 ETFs in profit. Risk: if CRASH confirms over 3 bars, will need to reduce sizing significantly (HighVolDefensiveStrategy: max 5% pos, cash preservation).
- **Confirmation not met**: 1/3 consecutive bars — HOLD by hard rule. Revisit at next bar.
- **No retrain triggered**: Model loaded from disk (fresh, < 7 days old).

### Session Fixes Applied
- Switched Alpaca data feed SIP → IEX (free-tier subscription limit)
- Fixed method name: `compute_features` → `build_feature_dataframe`
- Increased bar fetch: 60 → 300 bars (required for 252-day z-score min_periods=63)
