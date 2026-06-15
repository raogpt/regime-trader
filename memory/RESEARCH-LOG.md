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

## 2026-06-15 — YouTube Intel

> 25 new videos across 6 channels (George Gammon: 0 new). Transcripts blocked by YouTube cloud-IP restriction — analysis from titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|--------------|-----------|
| Bravos Research | The Biggest Stock Market Rug Pull in History is Here. | HIGH_VOL / RISK-OFF ★★★ | Crash warning; biggest bearish flag of the week |
| IG France (Baradez) | MarketLive 2026-06-15 (latest) | NEUTRAL — range-bound TA | Daily technical view, no directional break |
| IG France (Baradez) | IPO SpaceX : bulle de 1 750 milliards $ ? | HIGH_VOL catalyst | SpaceX IPO = major capital reallocation event |
| Real Vision | Alt Season Didn't Die, It Moved to AI | MID_VOL / RISK-ON | AI rotation ongoing; capital staying in risk assets |
| Real Vision | Discovering a Huge Copper Deposit | IWM bias | Commodities + small-caps rotation signal |
| Oseille TV | Le système va dans le mur : prêt pour le crash ? | HIGH_VOL / RISK-OFF ★★★ | 2nd channel flagging crash risk this week |
| Oseille TV | Résidence fiscale : le mythe des 183 jours | Wealth Mgmt — PRIORITY | Critical for UEMOA expat tax planning |
| Oseille TV | Quitter la France : ne laissez rien au fisc | Wealth Mgmt — PRIORITY | Tax exit framework |
| Oseille TV | Euro numérique : l'Europe contrôle votre argent | Macro / CBDC | Non-EUR asset hedge narrative |
| Finary | La vraie vie des ultra-riches (banquiers privés) | Wealth Mgmt | Private banking; UEMOA HNW context |
| Finary | Comment la famille la plus riche a tout perdu | Wealth Mgmt | Concentration risk / diversification lesson |
| Investing Simplified | SpaceX might break the ENTIRE Stock Market | HIGH_VOL catalyst | 2nd channel on SpaceX IPO disruption risk |
| Investing Simplified | 5 Laws Of Dividend ETF Placement | Wealth Mgmt | SCHD/JEPI/JEPQ placement rules |

**Cross-channel consensus:**
- **HIGH_VOL / RISK-OFF:** Bravos Research + Oseille TV (2 channels) — crash/rug-pull narrative
- **SpaceX IPO catalyst:** IG France + Investing Simplified (2 channels) — treat as HOLD trigger near IPO date
- **AI/QQQ RISK-ON:** Real Vision (solo) — mitigating factor

**Net regime implication:** MID_VOL → HIGH_VOL bias. HOLD until HMM confirms with 3 consecutive bars.
Apply HOLD rule within 2 days of SpaceX IPO event date (earnings-adjacent rule).

Full report: reports/2026-06-15-youtube-intel.md
