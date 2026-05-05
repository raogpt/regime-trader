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

## 2026-05-05 — Pre-Market Regime Detection

### Account
- Equity: $102,365.88
- Cash: $-89,289.86
- Buying power: $13,076.02
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

### ETF Snapshot (from Alpaca REST — IEX feed)
- SPY: $718.67 (avg_entry $714.76, unrl P&L +$625)
- QQQ: $676.58 (avg_entry $664.05, unrl P&L +$915)
- IWM: $279.47 (avg_entry $275.90, unrl P&L +$814)

### Positions
| ETF | Side | Qty | Avg Entry | Mkt Val | Unrl P&L |
|-----|------|-----|-----------|---------|----------|
| IWM | LONG | 228 | $275.90 | $63,719 | +$814 |
| QQQ | LONG | 73 | $664.05 | $49,390 | +$915 |
| SPY | LONG | 109 | $714.76 | $78,535 | +$625 |
| **Total** | | | | **$191,644** | **+$2,354** |

**Leverage: 1.87x** (equity $102,366)

### Anomalies / Warnings
- ⚠️ REGIME LABEL: Engine uses 5-state vocab (crash/bear/neutral/bull/euphoria), not LOW_VOL/MID_VOL/HIGH_VOL as documented in PROJECT-CONTEXT.md — doc mismatch, no functional impact
- ⚠️ CRASH REGIME at 100% confidence — most bearish state (expected_vol=50%, strategy=cash, max_pos=5%)
- ⚠️ HIGH LEVERAGE RISK: 1.87x long exposure while crash signal active. Max allowed in crash = 5% pos = ~$5,118. Current exposure = $191,644
- ⚠️ IEX feed used (SIP subscription not available) — data may lag SIP by ~15 min
- ℹ️ Model age: 1 day (loaded from disk, no retrain triggered)
- ℹ️ Regime unconfirmed: 1 of 3 consecutive bars required → HOLD today

### Decision
**HOLD** — Crash regime detected but NOT yet confirmed (1/3 consecutive bars). Hard rule: regime must be stable 3 bars before acting. Will monitor daily. If crash persists through 2026-05-07, reduction plan activates.
