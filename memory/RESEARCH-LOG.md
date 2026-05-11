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

## 2026-05-11 — Regime Detection

### Account
- Equity: $108,409
- Cash: -$107,981 (2× leveraged)
- Open positions: 3 (SPY 127sh, QQQ 81sh, IWM 228sh)

### Regime Signal
- Detected regime: CRASH
- Confidence: 100%
- Consecutive bars: 1
- Flickering: no
- Confirmed: NO (< 3 bars required)

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: $737.89 (1d chg: +0.05%)
- QQQ: $712.00 (1d chg: +0.12%)
- IWM: $285.20 (1d chg: +0.36%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Active earnings/catalyst risk: no
- Regime gate: OPEN

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| QQQ | BUY | 8 | 711.64 | 629.04 | 1.00 | crash (vol-rank strategy) |
| SPY | SKIP | — | — | — | — | insufficient buying power |
| IWM | SKIP | — | — | — | — | insufficient buying power |

### Decision
TRADE (QQQ only — regime stability check was missing; bug fixed post-execution)

**Issues found and fixed:**
- BUG FIXED: stability gate (is_confirmed / consecutive_bars ≥ 3) was absent from market-open flow — now added
- QQQ fill-tracker showed 0/0 due to paper-order timing lag; Alpaca order history confirms 8 shares filled @ $711.64
- CRASH regime generating BUY signal is expected behavior (vol-rank strategy assignment); CRASH = highest vol → most aggressive strategy slot. May need future review.
