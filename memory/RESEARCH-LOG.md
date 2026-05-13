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

## 2026-05-13 — Regime Detection

### Account
- Equity: $106,922.11
- Cash: $-107,980.63 (NEGATIVE — fully margined)
- Buying power: $0.00
- Open positions: 3 (IWM 228sh @$275.90, QQQ 81sh @$668.75, SPY 127sh @$715.80)
- Total market value: ~$214,903 (~2x leveraged vs equity)

### Regime Signal
- Detected regime: CRASH
- Confidence: 100.0%
- Consecutive bars: 1 (UNCONFIRMED — needs 3)
- Confirmed: no
- Flickering: no

### ETF Snapshot (from Alpaca REST / IEX feed)
- SPY: $737.00 (1d chg: -0.16%)
- QQQ: $708.70 (1d chg: +0.21%)
- IWM: $280.37 (1d chg: -0.78%)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown (trading-bot RESEARCH-LOG not available in cloud)
- Active earnings/catalyst risk: no
- Sizing modifier: 1.0x
- Regime gate: OPEN

### Signals Generated (HighVolDefensiveStrategy — 30% per ETF in uncertainty mode)
| ETF | Side | Shares | Entry | Stop | Conf | Reason |
|-----|------|--------|-------|------|------|--------|
| SPY | LONG | ~43 | 737.00 | EMA50-ATR | 1.00 | High-vol defensive, 30% (halved, unconfirmed) |
| QQQ | LONG | ~45 | 708.70 | EMA50-ATR | 1.00 | High-vol defensive, 30% (halved, unconfirmed) |
| IWM | LONG | ~114 | 280.37 | EMA50-ATR | 1.00 | High-vol defensive, 30% (halved, unconfirmed) |

### Decision
HOLD — Orders attempted but failed: buying_power=$0 (account fully margined at ~2x leverage).
Regime unconfirmed (1 bar, needs 3). RISK FLAG: account carries -$107k cash / 2x gross leverage in CRASH regime.
