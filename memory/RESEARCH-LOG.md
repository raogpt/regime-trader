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

## 2026-06-16 — YouTube Intel

**24 new videos | 6 channels | 1 channel with no update (George Gammon)**
**Transcripts:** Unavailable in cloud env; analysis from titles + channel thesis

| Channel | Video | Regime Signal | Relevance |
|---------|-------|--------------|-----------|
| Bravos Research ★★★ | The Economy is About to Witness the UNTHINKABLE. (Jun 15) | HIGH VOL / macro tail-risk | High |
| Bravos Research ★★★ | The Biggest Stock Market Rug Pull in History is Here. (Jun 11) | EXTREME risk-off / distribution | High |
| Oseille TV | Le système va dans le mur: prêt pour le crash? (Jun 15) | HIGH VOL crash narrative | Medium-High |
| Oseille TV | Exit tax: l'impôt qui taxe des gains fictifs (Jun 16) | EU capital flight / exit planning | Wealth Mgmt PRIORITY |
| Oseille TV | Euro numérique: l'Europe contrôle votre argent (Jun 13) | Capital control risk, EUR bearish | Wealth Mgmt |
| Oseille TV | Résidence fiscale: le mythe des 183 jours (Jun 9) | Tax residency planning | Wealth Mgmt |
| Finary | Comment la famille la plus riche de France a tout perdu (Jun 9) | Wealth destruction / cautionary | Medium |
| Prof G | SpaceX might break the ENTIRE Stock Market (Jun 13) | QQQ systemic IPO catalyst risk | Medium |
| Prof G | 5 Laws Of Dividend ETF Placement SCHD JEPI JEPQ SPYI (Jun 9) | Defensive rotation | Medium |
| Real Vision ★★★ | Alt Season Didn't Die, It Moved to AI (Jun 10) | Risk-on AI rotation | Medium |
| Real Vision ★★★ | Discovering a Huge Copper Deposit (Jun 13) | Commodities bullish | Low-Medium |
| IG France ★★★ | MarketLive x4 (Jun 9,11,12,15) | Technical market surveillance | Medium |

**Cross-channel consensus:** 3/6 channels RISK-OFF (Bravos ★★★, Oseille TV, Finary). Minority risk-on from Real Vision (copper + AI rotation). HMM implication: MID→HIGH VOL caution warranted. SpaceX IPO = latent QQQ catalyst. George Gammon silence = mild neutral.

**Wealth Mgmt priority (Oseille TV):** Exit tax, 183-day residency myth, Euro numérique capital control risk, France departure in 2 months. Full wealth mgmt section in reports/2026-06-16-youtube-intel.md.
