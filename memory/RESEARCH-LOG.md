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

## 2026-05-13 — Pre-Market Regime Detection

### Account
- Equity: $108,278.64
- Cash: $-107,980.63
- Buying power: $298.01
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

### Open Positions
| ETF | Shares | Avg Entry | Mkt Value | Unrealized P&L |
|-----|--------|-----------|-----------|----------------|
| IWM | 228 | $275.90 | $64,567.32 | +$1,662.63 |
| QQQ | 81 | $668.75 | $57,722.22 | +$3,553.27 |
| SPY | 127 | $715.80 | $93,967.30 | +$3,060.31 |
| **Total** | — | — | **$216,256.84** | **+$8,276.21** |

### Decision
**HOLD** — CRASH regime unconfirmed (1/3 bars). Awaiting confirmation per hard rule (3 consecutive bars required). No new entries. Existing positions held.

### Anomalies & Warnings
- **CRASH regime @ 100% confidence** — model's most bearish state (expected return: -25%, vol: 50%). Recommends full cash. Positions currently 2x leveraged (~$216k on $108k equity).
- **Unconfirmed (1 bar)** — Hard rule enforced: no action until 3 consecutive CRASH bars. Watch closely at market-open.
- **Negative cash** ($-107,980.63) — Portfolio fully deployed on margin from prior sessions. Buying power critically low ($298).
- **Data feed fix applied** — IEX feed substituted for SIP (subscription limit). Model was trained under SIP data; regime labels may drift slightly.
- **n_bars fix applied** — Pre-market bar fetch increased from 60 → 300 to satisfy z-score lookback (min 163 bars required). Prior sessions with n_bars=60 would have failed silently.
- **Model age: 2 days** (trained 2026-05-11) — Within 7-day window, no retrain triggered.
