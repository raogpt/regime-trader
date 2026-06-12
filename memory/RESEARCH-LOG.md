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

## 2026-06-12 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Biggest Stock Market Rug Pull in History is Here. | HIGH_VOL — strong bearish macro, correction imminent | ★★★ |
| Bravos Research | A Once in a Lifetime Economic Reset is Coming. | HIGH_VOL — systemic reset narrative, broad de-risking | ★★★ |
| Investing Simplified (Prof G) | 🚨BREAKING: Markets Are Starting to Crack | HIGH_VOL — retail-facing bear signal, widening cracks | ★★ |
| Investing Simplified (Prof G) | 5 Laws Of Dividend ETF Placement (SCHD, JEPI, JEPQ, SPYI) | LOW-MID_VOL — defensive dividend rotation, income focus | ★ |
| Real Vision Presents | Alt Season Didn't Die, It Moved to AI | MID_VOL — QQQ-positive rotation into AI/tech, selective risk-on | ★★ |
| Real Vision Presents | Retail Is Going to Get REKT by These IPOs! | HIGH_VOL — IPO froth warning, speculative excess signal | ★★★ |
| Real Vision Presents | The Real Opportunity Isn't What You Think! | NEUTRAL — contrarian framing, no transcript available | ★ |
| IG France (Baradez) | MarketLive 2026-06-12 (today) | NEUTRAL/MONITORING — daily technical analysis session | ★★★ |
| IG France (Baradez) | IPO SpaceX : bulle de 1 750 milliards $ ? | HIGH_VOL — speculative bubble warning, correction risk | ★★★ |
| IG France (Baradez) | MarketLive 2026-06-11, 06-09, 06-08, 06-05 | MONITORING — daily market analysis sessions | ★★★ |
| Oseille TV | Tout est trop cher, l'IA détruit tout | MID-HIGH_VOL — cost pressure + AI disruption, risk-off tone | ★★ |
| Oseille TV | Résidence fiscale : le mythe des 183 jours | WEALTH MGMT — tax residency rules, PRIORITY | ★★ |
| Oseille TV | Quitter la France : ne laissez rien au fisc | WEALTH MGMT — French exit tax strategy, PRIORITY | ★★ |
| Oseille TV | Aux USA 90% n'ont RIEN, 10% contrôlent TOUT | HIGH_VOL — US wealth inequality, political risk signal | ★★ |
| Oseille TV | La Chine se venge de 150 ans d'humiliation | HIGH_VOL — China geopolitical risk, risk-off catalyst | ★★ |
| Oseille TV | Pourquoi une partie du monde devient pro-Iran | HIGH_VOL — geopolitical fragmentation, EM risk-off | ★ |
| Oseille TV | L'État vous espionne : pire que Louis XIV ? | WEALTH MGMT — surveillance/CRS risk for expats | ★ |
| Finary | La vraie vie des ultra-riches (banquiers privés) | WEALTH MGMT — private banking structures, PRIORITY | ★★ |
| Finary | Comment la famille la plus riche de France a tout perdu | WEALTH MGMT — wealth preservation lessons, PRIORITY | ★★ |
| Finary | Ce français a trouvé comment éviter l'impôt sur le revenu à vie | WEALTH MGMT — lifetime tax optimization, PRIORITY | ★★ |

**Cross-channel consensus:** 3 high-signal channels (Bravos ★★★, Real Vision ★★★, Investing Simplified) converge on HIGH_VOL / risk-off. IG France (Baradez ★★★) providing daily market technical context. Regime bias: HIGH_VOL watchfulness warranted this week.
