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

## 2026-06-05 — Pre-Market Regime Detection

### Account
- Equity: $114,810.59
- Cash: $-108,622.12
- Buying power: $12,376.94
- Status: AccountStatus.ACTIVE

### Regime Signal
- Detected regime: BULL
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: False
- Flickering: False

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Catalyst gate active: False
- Sizing modifier: 1.0
- Regime gate: OPEN

### ETF Snapshot (from Alpaca REST — open positions)
- SPY: 100 shares @ $754.33 mkt, avg entry $729.51, unrealized +$2,482
- QQQ: 88 shares @ $734.03 mkt, avg entry $691.47, unrealized +$3,745
- IWM: 287 shares @ $290.61 mkt, avg entry $275.30, unrealized +$4,393

### Anomalies / Warnings
- **HMM label mismatch**: model returns "bull/bear" labels, not LOW_VOL/MID_VOL/HIGH_VOL — model was pre-trained with different state naming; regime_strategies.py mapping may need review
- **Regime unconfirmed**: 1/3 consecutive bars — HOLD, no new entries per rules
- **High leverage**: ~1.95x ($223k exposure on $114k equity), cash deeply negative
- **Startup fixes applied**: installed deps (numpy, pandas, hmmlearn, alpaca-py, python-dotenv); fixed IEX feed (SIP subscription not available); fixed feature method name; increased bar fetch 60→300 (SMA200 requires min 100 bars)

### Decision
**HOLD** — regime not confirmed (1 consecutive bar, need 3). Existing positions maintained.
