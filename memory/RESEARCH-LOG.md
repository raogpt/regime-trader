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

## 2026-06-07 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|

- **Status:** No new videos — RSS fetch skipped (feedparser/requests unavailable in network-restricted cloud env)
- **Channels checked:** Oseille TV, Bravos Research, Finary, Investing Simplified (Prof G), George Gammon, IG France (Alexandre Baradez), Real Vision Presents
- **All channels:** Last checked = never → 7-day lookback window attempted, 0 results returned
- **Action:** No regime signals extracted. HOLD bias maintained pending next successful fetch.
