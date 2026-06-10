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

## 2026-06-10 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | A Once in a Lifetime Economic Reset is Coming | HIGH_VOL — systemic reset narrative | ★★★ Macro |
| Investing Simplified (Prof G) | Markets Are Starting to Crack (Huge Stock Update) | HIGH_VOL — crack signal, risk-off | ★★★ Regime |
| Investing Simplified (Prof G) | 5 Laws Of Dividend ETF Placement (SCHD, JEPI, JEPQ, SPYI) | Defensive rotation into income ETFs | ★★ Allocation |
| Investing Simplified (Prof G) | The AI & Quantum Boom Is Just Starting | MID_VOL risk-on QQQ bias | ★★ Signal |
| Real Vision Presents | Retail Is Going to Get REKT by These IPOs! | Risk-off — retail warning, IPO bubble | ★★★ Regime |
| Real Vision Presents | The Real Opportunity Isn't What You Think! | Contrarian — possibly risk-on rotation | ★★ Signal |
| Real Vision Presents | A New Frontier in Gold Exploration | Defensive — commodities/gold preference | ★★ Signal |
| IG France (Baradez) | MarketLive sessions (×5, Jun 3–9) | Daily TA — elevated market attention | ★★ Regime |
| IG France (Baradez) | IPO SpaceX: bulle de 1 750 milliards? | Bubble warning — risk elevated | ★★★ Macro |
| Oseille TV | La Chine se venge de 150 ans d'humiliation | Geopolitical risk — tariff/trade tension | ★★ Macro |
| Oseille TV | Résidence fiscale : le mythe des 183 jours | Tax residency myth debunked | ★★★ Wealth |
| Oseille TV | Quitter la France : ne laissez rien au fisc | France exit / tax optimization | ★★★ Wealth |
| Finary | Ce français a trouvé comment éviter l'impôt à vie | Permanent income tax avoidance | ★★★ Wealth |
| Finary | Comment la famille la plus riche de France a tout perdu | Wealth preservation lessons | ★★ Wealth |

**Cross-channel vol consensus:** 3/6 channels (Bravos, Prof G, Real Vision) independently signaling elevated risk / HIGH_VOL environment. No transcripts available (cloud IP block) — signals derived from titles only. Confidence: MEDIUM.

**Regime implication:** Lean HIGH_VOL → wait for HMM confirmation ≥55% before acting. Reduce IWM exposure if economic reset narrative confirms.
