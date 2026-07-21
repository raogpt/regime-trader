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

## 2026-07-13 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Yahoo Finance | blog | Strait of Hormuz tensions squeeze Wall St pre-bell; US airstrikes on Iran, Iran retaliates; futures/oil react | Fresh war escalation, risk-off open | HIGH | High — direct SPY/QQQ/IWM driver |
| WSJ Markets | blog | Oil rises, gold slides on fresh U.S.-Iran strikes ("reviving concerns about inflation and prospects of tighter monetary policy") | Inflation-driven risk-off; gold down not up (hike fear dominates) | HIGH | High |
| WSJ Markets | blog | "Oil Prices Could Stay Elevated as Mideast Tensions Rise"; Treasury yields edge higher | Sustained energy/rate pressure | HIGH | High |
| CNBC — Finance | blog | Kalshi traders: Strait of Hormuz traffic won't normalize until 2027 (only 43% odds by Dec 1) | Prediction markets pricing prolonged disruption | HIGH | Med-High |
| CNBC — Finance | blog | Kalshi traders: odds gas >$3.50 through election day jump to 75% | Sustained energy/inflation pressure | HIGH | Med |
| Investing.com — Market Overview (3 headlines) | blog (title-only) | "US Markets Open to a War", "Gulf Tensions Igniting Risk-Off Monday", "Middle East Tensions Fuel Fed Hike Bets" | Risk-off + hawkish repricing | HIGH | High — but headline-only, low confidence detail |
| Seeking Alpha — Market Currents | blog (title-only) | Crude oil climbs >3% as US/Iran fight for Hormuz control | Oil-driven vol confirmation | HIGH | Med — title only |
| Liberty Street Economics (NY Fed) | blog | Tariff pass-through survey: ~47% service / 44% mfg firms still plan further price hikes from tariffs | Sticky, still-building inflation input | Supports HIGH | High — Fed/HMM relevant |
| Liberty Street Economics (NY Fed) | blog | Small Business Credit Survey: majority of goods/retail firms report tariff cost challenges in 2025 | Inflation persistence, corroborates above | Supports MID-HIGH | Med |
| Motley Fool | blog | Fed minutes show rate HIKE (not cut) "fully on the table" 2026; CME FedWatch shows 81.9% odds fed funds ends year above current range | Hawkish Fed regime shift | HIGH | High |
| CNBC — Economy | blog | Fed June minutes show officials split on rate direction ("family fight" could drag on) | Policy uncertainty at the Fed | MID-HIGH | High |
| Federal Reserve (official) | blog | June 16-17 FOMC minutes released; Warsh names task force leadership | Institutional/Fed governance context | Neutral | Med |
| Yahoo Finance | blog | Stocktwits retail sentiment: bullish on SPY, neutral on QQQ during Iran-driven selloff | Rotation: SPY favored over QQQ in sentiment | Rotation signal | High — direct SPY/QQQ split |
| Motley Fool | blog | "3 Dividend Stocks Leading 2026's Rotation Into Value" — tech worst H2 sector so far; capital flowing to energy/financials/healthcare/staples after soft jobs report | Broadening away from AI/tech mega-caps | Rotation (QQQ risk, IWM/value tailwind) | High |
| ETF Trends (VettaFi) | blog | "'Mega-Rotation' Could Lift This Income ETF" — breadth widening beyond AI trade, brief July 7 pullback | Confirms broadening/rotation | Med-High | High |
| ETF Trends (VettaFi) | blog | "Broadening Trade Returns as Conflict Eases. Can It Outlast a Hawkish Fed and Fading Liquidity?" — H1 2026 recap | Rotation thesis now tested by hawkish Fed + fading liquidity | Cautionary | High |
| The Big Picture (Ritholtz) | blog | Monday reads cite WSJ survey: "War Leaves Economy With More Stubborn Inflation," economists raising 2027 inflation forecasts | Confirms sticky-inflation narrative independently | HIGH | Med-High |
| Motley Fool | blog | Michael Burry places AI short bets, calls it "the beginning of the end" (single-name framed but macro AI-bubble theme) | AI-bubble sentiment risk flag | Vol risk | Med |
| WSJ Markets | blog | "The Quarter-Trillion-Dollar Onslaught of AI Bonds Is Testing Investors' Limits" | Credit-market stress from AI capex debt issuance | Vol risk | Med-High |
| WSJ Markets | blog | "AI Jitters Weigh on Nasdaq Futures"; "Tech Stock Jitters Just Went Off the Charts" | Tech-specific volatility elevated | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | Bitcoin ETFs in longest outflow streak on record (~$8B over 8 weeks); early signs of a bounce | Risk-appetite cooling in crypto, tentative stabilization | Med | Low-Med (sentiment proxy, not ETF universe) |
| ETF Trends (VettaFi) | blog | "So Far, So Good" — soft June jobs report (+57k, participation 61.5%) reduced odds of immediate July hike; front-end yield curve rallied | Partial dovish counter-signal to the hawkish narrative | Mixed | High |
| ETF Trends (VettaFi) | blog | Treasury Yields Snapshot 7/10: 10y 4.56%, 2y 4.21% | Rate-level/curve data point (normal curve) | Context | Med |
| Motley Fool + Yahoo Finance (2 sources) | blog | Bank earnings season opens Tue 7/14: JPM, WFC, C, GS, BAC report | Cross-source macro read via bank earnings | Catalyst event (2 days out) | High — earnings/catalyst filter relevant |
| WSJ Markets | blog | "How to Invest When the Global Crises Never Stop" — argues bond yields need higher risk premium in a multi-crisis world | Wealth-mgmt regime framing | Context | Med |
| CNBC — Economy | blog | India inflation accelerates to 4.38% in June (Iran war + food/energy); China CPI soft but PPI near 4-yr high | Global inflation spillover from war, independent of US sources | HIGH | Med |
| ETF Trends (VettaFi) | blog | "Focus on Intent" — post-tax-season reminder to revisit estate planning docs | Wealth-mgmt (generic) | Low direct | Low |
| WSJ Markets | blog | "10 of the Best Financial Advisor Companies" — fiduciary RIA rankings | Wealth-mgmt reference | Low | Low |
| Motley Fool (3 items) | blog | Retirement/Social Security personal-finance pieces ("$500k enough to retire?", SS claim-at-70 math, spousal benefits) | Wealth-mgmt, evergreen | n/a | Low |
| FRED Blog (St. Louis Fed) | blog | Primary vs. total deficit history; foreign-held US assets ~59% equities / ~24% Treasuries | Fiscal/macro background context | Low-Med | Low |
| IG France (Alexandre Baradez) | youtube (title-only) | "MarketLive: derniers tendances graphiques des marchés" | Unknown content — title-only | Low confidence | Low |
| Motley Fool (46 remaining items) | blog | Single-stock/AI-name deep dives (Nvidia, SpaceX, Micron, Nike, Salesforce, UnitedHealth, etc.) and generic index-fund/retirement explainers | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~35 remaining items) | blog | Niche ETF launches and sector pieces (nuclear, drones, dividends, CLOs, healthcare, REITs) | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~35 remaining items) | blog | M&A/deals, opinion columns, company-specific stories (UniCredit/Commerzbank, Circle bank charter, etc.) | — | — | Low |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company headlines (Q32 Bio, Ford/Unifor, Meta data center, Fraport, etc.) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (6 remaining items) | blog (title-only) | Single-company news headlines (CoreCivic, Ocugen, Gamehaus, Cathie Wood trades, etc.) | — | — | Low — title-only |

