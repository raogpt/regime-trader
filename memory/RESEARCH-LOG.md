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

## 2026-06-15 — Pre-Market Regime Detection

### Account
- Equity: $110,136.98
- Cash: $-28,569.69
- Buying power: $274,099.92
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: STRONG_BEAR
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### ETF Snapshot (IEX feed, last close 2026-06-12)
- SPY: $741.67 (1d chg: +0.54%)
- QQQ: $721.31 (1d chg: +0.65%)
- IWM: $292.97 (1d chg: +0.87%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

### Open Positions (stale TRADE-LOG — synced here)
| ETF | Qty | Avg Entry | Mkt Val | Unrealized P&L |
|-----|-----|-----------|---------|----------------|
| IWM | 149 | $288.25 | $44,266 | +$1,318 |
| QQQ | 62 | $712.83 | $45,637 | +$1,442 |
| SPY | 65 | $739.08 | $48,799 | +$759 |

### Anomalies / Warnings
- TRADE-LOG was stale (showed "No positions" since launch baseline); synced above
- STRONG_BEAR regime detected but unconfirmed (1/3 bars) — all longs still open
- HMM retrained from scratch (no saved model); 60-bar training on 7-state HMM → multiple non-convergence warnings (tight sample, degenerate solution warning at n_states=7)
- Negative cash (-$28,570) = leveraged margin positions (~1.25x)
- Fix applied: episodic_runner.py switched to IEX feed (SIP subscription error); compute_features → build_feature_dataframe; fetch 250 bars for feature warmup

### Signals Generated
None — regime unconfirmed (1/3 consecutive bars required)

### Decision
HOLD — STRONG_BEAR signal emerging but needs 2 more confirming bars before action. Existing longs monitored. Next run (market-open/midday) will re-evaluate if regime persists.
