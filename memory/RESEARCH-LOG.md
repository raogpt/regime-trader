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

## 2026-06-11 — Regime Detection

### Account
- Equity: $105,148.33
- Cash: $9,214.17
- Open positions: 3 (SPY 44 | QQQ 46 | IWM 112)

### Regime Signal
- Detected regime: BEAR
- Confidence: 100.0%
- Consecutive bars: N/A (HMM 5-state model, BIC=5330.30)
- Flickering: no

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: $726.84 | held 44 shares | P&L -$309.34
- QQQ: $697.77 | held 46 shares | P&L -$90.95
- IWM: $284.43 | held 112 shares | P&L +$586.70

### Cross-Enrichment Signal
- Regime gate: OPEN (no catalyst data from trading-bot)
- Sizing modifier: 1.0x (no conflict detected)

### Action Taken
- SELL SPY 122 @ $726.67 (reduced 166→44)
- SELL QQQ 96 @ $697.23 (reduced 142→46)
- SELL IWM 332 @ $284.64 (reduced 444→112)
- HighVolDefensiveStrategy: 60% target allocation, BEAR regime

### Decision
TRADE — reduced exposure to align with BEAR regime (60% allocation target)
