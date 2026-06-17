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

## 2026-06-17 — YouTube Intel

22 new videos across 6 channels (7 days lookback). George Gammon: no new content.
Transcripts unavailable (cloud restriction) — analysis from titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research ★★★ | Brace Yourself. | HIGH_VOL warning | HIGH |
| Bravos Research ★★★ | The Biggest Stock Market Rug Pull in History is Here. | Extreme bearish / HIGH_VOL | HIGH |
| Oseille TV | Le système va dans le mur : prêt pour le crash ? | Crash warning / HIGH_VOL | HIGH |
| Oseille TV | Exit tax : l'impôt qui taxe des gains fictifs | Wealth-mgmt / exit tax | PRIORITY |
| Oseille TV | Quitter la France en 2 mois | Expat / tax optimization | PRIORITY |
| Oseille TV | Euro numérique : l'Europe contrôle votre argent | Capital controls / defensive | MED |
| Oseille TV | Tout est trop cher, l'IA détruit tout | Stagflation / HIGH_VOL | MED |
| Oseille TV | L'IA crée deux castes : maîtres et esclaves | AI disruption / structural | LOW |
| Oseille TV | L'État vous espionne : pire que Louis XIV ? | Geopolitical | LOW |
| Oseille TV | Pourquoi une partie du monde devient pro-Iran | Geopolitical / energy | LOW |
| Finary | De 0 à millionnaire en un an. Mais il a un problème. | Wealth-mgmt / concentration risk | MED |
| Finary | La vraie vie des ultra-riches (banquiers privés) | Private banking / UEMOA HNW | MED |
| Finary | Les dépenses folles de Mike Tyson | Behavioral finance | LOW |
| Investing Simplified (Prof G) | Best Fidelity Funds to Buy and Hold FOREVER | Defensive ETF / passive | MED |
| Investing Simplified (Prof G) | SpaceX might break the ENTIRE Stock Market | IPO catalyst risk / HIGH_VOL | MED |
| Investing Simplified (Prof G) | These Space ETFs Could 10x by 2030! | Risk-on growth / QQQ | LOW |
| IG France (Baradez) ★★★ | MarketLive x4 (Jun 11, 12, 15, 17) | MID→HIGH_VOL (4 active sessions) | HIGH |
| Real Vision ★★★ | Discovering a Huge Copper Deposit | Commodities / IWM signal | MED |
| Real Vision ★★★ | Alt Season Didn't Die, It Moved to AI | Risk-on AI / QQQ | LOW |

**Cross-channel consensus**: Bravos Research + Oseille TV (2 ★★★ channels) both explicit on crash/HIGH_VOL risk. No bullish continuation call from any channel.
**Regime lean**: HIGH_VOL or MID_VOL top. SPY defensive, QQQ mixed, IWM copper bid vs. risk-off vulnerability.
**Catalyst watch**: SpaceX IPO date → apply 2-day pre-event HOLD rule when announced.
**Wealth mgmt**: Exit tax + euro numérique + UEMOA expat content = action items. See full report: reports/2026-06-17-youtube-intel.md
