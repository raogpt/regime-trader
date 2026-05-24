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

## 2026-05-24 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Entire Financial System Just Changed Forever… | HIGH VOL / RISK-OFF | ⭐⭐⭐ Macro structural shift thesis |
| Bravos Research | In 6 Months, It's All Over. | HIGH VOL / BEARISH | ⭐⭐⭐ Crash timing prediction |
| Investing Simplified (Prof G) | 🚨 Investors Could Get Blindsided.. (CRUCIAL Market Update 2026) | HIGH VOL / RISK-OFF | ⭐⭐⭐ Market warning, HMM-relevant |
| Investing Simplified (Prof G) | The only 5 ETFs you'll ever need | LOW VOL / NEUTRAL | ⭐ ETF allocation, not tactical |
| Investing Simplified (Prof G) | Forget NVDA.. These Quantum Stocks Could Be Bigger | MID VOL / RISK-ON | ⭐ Sector rotation signal |
| Finary | Les mystérieux trades du président américain | HIGH VOL / POLITICAL | ⭐⭐ Policy risk, insider-trade narrative |
| Finary | Bourse : les gagnants empochent toute la mise ? | MID VOL / CONCENTRATION | ⭐⭐ Market breadth concern |
| Finary | La France touche le fond. C'est l'heure du rebond. | LOW VOL / CONTRARIAN | ⭐ EU market, not SPY/QQQ/IWM direct |
| Finary | Combien gagnent nos députés ? | NEUTRAL | ⭐ Political/wealth context |
| IG France (Alexandre Baradez) | MarketLive 2026-05-22 — tendances graphiques | MID VOL / TECHNICAL | ⭐⭐ TA market read |
| IG France (Alexandre Baradez) | Créer un Robot de Trading (Sans Coder!) | NEUTRAL | ⭐ Algo trading education |
| IG France (Alexandre Baradez) | MarketLive 2026-05-20 | MID VOL / TECHNICAL | ⭐⭐ TA market read |
| IG France (Alexandre Baradez) | MarketLive 2026-05-18 | MID VOL / TECHNICAL | ⭐⭐ TA market read |
| Real Vision | RWAs: Every Asset Will Be Onchain — $100T Migration | RISK-ON / CRYPTO | ⭐ Crypto structural, not ETF |
| Real Vision | AI's Biggest Bottleneck Isn't Chips Anymore | MID VOL / TECH | ⭐⭐ QQQ tech narrative shift |
| Real Vision | Up 13% Overnight!? Why Hyperliquid Exploded! | RISK-ON / CRYPTO | ⭐ Crypto risk appetite |
| Real Vision | AI Eats Software: Agentic Finance | MID VOL / RISK-ON | ⭐ QQQ AI momentum |
| Real Vision | Adventures in US Capital Markets | MID VOL | ⭐ General markets |
| Real Vision | The Next-Gen Dollar: Stablecoins | NEUTRAL | ⭐ Macro USD framework |
| Real Vision | Why Sui Is Building for AI Agents | RISK-ON / CRYPTO | ⭐ Crypto/tech risk-on |
| Oseille TV | Où vivre au Panama ? Le guide complet | NEUTRAL / WEALTH MGMT | ⭐⭐ Tax haven, expat wealth |
| George Gammon | (no new videos) | — | — |

**Cross-channel consensus (HIGH VOL / RISK-OFF):** Bravos Research × 2 + Investing Simplified = 3 channels flagging elevated risk / potential regime shift. HMM should weight HIGH_VOL state upward.
**Transcripts:** ALL blocked (cloud IP — YouTube rate limit). Title-only analysis applied.
