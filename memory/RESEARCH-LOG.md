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

## 2026-07-08 — YouTube Intel
18 new videos across 6/7 channels. Transcript fetch blocked by YouTube IP ban on cloud infra for 17/18 (titles only, low confidence). Full report: reports/2026-07-08-youtube-intel.md

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| IG France (Baradez) | MarketLive 07/07 (full transcript) | Asian tech sell-the-news (Samsung/SK Hynix), rising EU/US 10Y yields, new Fed chair "Kevin W" gave no forward guidance → mild risk-off tilt, vol creeping up | High |
| George Gammon | "Are We On The Brink Of Another Financial Crisis?" | Title-only: crash/high-vol warning framing | Med (★★★ channel, unverified) |
| George Gammon | "Powerful Stock Indicator Just Gave An Extreme Crash Warning" | Title-only: crash warning | Med (★★★ channel, unverified) |
| Bravos Research | "Something Just Broke in the Financial System..." | Title-only: risk-off/systemic-stress framing | Med (unverified) |
| IG France (Baradez) | "Le Japon sous haute surveillance" | Title-only: yen weakness, BOJ, inflation — JPY/vol watch | Low-Med (unverified) |
| Oseille TV (x6) | Assurance-vie Luxembourg vs France, CBDC, impôt, expat | No regime signal — wealth-mgmt/tax content | Wealth-mgmt only |
| Finary (x2) | PEA concentration risk, money mistakes | No regime signal — wealth-mgmt/budgeting | Wealth-mgmt only |
| Investing Simplified (x3) | Retirement portfolio, "Bible money truths" | No regime signal — retail investing content | Low |
| IG France (Baradez) | "Ce qui fait la différence en trading" | No regime signal — trading psychology | Low |