## 2026-07-21 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Motley Fool | blog | US gas prices back above $4.00/gal (+27% YoY, AAA data) as Iran conflict grinds on | Sustained energy-cost pressure feeding inflation/Fed debate | HIGH | High |
| Yahoo Finance | blog | Yemen's Houthis impose naval blockade on Saudi Arabia — new front widening Iran war beyond the Gulf | Fresh escalation, not de-escalation, mid-window | HIGH | High |
| WSJ Markets (4 items) | blog | Ceasefire mediation push (7/21): gold up >1%, oil eases below $90 Brent, Asian equities up on ceasefire hopes | First concrete de-escalation signal, still unresolved | Mixed — HIGH→easing | High |
| Yahoo Finance | blog | New tariffs imposed on Canadian goods (mentioned in passing, 7/21) | Fresh trade-policy catalyst, thin detail | Unclear | Low-Med — no detail |
| Investing.com — Market Overview (5 headlines) | blog (title-only) | "Iran Strikes, Burnham's Gilt Test and Inflation Surprises"; "S&P 500: Treasury Liquidity Drain Signals Higher Market Volatility"; "Market Broadening Gains Momentum as AI Uncertainty Grows"; "The $40 Trillion Trap: Disinflation Is Not Deliverance" | Vol + broadening + disinflation themes echoed | HIGH | Med — headline-only |
| Yahoo Finance + Motley Fool (2 sources) | blog | Kevin Warsh confirmed as Fed Chair (sworn in May 22), "reform-oriented" Fed, declined to issue dot plot | Fed leadership/communication-regime shift | Uncertainty-raising | High — HMM Fed-feature relevant |
| Motley Fool | blog | Warsh's inflation testimony landed as traders priced 86% odds of a July rate HOLD | Reduced near-term hike/cut tail risk vs 7/13 | Lower near-term | High |
| CNBC — Finance | blog | Dallas Fed's Logan: "modestly" higher rates warranted, "good inflation news wasn't good enough" | Hawkish Fed voice | HIGH | High |
| CNBC — Finance | blog | NY Fed's Williams: inflation "has peaked," rates "well positioned" | Dovish counterweight — Fed voices still split | MID | High |
| The Big Picture (Ritholtz) | blog | Warsh has not confirmed PCE as Fed's inflation yardstick across hearings/press conf — "glaring omission" per Stay-At-Home Macro | More opaque Fed communication regime | Uncertainty-raising | Med — HMM relevant |
| CNBC — Economy + ETF Trends (2 sources) | blog | June CPI 3.5% YoY (vs 3.8% expected, down from May 4.2%); core ~2.9% | Disinflation surprise, complicates hawkish narrative | Dovish counter-signal | High |
| CNBC — Economy | blog | June PPI unexpectedly fell 0.3% on big drop in gasoline | Confirms cooling headline inflation | Dovish | High |
| CNBC — Economy | blog | Import prices from China hit highest level since 2008 | Tariff pass-through still building (corroborates 7/13 NY Fed thesis) | Supports HIGH/hawkish | High |
| ETF Trends | blog | Retail sales +0.2% June, 5th straight monthly gain but deceleration from May's +1.0% | Consumer resilient but slowing | Mixed | Med-High |
| WSJ Markets | blog | US Leading Economic Index fell 0.2% in June on weakening consumer spending | Modest deceleration signal | Mixed | Med |
| CNBC — Economy | blog | Renewed Hormuz hostilities force ECB rate rethink amid "extremely volatile" outlook | Explicit named-source volatility characterization | HIGH | High |
| ETF Trends (3 posts) | blog | Russell 2000 + S&P SmallCap 600 averaging +20.8% YTD vs S&P 500's +8.9-11.4% YTD | Strongest quantified IWM-outperforming-SPY rotation data point to date | Rotation signal | High — direct IWM/SPY split |
| ETF Trends | blog | S&P 500 fell 1.6% for week ending 7/17, sitting 2.0% below June 2 record, +8.9% YTD | Confirms real single-week vol/drawdown | HIGH (realized) | High |
| ETF Trends | blog | Record $1.1T ETF inflows in 2026 so far; new Nasdaq-100 ETF fee war | Strong risk appetite/participation despite vol | Med | Med |
| ETF Trends | blog | "Q2 Recap: Markets Get Back on Track" — Q2 2026 as a full-quarter "wall of worry" climb | Resilience-despite-macro-noise framing continues from 7/13 | Context | High |
| WSJ Markets (4 items) | blog | Chip/AI whipsaw across the week: "Nasdaq Loses Early Gains... Fears... AI" → "Chip Stocks Regain Ground... AI-bubble anxieties in rear-view mirror" → "AI Trade Bounces Back" → "Chip Stocks Lead Futures Higher" | Elevated realized vol specifically in QQQ-relevant chip/AI complex, both directions within days | HIGH (QQQ-specific) | High |
| The Big Picture (Ritholtz) | blog | SpaceX lost >$1T value from post-IPO peak ($2.64T→$1.63T); bonds "trading like junk bonds" (Bloomberg/Globe and Mail) | Major AI-adjacent value-destruction + credit-stress data point | Vol risk | Med-High |
| CNBC — Finance (2 items) | blog | Morgan Stanley record quarterly revenue, equities trading +69%; peers call market "clearly extremely risk-on" | Hard evidence of elevated realized trading volume/vol | HIGH (realized) | High |
| CNBC — Finance + Yahoo Finance (2 sources) | blog | Jamie Dimon: wouldn't buy stocks or long Treasurys at current prices, markets underestimate risk | Prominent bearish counter-voice to market resilience | Vol risk | High |
| The Big Picture (Ritholtz) | blog | "Overvalued, Bubble, or Revolution?" — Mag 7 concentration ~27%, Nvidia P/E back to 2019 level, tech fwd P/E 22 vs 55 in 2000 | Data-backed pushback against AI-bubble framing | Mitigating factor | Med-High |
| George Gammon | youtube (title-only) | "It's Official, The AI Bubble Just Popped (Here's Why)" | Contradicts Ritholtz "not a bubble" thesis — unconfirmed | Low confidence | Low — title-only |
| ETF Trends | blog | "Bonds Are Back" — cash increasingly costly, Treasuries pitched as rebalancing target with attractive real yields, lower vol than equities | Wealth-mgmt regime framing | Context | High |
| ETF Trends | blog | American Century's Greenblath on new Fed chair's impact on bond landscape | Fed-communication-shift is bond-market relevant | Context | Med |
| CNBC — Finance + Motley Fool (2 sources) | blog | Buffett: "tough to find values when everybody is preferring gambling" | Market froth/sentiment gauge, recurring theme | Context | Med-High |
| The Big Picture (Ritholtz) | blog | "At The Money: When Should Do-It-Yourself Investors Fire Themselves?" — advisor-value/DIY-investing interview series | Wealth-mgmt, evergreen | n/a | Low-Med |
| Investing Simplified (Prof G) (2 titles) | youtube (title-only) | "This Market Dip Just Created the BEST Buying Opportunity of 2026"; "History is About to be Made" | Bullish dip-buy framing coinciding with mid-window S&P pullback — unconfirmed | Low confidence | Low — title-only |
| IG France (2 titles) | youtube (title-only) | "Tensions USA-Iran : Quel impact..."; "Inflation US : Pourquoi les marchés ne réagissent pas ?" | On-theme with Iran/inflation narrative, content unknown | Low confidence | Low — title-only |
| Liberty Street Economics (NY Fed) (3 items) | blog | Series on nonbank subsidiaries, Basel III capital treatment, regulatory arbitrage in bank holding companies | Banking-structure research, narrower than 7/13's tariff series | Low direct | Med — background |
| Federal Reserve (official) (3 items) | blog | Discount-rate meeting minutes; bank-examiner enforcement action; joint exam-confidentiality statement | Administrative, procedural | Neutral | Low |
| FRED Blog (3 items) | blog | Unemployment/marriage status; state manufacturing employment; Q1 2026 state GDP growth | Background macro context | Low | Low |
| Oseille TV (1 title) | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)" | Citizenship-by-investment content, not UEMOA/portfolio relevant | n/a | Low — checked for UEMOA relevance, none found |
| Motley Fool (~45 remaining items) | blog | Single-stock "should you buy X" pieces (Palantir, Meta, ServiceNow, Uber, Netflix, Salesforce, Broadcom, Tesla, Marvell, Micron, Nebius, etc.), Cathie Wood/Tom Lee crypto picks | — | — | Low — outside ETF-only mandate |
| ETF Trends (~30 remaining items) | blog | Niche fund/sector pieces (nuclear, rare earths, healthcare, REITs, crypto ETPs, active-mgmt launches) | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~42 remaining items) | blog | M&A/deals, opinion columns, personal-finance/tax features, single-company stories | — | — | Low |
| CNBC — Finance (~17 remaining items) | blog | Company/deal-specific (Capital One/Discover, Coinbase, China auto sales, Kalshi growth, India IPO, Anthropic IPO prep) | — | — | Low |
| Yahoo Finance (~11 remaining items) | blog | Single-stock "why did X move today" pieces (Pan American Silver, Rithm, Itron, Garmin, Ouster, Cenovus, M/I Homes, Lucid, etc.) | — | — | Low |
| Investing.com — Stock Market News (10 items) | blog (title-only) | Single-company headlines (Virbac, Jungheinrich, Bachem, Samsung robotics, Nextdc, Zurich Insurance, Emirates/Boeing) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (7 items) | blog (title-only) | Single-company/earnings-print headlines (NBIS/ZION movers, TSMC, Anthropic, Oracle/Wisconsin, Wärtsilä/Wereldhave/Vår Energi) | — | — | Low — title-only |
| IG France (5 remaining), Investing Simplified (2 remaining), Oseille TV (2 remaining), Finary (3), George Gammon (1 remaining) | youtube (title-only) | Generic technical-analysis/personal-finance/wealth-mgmt French and English content | — | — | Low — title-only, unconfirmed |
