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

## 2026-06-26 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| George Gammon | A $100T Currency Crisis Just Started | HIGH_VOL — Dollar reset triggered, DXY 99→101.3, EM currencies under pressure | ★★★ CRITICAL |
| George Gammon | New Fed Chair Changed Everything (Warsh) | HIGH_VOL — Warsh HAWKISH surprise, 89% mkt probability of Fed RATE HIKE, 2Y yield +14bp in 5 min | ★★★ CRITICAL |
| IG France (Baradez) | Inflation US, Fed reaction? | HIGH_VOL — PCE expected 4.1% (3yr high), bond mkt under tension, rate hike odds surging | ★★★ CRITICAL |
| IG France (Baradez) | MarketLive 2026-06-25 | MID_VOL — VIX ~19-20, NASDAQ rebounded post-Micron; watching VIX support break | ★★ |
| IG France (Baradez) | MarketLive 2026-06-24 | MID_VOL — VIX 19.2, tech sell-off then partial recovery; KOSPI/Samsung stellar | ★★ |
| IG France (Baradez) | MarketLive 2026-06-22 | MID_VOL — VIX 17.6, Hormuz briefly re-blocked then eased; oil down, vol elevated | ★★ |
| IG France (Baradez) | MarketLive 2026-06-19 | MID_VOL — VIX 16-18, key oblique support monitored; yield curve shifted post-Fed | ★★ |
| IG France (Baradez) | 5 valeurs en live | NEUTRAL — sentiment survey: gold 54% bearish, analysis of Nvidia, Bitcoin, CAC40 | ★ |
| Oseille TV | Le prochain krach sera pire que 2008 | HIGH_VOL WARNING — Buffett Indicator 228% (vs 146% in 2000, 109% in 2007) | ★★★ |
| Investing Simplified | 7 Best ETFs ROTH IRA 2026 | CAUTION — cites Buffett Indicator 230%, S&P 35% in top 7 stocks; vol regime elevated | ★★ |
| Investing Simplified | Opportunity of a Lifetime (6 stocks) | RISK-ON bias — quantum/AI/space themes; cautious re: crash possible | ★ |
| Investing Simplified | SCHD beats all dividend ETFs 2026 | NEUTRAL wealth-mgmt — SCHD yield 3.8%, 100% qualified dividends, $91B AUM | ★ |
| Finary | Bienvenue dans le siècle chinois | MACRO STRUCTURAL — China dominates 74 future tech sectors; geopolitical risk to US tech | ★★ |
| Finary | Médecin millionnaire sans héritage | WEALTH MGMT — FR doctor, SAS structure, €4.7M patrimony, €41k/mo, FIRE at 50 | PRIORITY |
| Oseille TV | Turquie : 20 ans sans impôt revenus étrangers | WEALTH MGMT — Turkey 20yr foreign income tax exemption for 2026+ residents | PRIORITY |
| Oseille TV | S'expatrier à Dubaï en 2026 | WEALTH MGMT — UAE still viable expat destination; 3-month residency rule noted | PRIORITY |
| Oseille TV | Pourquoi l'héritage ruine les héritiers | WEALTH MGMT — Inheritance psychology; hide wealth from children | ★ |
| Oseille TV | Le vrai prix de la liberté financière | WEALTH MGMT — Opportunity cost of financial independence (20s–30s sacrifice) | ★ |
| Oseille TV | La sélection par la bêtise (Attali) | MACRO SOCIAL — France demographic Ponzi, productivity decline | ★ |
| Oseille TV | Ces métiers bizarres qui payent 200k€/an | INCOME — High-paying niche jobs outside France; international salary arbitrage | ★ |
| Oseille TV | OnlyFans rapporte plus que la pêche (UK) | ANECDOTE — Platform economy satire | — |
| Real Vision Presents | What Finance Looks Like in 5 Years | STRUCTURAL — TradFi/DeFi convergence; blockchain/AI redesign of finance | ★ |
| Real Vision Presents | End Goal for Binance Is Much Bigger | CRYPTO — Binance expanding to stocks, tokenized securities, global super-app | ★ |
| Real Vision Presents | Binance CEO Richard Teng on Blockchain | CRYPTO — Binance >320M users, expanding into equities/commodities | ★ |
| Bravos Research | (no new videos) | — | — |

**Regime consensus (2026-06-26):** MID_VOL trending HIGH_VOL. Multi-channel agreement on extreme valuations (Buffett 228-230%), hawkish Fed pivot (Warsh, +89% hike prob), dollar surge (DXY 101+), PCE inflation at 3yr high. Reduce sizing. Favor SPY > QQQ (tech vol) >> IWM (rate-sensitive). Hold > Trade bias.
