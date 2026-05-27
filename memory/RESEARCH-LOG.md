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

## 2026-05-27 — YouTube Intel

**Channels checked:** 7 | **New videos:** 23 | **Transcripts:** blocked (titles+web research used)

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Entire Financial System Just Changed Forever | 🔴 HIGH_VOL — $8T Treasury supply shock, EU selling pressure on yields | ★★★ HIGH |
| Investing Simplified | 🚨 Investors Could Get Blindsided (Crucial Market Update) | 🟡 MID→HIGH — Fed rate-hike prob 1%→60%, USMCA tail risk | ★★ MEDIUM |
| Investing Simplified | 5 Best Sectors for 2026 | 🟡 MID_VOL — QQQ/AI leads, IWM lagging, leveraged ETF closure risk | ★★ MEDIUM |
| Investing Simplified | America's #1 Retirement Risk | 🟡 MID→HIGH — inflation + rate hike = defensive allocation | ★★ MEDIUM |
| IG France (Baradez) | MarketLive 2026-05-27 | 🟡 MID_VOL — CAC volatile, ECB hike Jun 11 = spillover risk | ★★ MEDIUM |
| IG France (Baradez) | MarketLive 2026-05-22 | 🟢 Temporary LOW_VOL window (quickly reversed) | ★ LOW |
| IG France (Baradez) | Créer un Robot de Trading sans coder | 🟢 Neutral (product demo) | ★ LOW |
| IG France (Baradez) | MarketLive 2026-05-20 | 🟢 Neutral (background macro) | ★ LOW |
| Real Vision | AI's Biggest Bottleneck Isn't Chips Anymore | 🟡 MID_VOL — AI capex cycle maturing, QQQ earnings risk ahead | ★ LOW-MEDIUM |
| Real Vision | RWAs: Every Asset Will Be Onchain ($100T Migration) | 🟢 Neutral — crypto/DeFi, indirect spillover only | ★ LOW |
| Real Vision | Adventures in US Capital Markets | 🟢 Neutral — institutional/DeFi crossover | ★ LOW |
| Real Vision | AI Eats Software: Agentic Finance | 🟢 Neutral — AI infrastructure long-term | ★ LOW |
| Real Vision | Slush Wallet / Sui Live | 🟢 Neutral — crypto product | ★ LOW |
| Real Vision | DeepBook: Where Sui Finance Starts | 🟢 Neutral | ★ LOW |
| Real Vision | Moonshots: Next Wave of Sui DeFi | 🟢 Neutral | ★ LOW |
| Real Vision | "One Forgotten Wallet Cost Me Everything!" | 🟢 Neutral (crypto custody) | ★ LOW |
| Real Vision | From Lagos to World: African Payments (Tayo Oviosu) | 🟢 PRIORITY wealth — Africa fintech, UEMOA integration | ★★ MEDIUM |
| Oseille TV | Votre argent en banque n'est plus à vous! | 🔴 RISK-OFF — bail-in risk, offshore banking urgent | ★★ WEALTH PRIORITY |
| Oseille TV | Où vivre au Panama? Guide complet | 🟢 Tax optimization — Panama residency guide | ★★ WEALTH PRIORITY |
| Finary | Les mystérieux trades du président américain | 🔴 POLITICAL RISK — Trump $220–750M trades, catalyst filter = ON | ★★★ HIGH |
| Finary | Bourse: les gagnants empochent toute la mise? | 🟡 MID_VOL — breadth weak, QQQ concentration confirmed | ★★ MEDIUM |
| Finary | La France touche le fond. C'est l'heure du rebond. | 🟢 Neutral for US ETFs (France-specific rebound) | ★ LOW |
| Finary | La richesse réelle de la famille royale britannique | 🟢 Neutral (informational wealth-mgmt) | ★ LOW |

### Cross-Channel Consensus (4+ channels)
- **MID→HIGH VOL transition confirmed**: Bravos + Investing Simplified + IG France + Finary all flag macro deterioration
- **QQQ ≫ IWM**: Investing Simplified + Real Vision + Finary all prefer large-cap/AI over small-cap
- **Political risk = permanently elevated**: Finary (Trump trades) + Investing Simplified (USMCA)
- **Systemic/banking risk**: Bravos ($8T refinancing) + Oseille TV (bail-in warning)

### HMM Bot Actions
- Raise confidence threshold to **≥ 60%** (vs 55% default) until macro clears
- **Block entries Jun 9–11** (ECB rate decision catalyst window)
- ETF preference order: **QQQ > SPY; IWM = avoid longs**
- Sizing: HIGH_VOL parameters preemptively (60% max allocation, wide stops)

### Wealth Management (PRIORITY)
1. Open offshore account Panama (6% fixed deposit, bail-in protection) — Oseille TV
2. UEMOA diaspora: CFA franc account access since Mar 2026 (BCEAO rule change)
3. Trump political risk buffer: maintain 10–15% cash, avoid leveraged ETFs
4. France rebound: contrarian long-term opportunity (personal portfolio, not HMM bot)
5. AI capex watch: QQQ earnings risk if capex plateau hits Q3 2026

**Full report:** reports/2026-05-27-youtube-intel.md
