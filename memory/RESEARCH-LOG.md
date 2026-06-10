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

## 2026-06-10 — Pre-Market Regime Detection

### Account
- Equity: $105,712.82
- Cash: $-193,391.81
- Buying power: $63,925.72
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

### Open Positions (discovered this session)
| ETF | Qty | Avg Entry | Current | Mkt Value | Unreal P&L |
|-----|-----|-----------|---------|-----------|------------|
| IWM | 391L | $278.20 | $282.77 | $110,563 | +$1,787 |
| QQQ | 119L | $698.74 | $699.08 | $83,191 | +$41 |
| SPY | 144L | $733.73 | $731.27 | $105,303 | -$354 |
- **Total notional:** ~$299,057 on $105,713 equity = **2.83x leverage**

### Anomalies & Warnings
- ⚠️ CRASH regime at 100% confidence (1/3 bars — not yet confirmed)
- ⚠️ Account 2.83x leveraged long vs. CRASH regime signal — high risk if confirmed
- ⚠️ TRADE-LOG stale — positions pre-exist but were never logged (shows Day 0 baseline)
- ⚠️ Cross-enrichment sector_momentum=unknown — trading-bot RESEARCH-LOG not readable
- **CODE BUGS FIXED THIS SESSION:**
  - Alpaca data feed: SIP → IEX (SIP requires paid subscription)
  - `FeatureEngineer.compute_features` → `.build_feature_dataframe` (method name mismatch)
  - `load_or_train_hmm(n_bars=60)` → `n_bars=settings.HMM_TRAINING_DAYS` (60 bars too few for sma200/zscore warmup, produced 0 clean feature rows)

### Decision
HOLD — CRASH regime unconfirmed (1/3 bars). Monitor closely. If CRASH confirmed tomorrow, circuit breaker should trigger position reduction to max 5% notional per rule.
