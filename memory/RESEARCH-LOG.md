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

## 2026-05-30 — YouTube Intel

> Note: Transcripts blocked (cloud IP ban on YouTube transcript API). Analysis by title + channel profile.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Votre argent en banque n'est plus à vous ! 🏦 | Risk-off / systemic banking risk | ★★★ Wealth-mgmt |
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL — bearish macro alert | ★★★ Regime |
| Finary | Le Japon perd 1 habitant toutes les 35 secondes. Son économie va-t-elle s'effondrer ? | Macro tail-risk / Japan rates | ★★ Macro |
| Finary | Le crédit caché de millions de Français | Consumer debt stress France | ★ Wealth-mgmt |
| Finary | La richesse réelle de la famille royale britannique | Informational | ✗ |
| Finary | J'ai retracé le patrimoine de Donald Trump | Political/financial | ★ |
| Prof G | The Only Retirement Video You Ever Need to Watch | Passive income, ETF withdrawal | ★★★ Wealth-mgmt |
| Prof G | 5 Best Stocks & Hottest Investing Sectors for 2026? | Risk-on sector rotation signal | ★★ Regime |
| Prof G | 🚨 Investors Could Get Blindsided.. (CRUCIAL Market Update 2026) | HIGH_VOL warning | ★★★ Regime |
| IG France (Baradez) | MarketLive : tendances graphiques 2026-05-28 | TA daily — actionable | ★★★ Regime |
| IG France (Baradez) | Comment vraiment maîtriser le RSI en trading | Educational — TA methodology | ★ |
| IG France (Baradez) | MarketLive : tendances graphiques 2026-05-27 | TA daily — actionable | ★★★ Regime |
| Real Vision | It Said 2-Months... It Did It In Minutes! | Rapid-move / HIGH_VOL event | ★★★ Regime |
| Real Vision | The Convergence: AI, DeFi, and the Next Financial System | Structural macro / crypto | ★ |
| Real Vision | Sui Overflow 2026 Hackathon | Crypto ecosystem | ✗ |
| Real Vision | One Wallet Cost Me Everything! | Crypto risk mgmt | ✗ |
| Real Vision | Moonshots: The Next Wave of Sui DeFi | Speculative crypto | ✗ |
| Real Vision | DeepBook: Where Sui Finance Starts | Crypto infrastructure | ✗ |
| Real Vision | From Lagos to the World: the Future of African Payments | Africa fintech / UEMOA payments | ★★★ Wealth-mgmt |
| Real Vision | RWAs: Every Asset Will Be Onchain — The $100T Migration | Asset tokenization / access | ★★★ Wealth-mgmt |

**Cross-channel consensus (4/6 active channels):** Risk-off / elevated caution → leans HIGH_VOL or MID→HIGH transition.
**No-new-video channel:** George Gammon (1 channel quiet).
