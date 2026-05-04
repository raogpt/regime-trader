# Research Log — regime_trader

Daily regime detection entries appended here.
Format:

## 2026-05-04 — Regime Detection

### Account
- Equity: $102,302.23
- Cash: ~$102,302.23 (pre-fill)
- Open positions: 0 (orders pending fill)

### Regime Signal
- Detected regime: CRASH
- Confidence: 100%
- Consecutive bars: confirmed (is_confirmed=True)
- Flickering: no

### ETF Snapshot (from Alpaca IEX feed)
- SPY: bar data fetched (300 bars), current ~near recent close
- QQQ: bar data fetched (300 bars)
- IWM: bar data fetched (300 bars)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown (RESEARCH-LOG not available to cross-enrichment)
- Active earnings/catalyst risk: no
- Regime gate: OPEN

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | BUY  | 18 | pending fill | 682.65 | 1.00 | CRASH regime, no catalyst gate |
| QQQ | BUY  | 11 | pending fill | 616.98 | 1.00 | CRASH regime, no catalyst gate |
| IWM | BUY  | 34 | pending fill | 259.96 | 1.00 | CRASH regime, no catalyst gate |

### Decision
TRADE — 3 BUY orders submitted (SPY 18, QQQ 11, IWM 34). Catalyst gate OPEN; CRASH regime with full confidence; sizing modifier 1.0x.

---

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
