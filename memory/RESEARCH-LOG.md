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

## 2026-05-26 — Regime Detection

### Account
- Equity: $113,204.01
- Cash: -$108,622.12 (leveraged)
- Open positions: 3 (SPY, QQQ, IWM — all LONG)

### Regime Signal
- Detected regime: BULL
- Confidence: 100.0%
- HMM: n_states=5, model fresh (loaded from disk)
- Flickering: no
- is_confirmed: yes

### ETF Snapshot (from Alpaca IEX feed)
- SPY: $749.92 (entry $729.51 | +$2,040 unreal.)
- QQQ: $725.43 (entry $691.47 | +$2,988 unreal.)
- IWM: $289.19 (entry $275.30 | +$3,984 unreal.)

### Cross-Enrichment Signal (from trading-bot)
- Sector momentum: unknown (cloud session — trading-bot path not mounted)
- Active earnings/catalyst risk: no (cross-enrichment unavailable)
- Regime gate: OPEN
- Sizing modifier: 1.0x (no sector conflict detected)

### Signals Generated
| ETF | Side | Direction | Stop | Conf | Reason |
|-----|------|-----------|------|------|--------|
| SPY | LONG | already held | ATR-based | 1.00 | BULL — LowVol/HighVol strategy |
| QQQ | LONG | already held | ATR-based | 1.00 | BULL — LowVol/HighVol strategy |
| IWM | LONG | already held | ATR-based | 1.00 | BULL — LowVol/HighVol strategy |

### Decision
HOLD — Already fully invested in BULL regime. No buying power for additional positions. All signals aligned with current holdings.
