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

## 2026-06-14 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Biggest Stock Market Rug Pull in History is Here. | HIGH_VOL → BEAR | ★★★ — explicit crash warning, systemic top signal |
| Real Vision Presents | Retail Is Going to Get REKT by These IPOs! | HIGH_VOL | ★★★ — IPO overhang risk, retail positioned wrong |
| Investing Simplified (Prof G) | SpaceX might break the ENTIRE Stock Market | HIGH_VOL risk catalyst | ★★ — SpaceX IPO as tail-risk event for indices |
| IG France (Alexandre Baradez) | IPO SpaceX : bulle de 1 750 milliards $ ? | HIGH_VOL | ★★ — $1.75T valuation bubble concern; broad mkt risk |
| IG France (Alexandre Baradez) | MarketLive ×4 (Jun 8–12) | MID_VOL / technicals | ★★★ — active chart analysis; no explicit transcript |
| Real Vision Presents | Alt Season Didn't Die, It Moved to AI | Risk-ON / QQQ positive | ★★ — speculative rotation into AI/tech, contradicts bear |
| Real Vision Presents | Discovering a Huge Copper Deposit | Commodity bull | ★ — copper long-term bull; IWM materials proxy |
| Investing Simplified (Prof G) | These Space ETFs Could 10x by 2030! | Speculative bull | ★ — longer-horizon; not actionable for HMM |
| Investing Simplified (Prof G) | 5 Laws Of Dividend ETF Placement | Defensive positioning | ★★ — income rotation signal; modest risk-off lean |
| Oseille TV | Tout est trop cher, l'IA détruit tout | Stagflation / HIGH_VOL | ★★ — cost-of-living + AI disruption; inflation narrative |
| Oseille TV | Euro numérique : l'Europe contrôle votre argent | Macro tail risk (EUR) | ★ — CBDC narrative; EUR capital flight theme |
| Oseille TV | Résidence fiscale : mythe des 183 jours | Wealth-mgmt | PRIORITY — tax emigration; UEMOA/diaspora relevant |
| Oseille TV | Quitter la France : ne laissez rien au fisc | Wealth-mgmt | PRIORITY — capital exit strategies |
| Oseille TV | Quitter la France en 2 mois | Wealth-mgmt | PRIORITY — accelerated expat playbook |
| Finary | La vraie vie des ultra-riches | Wealth-mgmt | ★ — private banking; wealth preservation case study |
| Finary | Comment la famille la plus riche de France a tout perdu | Wealth-mgmt | ★★ — concentration risk cautionary tale |
| Finary | De 0 à millionnaire en un an | Wealth-mgmt | ★ — accumulation story |

**Cross-channel consensus (3+ channels agree):** SpaceX IPO = near-term HIGH_VOL catalyst. Reduce size, widen stops.
