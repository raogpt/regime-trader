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

## 2026-06-04 — Regime Detection

### Account
- Equity: $113,994.55
- Buying power: $10,749.25 (account ~91% deployed)
- Open positions: existing (pre-loaded from prior sessions)

### Regime Signal
- Detected regime: BULL
- Confidence: 100%
- Consecutive bars: confirmed (is_confirmed=True)
- Flickering: no

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: $752.23 (1d chg: -0.26%)
- QQQ: $735.17 (1d chg: -1.21%)
- IWM: $288.12 (1d chg: +0.15%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unavailable (cloud env — local path not present)
- Active earnings/catalyst risk: no
- Regime gate: OPEN (default — no local trading-bot log)

### Signals Generated
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | LONG | — | 752.23 | ATR-based | 1.00 | BULL regime |
| QQQ | LONG | — | 735.17 | ATR-based | 1.00 | BULL regime |
| IWM | LONG | — | 288.12 | ATR-based | 1.00 | BULL regime |

### Decision
HOLD — account already ~91% deployed; all BUY orders rejected (insufficient buying power $10,749 vs $16k+ needed per position). No new capital to deploy.
