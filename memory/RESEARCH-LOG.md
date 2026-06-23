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

## 2026-06-23 — YouTube Intel

**21 new videos across 7 channels. Transcripts unavailable (API blocked — title-based analysis).**

| Channel | Video | Regime Signal | Relevance |
|---------|-------|--------------|-----------|
| Oseille TV | Le prochain krach sera pire que 2008 | HIGH_VOL / BEARISH | ★★★ crash warning |
| Oseille TV | Le vrai prix de la liberté financière | Wealth mgmt | ★★ financial freedom |
| Oseille TV | L'IA va supprimer 300M d'emplois | Macro / AI disruption | ★★ labor risk |
| Oseille TV | 20 ans à 0% d'impôts : Erdogan | Expat tax strategy | ★★★ UEMOA priority |
| Oseille TV | La sélection par la bêtise (Attali) | Neutral societal | ★ |
| Oseille TV | Ces métiers bizarres 200k€/an | Career content | ★ |
| Oseille TV | Entrepreneuriat : écoutez le marché | Entrepreneurship | ★ |
| Bravos Research | The Biggest Trap in Financial History Has Just Been Set. | HIGH_VOL / EXTREME RISK-OFF | ★★★ macro danger |
| Finary | Médecin millionnaire sans héritage | Wealth mgmt case study | ★★★ UEMOA priority |
| Finary | Investissement avec 1M€ à placer | HNW allocation | ★★★ portfolio strategy |
| Investing Simplified | Best Fidelity Funds to Buy and Hold FOREVER | LOW_VOL passive | ★★ index ETF |
| Investing Simplified | 6 Stocks Could PRINT Millions Soon | Risk-ON (individual stocks) | ★ out of scope |
| George Gammon ★★★ | New Fed Changed Everything (Interest Rates) | **HIGH PRIORITY** Fed regime shift | ★★★ HMM input |
| George Gammon ★★★ | SpaceX, Iran, OpenAI IPO Strategy 2026 | Geopolitical macro | ★★ context |
| IG France ★★★ | MarketLive graphiques 2026-06-22 | Technical chart analysis | ★★★ most recent |
| IG France ★★★ | MarketLive graphiques 2026-06-19 | Technical chart analysis | ★★★ |
| IG France ★★★ | MarketLive graphiques 2026-06-18 | Technical chart analysis | ★★ |
| IG France ★★★ | 3 façons d'acheter SpaceX IG | Product content | ★ |
| Real Vision ★★★ | The End Goal for Binance Is Much Bigger | Crypto institutional | ★★ liquidity context |
| Real Vision ★★★ | Binance CEO on Future of Blockchain | Crypto/regulatory | ★★ |

**Cross-channel consensus:** MID→HIGH_VOL lean. 2 channels (Oseille TV + Bravos Research) publish explicit crash/trap warnings. George Gammon flags Fed policy change. IG France ran 4 MarketLive sessions in one week = elevated market attention. Real Vision crypto focus = mild risk-on undercurrent (offsetting). Net: **defensive posture warranted, await HMM confirmation before acting.**

Full analysis: reports/2026-06-23-youtube-intel.md
