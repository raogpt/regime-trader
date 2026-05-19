# Research Log — regime_trader

Daily regime detection entries appended here.

---

## 2026-05-19 — Regime Detection

### Account
- Equity: $105,446.11
- Cash: -$63,382.86 (margin used)
- Open positions: 3 (SPY, QQQ, IWM)

### Regime Signal
- Detected regime: CRASH
- Confidence: 100.0%
- HMM states: 5 (crash/bear/neutral/bull/euphoria)
- Model: loaded from disk (fresh)
- Flickering: no

### ETF Snapshot (from Alpaca REST)
- SPY: $735.48 (current: $735.34)
- QQQ: $704.90 (current: $704.31)
- IWM: $273.23 (current: $273.08)

### Cross-Enrichment Signal (from trading-bot)
- Sizing modifier: 1.0x (no reduction applied)
- Regime gate: OPEN (confidence 100% ≥ 55% threshold)

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | BUY | 19 | 735.48 | 698.72 | 1.00 | HighVolDefensive: 60% invested, wider stop |
| QQQ | BUY | 11 | 704.90 | 643.10 | 1.00 | HighVolDefensive: 60% invested, wider stop |
| IWM | BUY | 58 | 273.23 | 265.31 | 1.00 | HighVolDefensive: 60% invested, wider stop |

### Decision
TRADE — all 3 orders filled on Alpaca paper account
