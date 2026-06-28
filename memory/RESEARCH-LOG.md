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

## 2026-06-28 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| IG France (Baradez) | Inflation américaine, vers une réaction de la Fed ? | HIGH_VOL ★★★ — PCE 4.1% (3yr high), Warsh hawkish, 89% mkt prob of rate hike | Critical macro catalyst for vol regime |
| George Gammon | A $100 Trillion Currency Crisis Just Started | HIGH_VOL ★★★ — DXY rally 99→101+, dollar safe-haven status questioned, JPY at 160 | Dollar dislocation = tail risk for all equities |
| IG France (Baradez) | MarketLive 2026-06-25 | HIGH_VOL — elevated vol, bond market under tension, equity valuation risk | Daily confirmation of hawkish Fed environment |
| IG France (Baradez) | MarketLive 2026-06-24 | MID→HIGH — markets digesting Fed signals, ECB divergence noted | Rate differential story building |
| IG France (Baradez) | MarketLive 2026-06-22 | MID_VOL — volatility levels elevated, Fed/ECB probability analysis | Baseline vol confirmation |
| Finary | Bienvenue dans le siècle chinois | MID_VOL (structural) — China dominance in AI, EV, energy; geopolitical shift | Long-term QQQ headwind from tech competition |
| Investing Simplified (Prof G) | My ENTIRE Investing Portfolio 2026 | LOW→MID — 31-33% equity returns past 12m, portfolio repositioning | Late-cycle signal; buy-and-hold confidence high |
| Investing Simplified (Prof G) | 7 Best ETFs for ROTH IRA | LOW_VOL preference — ETF diversification beats S&P500 in backtest | Structural ETF allocation intel |
| Investing Simplified (Prof G) | SCHD STILL BEATS every dividend ETF | MID_VOL defense — dividend/quality ETF preference signals defensiveness | Rotation toward income/quality = defensive |
| Real Vision Presents | What Finance Looks Like in 5 Years | LOW signal — crypto/TradFi convergence narrative, structural not tactical | Long-horizon structural only |
| Real Vision Presents | The End Goal for Binance Is Much Bigger | LOW signal — crypto super-app ambition | Not relevant to ETF regime |
| Oseille TV | Turquie : 20 ans sans impôt sur les revenus étrangers | WEALTH MGMT PRIORITY — Turkey 20yr foreign income exemption since Jan 2026 | High relevance for UEMOA diaspora tax planning |
| Oseille TV | Dividendes, loyers, cryptos : 0% d'impôt en Turquie | WEALTH MGMT PRIORITY — exemption covers div, cap gains, crypto, rental, bonds | Confirms Turkey as top jurisdiction |
| Oseille TV | S'expatrier à Dubaï en 2026 : encore une bonne idée ? | WEALTH MGMT — Dubai still viable post-Middle East tensions, opportunities remain | UAE vs Turkey comparison relevant |
| Oseille TV | La France taxe plus que l'URSS ? | WEALTH MGMT — extreme French tax burden framing, exit thesis reinforced | Tax optimization urgency signal |
| Oseille TV | Pourquoi l'héritage ruine la vie des héritiers | WEALTH MGMT — wealth transfer psychology | Background context |
| Oseille TV | Le vrai prix de la liberté financière | WEALTH MGMT — personal sacrifice required for FI | Motivational, low signal |
| Oseille TV | La « sélection par la bêtise » selon Attali | LOW — societal commentary | Not relevant |
| Oseille TV | OnlyFans rapporte plus que la pêche au Royaume-Uni | LOW | Not relevant |
| Finary | Bon salaire, mauvaises décisions : le réveil à 44 ans | WEALTH MGMT — avoid consumer debt, start investing early | Personal finance case study |
| IG France (Baradez) | 5 valeurs, vos avis en live | LOW — stock-picking, not ETF-relevant | Background |

**Cross-channel consensus (2+ agree on vol):** HIGH_VOL bias — Baradez + Gammon independently confirm hawkish Fed, elevated rates, currency stress, equity risk. Defensive positioning (SCHD/dividend) from Prof G aligns.
