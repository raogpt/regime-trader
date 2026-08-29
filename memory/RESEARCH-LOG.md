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

## 2026-08-29 — Market Intel (regime_trader)
Gap since last run: 2026-07-13 → 2026-08-29 (6.5 weeks). 279 new items across 20 sources (73 YouTube, 206 blog). Full detail in reports/2026-08-29-market-intel.md; table below is high/med relevance items only — see report for the low-relevance bucket breakdown.

| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets (6 headlines, content available) | blog | Fed Chair Kevin Warsh's Jackson Hole speech (Aug 28) signals inflation fight "not done"; 2y yields up, stocks down, dollar up, gold down | Hawkish Fed regime confirmation | HIGH | High — direct rate-regime driver |
| Investing.com — Market Overview (3 headlines, title-only) | blog | "Warsh Talks Tough on Inflation as US Dollar Rallies", "The Only Thing Markets Need to Hear From Warsh at Jackson Hole" | Corroborates WSJ hawkish read | HIGH | High — 5+ source consensus on one catalyst |
| Yahoo Finance — Market News | blog | "Review & Preview: Warsh Gets Real on Inflation" | Corroborates hawkish turn | HIGH | Med-High |
| Motley Fool | blog | "President Trump Claims 'Prices Are Dropping Fast,' but Trumpflation Data Tells a Different Story" | Political/data conflict on inflation narrative | HIGH | Med — context for Fed credibility |
| WSJ Markets | blog | "Japan Spent Record $98.7B to Prop Up Yen in Joint Move With U.S." (Bessent-backed) | FX intervention scale confirms yen/dollar stress | Elevated | Med-High — cross-asset vol input |
| Federal Reserve (official) | blog | FOMC statement (7/29) + July 28–29 minutes released 8/19 | Official record ahead of Warsh's hawkish Jackson Hole follow-up | Context | Med — primary source |
| The Big Picture (Ritholtz) | blog | "What's Upsetting the Bond Market?" — yen interventions, Treasury buyback talk, sticky inflation, tariffs, $40T debt, bond vigilantes | Bond-market stress, multi-factor | HIGH | High — synthesizes multiple threads |
| The Big Picture (Ritholtz) | blog | "Wanted: A More Humble Fed" — institutional behavioral-error critique of Fed/Treasury/Congress | Policy uncertainty | Med | Med |
| Motley Fool | blog | "The S&P 500 Is Flashing a Warning Signal Not Seen in Decades" — valuation stretch despite record highs | Late-cycle/valuation risk flag | Vol risk | High — index-level, direct SPY relevance |
| Motley Fool | blog | WSJ-sourced: "$3 Trillion in Off-Balance-Sheet AI Commitments" tanked Vertiv, GE Vernova | AI-capex credit/balance-sheet risk continuing from July | Vol risk (QQQ-specific) | High |
| Motley Fool | blog | "Marvell Slides 10% on Softer Fiscal 2028 Guidance" despite EPS beat — guidance-driven, not headline miss | AI-semis vol, guidance sensitivity | Med-High (QQQ) | Med-High |
| Seeking Alpha — Market Currents | blog (title-only) | "Gold plunges as Warsh's Jackson Hole inflation concerns spark rate hike bets" | Corroborates hawkish-Fed/gold-down pattern (same as July Iran shock) | HIGH | High |
| Seeking Alpha / WSJ | blog | Venezuela oil-reserves deal (65B barrels, Trump) + "Persian Gulf exports recovered to two-thirds of pre-war levels" | Oil-supply de-escalation vs. July's Hormuz shock | Moderating from July HIGH | Med — partial unwind of prior oil-driven vol |
| WSJ Markets | blog | "How Xi Jinping Turned Oil From a Weakness Into a Geopolitical Weapon" — China crude reserves as leverage | Structural geopolitical-oil risk | Context | Med |
| Liberty Street Economics (NY Fed) | blog | "Has Broader Stock Market Participation Changed How Interest Rates Affect the Economy?" | Wealth-effect transmission channel, relevant to HMM rate-sensitivity features | Context | Med — methodology, not immediate signal |
| Liberty Street Economics (NY Fed) | blog | "How Distressed Are Consumers?" — credit card delinquency measures reconciled, total debt -$13B Q2 | Consumer credit stabilizing, mild | LOW-MED | Med |
| Liberty Street Economics (NY Fed) | blog | "AI's Impact on Labor and Hiring" (new Research Director series) | AI/labor macro theme, ongoing | Context | Low-Med |
| Yahoo Finance | blog | "Bank of America takes heat for stark S&P 500 call" | Wall St forecast dispersion widening | Med | Med |
| Bravos Research (8 items, YouTube title-only) | youtube | "China Just Triggered a Global Monetary Reset", "The First Domino of the Global Debt Crisis is Here", "Japan and the US Just Pulled the Trigger" | Crisis/reset narrative cluster, Aug 9–27 | Bearish tilt (unconfirmed, title-only) | Med — thematically aligned w/ Warsh/yen items above but not corroborated by content |
| George Gammon (8 items, YouTube title-only) | youtube | "The Entire House of Cards Is About To Fall", "WARNING: This Is When The Dollar Will Lose Reserve Currency Status", "It's Official, The AI Bubble Just Popped" | Same bearish/crisis cluster as Bravos Research | Bearish tilt (unconfirmed) | Med — 2-channel title-only consensus on dollar/debt stress |
| Investing Simplified (Prof G) (15 items, YouTube title-only) | youtube | "Extreme Fear: Complete Market Failure", "The next big market crash", "How to survive the next stock market correction" | Bearish/defensive positioning theme (wealth-mgmt framed) | Bearish tilt (unconfirmed) | Med — Wealth Mgmt |
| Finary (15 items, YouTube title-only) | youtube | French wealth-mgmt/tax/expat content, no market-crash framing this cycle | — | — | Wealth Mgmt, low regime relevance |
| Oseille TV (11 items, YouTube title-only) | youtube | Expat tax/passport content (Italy, Panama/Paraguay, Africa), EU "Chat Control" surveillance vote coverage | — | — | Wealth Mgmt / UEMOA-adjacent (expat tax), low regime relevance |
| IG France (15 items, YouTube title-only) | youtube | Titles ref VIX technical level, JPMorgan CEO leverage warning, CDS pricing on Nvidia/Meta/Alphabet, Iran war US borrowing costs, yen/BoJ | Vol/leverage/credit-risk themed titles, unconfirmed | Med (unconfirmed) | Med — most regime-relevant YouTube titles this cycle, still title-only |
| Motley Fool (~24 remaining), WSJ (~24 remaining), Federal Reserve enforcement actions (14), FRED Blog (6), Investing.com Stock Market News (9), Seeking Alpha (4) | blog | Single-stock deep dives, bank enforcement actions/charters, regional employment data, M&A/opinion columns | — | — | Low — outside ETF-only mandate or background-only |
