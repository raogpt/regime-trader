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

## 2026-06-13 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|--------------|-----------|
| Bravos Research | The Biggest Stock Market Rug Pull in History is Here. | HIGH_VOL / Bearish | ★★★ macro signal |
| Investing Simplified | 🚨BREAKING: Markets Are Starting to Crack | HIGH_VOL / Bearish | ★★ corroborates Bravos |
| Real Vision Presents | Alt Season Didn't Die, It Moved to AI | Risk-on AI rotation | ★★ QQQ/tech bias |
| Real Vision Presents | Retail Is Going to Get REKT by These IPOs! | Caution / crowding risk | ★★ IPO bubble warning |
| IG France (Baradez) | MarketLive x5 + SpaceX IPO bubble $1.75T | MID→HIGH_VOL / bubble caution | ★★★ technical + macro |
| Oseille TV | Résidence fiscale : le mythe des 183 jours | WEALTH MGMT PRIORITY | tax-residency strategy |
| Oseille TV | Quitter la France : ne laissez rien au fisc | WEALTH MGMT PRIORITY | exit-tax, asset protection |
| Oseille TV | Tout est trop cher, l'IA détruit tout | MID_VOL / structural stress | ★ macro backdrop |
| Oseille TV | La Chine se venge de 150 ans d'humiliation | HIGH_VOL risk / geopolitics | ★★ macro tail-risk |
| Finary | Le métier français qui exonère d'impôt à vie | WEALTH MGMT PRIORITY | French tax exemption |
| Finary | La vraie vie des ultra-riches (banquiers privés) | WEALTH MGMT | private banking allocation |
| Investing Simplified | These Space ETFs Could 10x by 2030! | Risk-on speculative | ★ QQQ adjacent |
| Investing Simplified | 5 Laws Of Dividend ETF Placement (SCHD, JEPI…) | Defensive income tilt | ★ positioning insight |

**Cross-channel consensus (2+ channels):** HIGH_VOL / bearish lean — Bravos + Investing Simplified + Real Vision all flag market stress / crack signals. Pair with Baradez MarketLive for technical confirmation. Regime bias → HIGH_VOL or MID→HIGH transition. Reduce sizing 50% per conflict rule if sector momentum misaligned.

**Note:** Transcripts unavailable (IP-blocked in cloud environment). Analysis derived from titles + channel category knowledge.
