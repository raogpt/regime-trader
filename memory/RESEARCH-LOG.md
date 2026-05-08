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

## 2026-05-08 — Pre-Market Regime Detection

### Account
- Equity: $106,679.42
- Cash: $-102,287.48
- Buying power: $4,391.94
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

### Open Positions (Alpaca)
| ETF | Qty | Side | Avg Entry | Unrealized P&L |
|-----|-----|------|-----------|----------------|
| IWM | 228 | LONG | $275.90   | +$1,664.91     |
| QQQ | 73  | LONG | $664.05   | +$2,589.89     |
| SPY | 127 | LONG | $715.80   | +$2,438.01     |

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| -   | -    | -      | -     | -    | -    | HOLD — regime unconfirmed (1/3 bars) |

### Decision
**HOLD** — CRASH regime detected (HIGH_VOL class) but unconfirmed (1 consecutive bar; requires 3). No new entries. Existing longs monitored.

### Anomalies & Warnings
- HMM state "crash" (5-state model) — maps to HIGH_VOL_LABELS; 100% confidence unusual; watch for mean-reversion next bar
- Existing LONG positions (IWM/QQQ/SPY) pre-date TRADE-LOG; not entered by this bot session — verify stop levels at market-open
- Cross-enrichment signal unavailable (trading-bot RESEARCH-LOG not mounted in this environment)
- TRADE-LOG shows Day 0 baseline (no positions) but Alpaca reports 3 open longs — TRADE-LOG out of sync; see below

### Runner Fixes Applied (session bugs)
- `episodic_runner.py`: SIP → IEX data feed (paper account lacks SIP subscription)
- `episodic_runner.py`: `compute_features` → `build_feature_dataframe` (method name mismatch)
- `episodic_runner.py`: `n_bars=60` → `settings.HMM_TRAINING_DAYS` (504) at all call sites (60 bars insufficient for SMA200/zscore features)

### Model Status
- HMM loaded from disk (fresh — no retrain required)
- n_states=5 | labels include: crash, bear, bull, etc.
- Last retrain: within 7 days (model_is_fresh=True)
