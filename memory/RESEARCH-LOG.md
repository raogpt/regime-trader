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

## 2026-04-30 — Pre-Market Regime Detection

### Account
- Equity: $99,790.66
- Cash: $5,213.88
- Buying power: $105,004.54
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

## 2026-04-30 — Anomalies & HMM Warnings

### Bugs Fixed (pre-market bootstrap)
1. **IEX feed missing** — Alpaca SIP data 403 on free tier. Fixed: `feed=DataFeed.IEX` in `fetch_daily_bars`.
2. **Method name mismatch** — `compute_features` → `build_feature_dataframe` (FeatureEngineer API).
3. **Insufficient bars** — `n_bars=60` produced empty feature matrix; `_ZSCORE_WINDOW=252` with `min_periods=63` requires ≥63 bars. Fixed: all modes now use `HMM_TRAINING_DAYS=504`.
4. **Hardcoded git branch** — `git push origin main` failed on feature branch. Fixed: dynamically detect current branch.

### Position Anomaly
- **3 open long positions discovered not in TRADE-LOG** (IWM 111sh, QQQ 38sh, SPY 55sh)
- Likely entered by prior session(s) Apr 27-29 before episodic_runner bugs were resolved
- Retroactively logged in TRADE-LOG.md

### Regime Warning
- CRASH state detected at 100% confidence — but only 1 consecutive bar
- Rule: 3 bars required before acting → **HOLD on new entries**
- All 3 positions are LONG — conflict with CRASH regime if confirmed tomorrow
- Watch: if CRASH confirms Day 2 (2026-05-01), review stops aggressively
- No retrain triggered (model age <7 days, loaded from disk, n_states=5)

### Cross-Enrichment
- trading-bot RESEARCH-LOG not mounted (cloud env) — defaults used
- Catalyst gate: OPEN | Sizing modifier: 1.0x

### Decision: HOLD
