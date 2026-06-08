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

## 2026-06-08 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Aux USA 90% n'ont RIEN, 10% contrôlent TOUT | NEUTRAL — wealth inequality framing | LOW — background context |
| Oseille TV | La Chine se venge de 150 ans d'humiliation | RISK-OFF — geopolitical escalation | MED — macro uncertainty catalyst |
| Oseille TV | Une IA révèle des failles cachées depuis 17 ans ! | NEUTRAL — tech/security | LOW |
| Oseille TV | Amazon FBA en 2026 : C'est fini ? | NEUTRAL — entrepreneurship | LOW |
| Bravos Research | A Once in a Lifetime Economic Reset is Coming. | HIGH_VOL — systemic reset framing, bearish | HIGH — macro regime shift signal |
| Bravos Research | History is About to Be Made. | HIGH_VOL — anticipates major market event | HIGH — watch for catalyst |
| Finary | Ce français a trouvé comment éviter l'impôt sur le revenu à vie | NEUTRAL — tax strategy | HIGH — wealth mgmt priority |
| Finary | La vie (folle) de la famille la plus riche d'Asie | NEUTRAL — profile | LOW |
| Finary | Ce que révèle cette émission TV sur la finance... | NEUTRAL — financial literacy | LOW |
| Investing Simplified (Prof G) | BREAKING: Markets Are Starting to Crack | HIGH_VOL — bearish, market stress signal | HIGH — confirms vol expansion risk |
| Investing Simplified (Prof G) | The AI & Quantum Boom Is Just Starting | LOW-MID_VOL — risk-on QQQ bias | MED — contradicts bearish signals |
| IG France (Baradez) | MarketLive 2026-06-08 | MID-HIGH_VOL — TA on current market trends | HIGH — daily technical context |
| IG France (Baradez) | MarketLive 2026-06-05 | MID_VOL — ongoing TA session | MED |
| IG France (Baradez) | Créer un Robot de Trading Automatique avec l'IA | NEUTRAL — AI trading tools | LOW |
| IG France (Baradez) | MarketLive 2026-06-04 | MID_VOL — TA session | MED |
| IG France (Baradez) | MarketLive 2026-06-03 | MID_VOL — TA session | MED |
| IG France (Baradez) | MarketLive 2026-06-01 | MID_VOL — TA session | MED |
| Real Vision Presents | Retail Is Going to Get REKT by These IPOs! | HIGH_VOL — IPO risk-off, bearish retail | HIGH — risk-off sentiment |
| Real Vision Presents | The Real Opportunity Isn't What You Think! | MID_VOL — contrarian framing | MED |
| Real Vision Presents | WHAT?? Financial Privacy?? | NEUTRAL — privacy/crypto | LOW |
| Real Vision Presents | A New Frontier in Gold Exploration | RISK-OFF — gold demand = flight to safety | MED — vol expansion signal |
| Real Vision Presents | Stablecoins, ETFs, and the New Crypto Market Structure | NEUTRAL — crypto/ETF structure | LOW |
| Real Vision Presents | How Current Makes DeFi Yield Simple | NEUTRAL — DeFi | LOW |
| Real Vision Presents | Why This Founder Left Ethereum for Sui | NEUTRAL — crypto | LOW |
| George Gammon | (no new videos this week) | — | — |

**Cross-channel consensus (HIGH_VOL bias):** Bravos Research + Investing Simplified/Prof G + Real Vision = 3 independent channels flagging market stress, economic reset risk, and IPO danger. Geopolitical risk (China, Oseille TV) adds macro uncertainty. Net signal: **MID→HIGH_VOL transition watch**. Reduce position sizing 50% if HMM confirms. SPY/IWM cautious; QQQ mixed (AI tailwind vs market crack).
