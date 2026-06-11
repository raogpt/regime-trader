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

## 2026-06-11 — YouTube Intel

**24 new videos across 6 channels | 0 transcripts (first run — all channels were "never checked")**

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | A Once in a Lifetime Economic Reset is Coming. | **HIGH_VOL** — structural reset thesis | ★★★ HIGH |
| Investing Simplified (Prof G) | Markets Are Starting to Crack | **HIGH_VOL** — broad equity crack warning | ★★★ HIGH |
| Real Vision Presents | Retail Is Going to Get REKT by These IPOs! | **HIGH_VOL** — IPO excess / risk-off | ★★★ HIGH |
| Real Vision Presents | Alt Season Didn't Die, It Moved to AI | Narrow risk-on (AI), late-cycle excess | ★★ MED |
| IG France (Baradez) | IPO SpaceX : bulle de 1 750 milliards $ ? | Speculative excess warning | ★★ MED |
| Investing Simplified (Prof G) | 5 Laws Of Dividend ETF Placement | Defensive rotation signal | ★★ MED |
| Oseille TV | Tout est trop cher, l'IA détruit tout | Stagflation / AI disruption backdrop | ★★ MED |
| Oseille TV | La Chine se venge de 150 ans d'humiliation | Geopolitical HIGH_VOL catalyst | ★★ MED |
| Oseille TV | Pourquoi une partie du monde devient pro-Iran | Geopolitical tail risk | ★ LOW |
| Finary | Comment la famille la plus riche de France a tout perdu | Wealth preservation / risk-off lesson | ★ LOW |
| IG France (Baradez) | MarketLive x6 daily sessions (Jun 4–11) | Daily TA — no transcript, neutral | — |
| Oseille TV | Résidence fiscale : mythe des 183 jours | Tax/legal info — wealth mgmt priority | WEALTH |
| Oseille TV | Quitter la France : ne laissez rien au fisc | Exit tax optimization — wealth mgmt | WEALTH |
| Finary | Ce français a trouvé comment éviter l'impôt à vie | Legal tax structuring | WEALTH |
| Finary | La vraie vie des ultra-riches (banquiers privés) | HNW banking strategies | WEALTH |

**Cross-channel consensus:** 3 channels (Bravos, Prof G, Real Vision) → **MID→HIGH_VOL transition risk**. No low-vol consensus.  
**ETF bias:** SPY defensive preferred. QQQ mixed (AI tailwind vs. crack risk). IWM not mentioned — neutral.  
**Full report:** reports/2026-06-11-youtube-intel.md
