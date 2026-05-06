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

## 2026-05-06 — Pre-Market Regime Detection

### Account
- Equity: $106,262.60
- Cash: $-102,287.48
- Buying power: $3,975.12
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
- **CRASH regime detected** (confidence 100%, 1 bar) — not confirmed (requires 3 consecutive bars). HOLD until stability condition met.
- Regime label "crash" is an internal HMM state label; maps to HIGH_VOL policy (60% allocation, wide stops). No trades until confirmed ≥3 bars.
- Cash negative ($-102,287.48) with equity $106,262.60 → net long position ~$208k already on books from prior sessions. Buying power only $3,975.
- **Runner fixes applied this session:** (1) added `feed=DataFeed.IEX` to SIP-restricted account; (2) renamed `compute_features` → `build_feature_dataframe`; (3) increased bar fetch from 60 → 252 to satisfy `sma200 min_periods=100`.
- No model retrain triggered — HMM loaded from disk (fresh, n_states=5).

### Decision
HOLD — regime unconfirmed (1/3 bars), buying power minimal.
