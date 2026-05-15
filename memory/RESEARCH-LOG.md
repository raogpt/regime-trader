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

---

## 2026-05-15 — Midday Scan

### Regime Signal
- Detected regime: **CRASH** (HIGH_VOL bucket)
- Confidence: **100.0%**
- Action: stops tightened on all open positions (IWM, QQQ, SPY); no cuts triggered

### Midday Actions
- IWM: stop tightened (HIGH_VOL/CRASH)
- QQQ: stop tightened (HIGH_VOL/CRASH)
- SPY: stop tightened (HIGH_VOL/CRASH)
- No positions cut (none at -7% threshold)

### Correlation Risk — Step 3
- **CRASH regime at 100% confidence** is a broad-market signal affecting all ETFs simultaneously
- If trading-bot is also in drawdown today (likely given market-wide CRASH): **cross-bot correlation risk is ELEVATED**
- Both bots hold SPY/QQQ/IWM exposure → correlated drawdown in a CRASH event is expected
- **Risk note:** Reduce sizing 50% on next entry signal per cross-bot conflict rule; do NOT add to existing positions while both bots are in HIGH_VOL/CRASH regime
