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

## 2026-06-10 — Regime Detection

### Account
- Equity: $108,717.64
- Cash: $-240,872.56 (positions already carried from prior sessions)
- Open positions: 3 (IWM 444 @ $279.17, QQQ 142 @ $699.41, SPY 166 @ $733.72)

### Regime Signal
- Detected regime: crash
- Confidence: 100.0%
- Consecutive bars: 1
- Confirmed: NO (< 3 bars required)
- Flickering: no

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: $734.47 (1d chg: -0.35%)
- QQQ: $704.27 (1d chg: -0.51%)
- IWM: $286.89 (1d chg: +0.68%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown
- Active earnings/catalyst risk: no
- Regime gate: OPEN

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | BUY | 22 | 734.82 | 716.75 | 1.00 | HighVolDefensive (60% size, 1× leverage) |
| QQQ | BUY | 23 | 705.05 | 672.27 | 1.00 | HighVolDefensive (60% size, 1× leverage) |
| IWM | BUY | 53 | 286.89 | 272.49 | 1.00 | HighVolDefensive (60% size, 1× leverage) |

### Decision
TRADE — **⚠️ WARNING: regime stability rule violated (1/3 bars)**
- Orders submitted before stability guard was added; affected runner has been patched
- Stability check added post-hoc; future runs will HOLD until 3 consecutive bars
