# Research Log — regime_trader

Daily regime detection entries appended here.

---

## 2026-05-07 — Regime Detection

### Account
- Equity: $106,971
- Cash: -$102,287 (margin)
- Open positions: 3 (SPY 127, QQQ 73, IWM 228)

### Regime Signal
- Detected regime: **CRASH**
- Confidence: **100%**
- Consecutive bars: <3 (is_flickering=True — not yet confirmed stable)
- Flickering: yes (regime.is_confirmed check failed)

### ETF Snapshot (from Alpaca IEX)
- SPY: ~$734 (latest bar)
- QQQ: ~$697 (latest bar)
- IWM: ~$286 (latest bar)

### Cross-Enrichment Signal (from trading-bot)
- Sizing modifier: 1.0 (default — trading-bot signal unavailable)
- Catalyst gate: False
- Regime gate: OPEN (confidence > 55%)

### Signals Generated
- CRASH regime signals generated for SPY, QQQ, IWM
- All BUY orders rejected: insufficient buying power (account over-leveraged at ~1.95×)

### Decision
**HOLD** — buying power exhausted by existing positions from prior sessions
