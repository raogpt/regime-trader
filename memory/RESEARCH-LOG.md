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

## 2026-05-07 — YouTube Intel

**Status: No new videos** — RSS fetch failed for all 7 channels (feedparser/requests unavailable; no outbound network in cloud session).

| Channel | Status | Note |
|---------|--------|------|
| Oseille TV | no new | RSS unavailable |
| Bravos Research | no new | RSS unavailable |
| Finary | no new | RSS unavailable |
| Investing Simplified (Prof G) | no new | RSS unavailable |
| George Gammon | no new | RSS unavailable |
| IG France (Alexandre Baradez) | no new | RSS unavailable |
| Real Vision Presents | no new | RSS unavailable |

- All channels were "never checked" (first run) → 7-day lookback applied
- Zero transcripts fetched; no regime signals extracted
- Timestamps NOT updated (no data ingested)
