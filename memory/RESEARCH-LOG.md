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

## 2026-07-20 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Yahoo Finance | blog | "Markets brace for return to all-out war in Iran amid rising U.S. death toll... Suez Canal could be next" (7/19) | War re-escalation after brief mid-week pause | HIGH | High — direct SPY/QQQ/IWM driver |
| WSJ Markets (7 headlines, 7/17–7/20) | blog | Oil holds near $90/bbl; Eurozone bond yields + European airline stocks react; U.S. emergency oil reserve at lowest since 1983; oil futures rise on Mideast escalation fears | Sustained energy/rate pressure from renewed Iran conflict | HIGH | High |
| CNBC — Economy | blog | "Renewed Hormuz hostilities drive ECB rates rethink amid 'extremely volatile' outlook" (7/15) | Vol regime named explicitly by an ECB-adjacent source | HIGH | High |
| CNBC — Economy | blog | CPI +3.5% YoY June (vs 3.8% expected, core ~2.9%); PPI -0.3% on falling gasoline — both during the brief Iran pause (7/14–15) | Early-week disinflation surprise, briefly pulled toward MID | MID (early wk) | High |
| CNBC — Finance (5-item cluster, 7/13–16) | blog | Fed Chair Warsh testifies, pledges policy "regime change" to fight inflation; Dallas Fed Logan calls for "modestly" higher rates; Waller warns hikes still possible — vs. NY Fed Williams says inflation "has peaked," rates "well positioned" | Genuine FOMC hawk/dove split; policy uncertainty itself is a vol input | MID-HIGH | High — Fed/HMM relevant |
| Yahoo Finance, WSJ, Motley Fool (4-source cluster, 7/17–20) | blog | SOXX enters bear market (-20%, Yardeni sees another -12% downside); Micron -30% drags SOXX; Nasdaq drops repeatedly on chip slump; "Everything That Could Go Wrong for the AI Trade Just Did" | Sharp QQQ-specific/semiconductor vol spike; S&P ~2% off ATH — "surface calm, engine broke" (Yardeni) | HIGH (QQQ-specific) | High — direct QQQ driver, biggest new theme vs last week |
| ETF Trends (VettaFi) | blog | S&P 500 Snapshot: -1.6% weekly loss, closes below 50-day MA, still only 2.0% off June 2 ATH (7/17) | Confirms broad-index vol uptick but shallow drawdown so far | MID-HIGH | High |
| ETF Trends (VettaFi) | blog | "Small Caps Rally Is Running With Strong, Fundamental Legs" — Russell 2000 outpacing S&P (7/15, early week only) | IWM strength signal that faded from headlines as war/chip selloff dominated later in week | Mixed | High — direct IWM signal |
| Investing.com — Market Overview (3 headlines, title-only) | blog | "Nasdaq 100's Pullback Takes Sentiment Back Into Heavy Buy Territory"; "Everything That Could Go Wrong for the AI Trade Just Did"; "Economic Week Ahead: Fed Silence, Earnings Noise, and Oil Market Risk" (7/20) | Contrarian dip-buy sentiment read emerging post-selloff | Moderating (low-conf) | Med — title-only |
| ETF Trends (VettaFi) | blog | "Notes from the Desk: Priced for Perfection" — Big 4 hyperscaler AI capex ~$700B 2026 (+80% YoY), debt financing strained (7/16) | Credit/valuation stress underlying the chip/tech selloff | Vol risk | High |
| CNBC — Finance | blog | "Big banks poised to report booming revenue propelled by SpaceX IPO, Iran war volatility" (7/14); Morgan Stanley equities trading revenue +69% | Trading desks already monetizing elevated realized vol | Confirms HIGH | High |
| The Big Picture (Ritholtz) | blog | "Overvalued, Bubble, or Revolution?" AI-bubble chart deep-dive (7/17); Friday reads note "the market is clearly extremely risk-on" per WSJ trading-revenue story | AI-valuation debate live; risk-on framing coexists with the chip selloff (divergence, not uniform risk-off) | Mixed | Med |
| CNBC — Economy | blog | China Q2 GDP slowest since 2022, below stimulus target; import prices from China highest since 2008 (7/15, 7/17) | Global growth/inflation spillover risk | MID | Med |
| George Gammon (YouTube, title-only, ×2) | youtube | "It's Official, The AI Bubble Just Popped" (7/16); "WARNING: This Is An Economic Sign That Can't Be Ignored" (7/18) | Bearish macro/AI-bubble warning, timed with the chip selloff | Low-confidence | Med — title-only |
| Investing Simplified/Prof G (YouTube, title-only, ×2) | youtube | "This Market Dip Just Created the BEST Buying Opportunity of 2026" (7/15); "History is About to be Made" (7/18) | Contrarian bullish dip-buy framing | Low-confidence | Med — title-only |
| IG France/Alexandre Baradez (YouTube, title-only, ×4) | youtube | "Tensions USA-Iran: impact Pétrole/Taux/Actions" (7/13); "BCE et Fed: les marchés anticipent le pire" (7/13); "Inflation US: pourquoi les marchés ne réagissent pas" (×2, 7/15) | FR-market corroboration of Iran/Fed narrative | Low-confidence | Med — title-only |
| Finary (YouTube, title-only, ×2) | youtube | "La monnaie parfaite existe-t-elle? Bitcoin, euro, dollar" (7/17); "Votre argent ne vaut rien" (7/15) | Currency-debasement/inflation theme, consistent with sticky-inflation narrative | Low-confidence | Low-Med — title-only |
| Oseille TV (YouTube, title-only) | youtube | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)" (7/14) | Africa-adjacent content, but passport/residency topic — not investment/allocation | n/a | Low — flagged per Africa-priority instruction; off wealth-mgmt mandate |
| WSJ Markets | blog | "The Tax Strategy for People Suffering From Stock-Market Success"; "Inside America's Most Generous 401(k) Plans" (7/17, 19) | Wealth-mgmt, generic | n/a | Low-Med |
| ETF Trends (VettaFi) | blog | "Avert Interest Rate Jitters With This Cash ETF" — post-CPI duration-risk framing (7/15) | Wealth-mgmt, rate-uncertainty hedge | Context | Med |
| Liberty Street Economics (NY Fed) (3 items) | blog | 3-part Basel III/nonbank-subsidiary capital-arbitrage research series | Bank-regulation background, not a near-term vol driver | Low | Low-Med |
| Federal Reserve — Press Releases (3 items) | blog | Bank-exam confidentiality guidance; enforcement action vs. ex-Heritage State Bank officer; discount-rate meeting minutes | Routine/administrative, not FOMC policy signal | n/a | Low |
| FRED Blog (2 items) | blog | State-level manufacturing employment and Q1 real GDP maps | Long-run macro background | Low | Low |
| Motley Fool (~46 remaining items) | blog | Single-stock/AI-name deep dives (Nvidia, SpaceX, Palantir, Netflix, IBM, Apple, etc.) and generic retirement/RMD/Social Security explainers | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~46 remaining items) | blog | Niche single-fund/sector product coverage (nuclear, REITs, healthcare, dividends, crypto ETPs, single-country funds) | — | — | Low-Med — product-level, not macro |
| WSJ Markets (~47 remaining items) | blog | M&A/deals, opinion columns, single-company stories (Prologis/Segro, Fifth Third, U.S. Bancorp, SpaceX) | — | — | Low |
| Investing.com — Stock Market News (10 items, title-only) | blog | Single-European-company headlines (Ryanair, Prysmian, Nokian Renkaat, Arab National Bank, etc.) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (6 remaining items, title-only) | blog | Single-company/quant-fund headlines (MXL/INTC quant snapshot, Prysmian-Molex, Blackstone-Futronic) | — | — | Low — title-only |
| CNBC — Finance (~19 remaining items) | blog | Buffett commentary, IPO news (Anthropic, India IPO), Kalshi user growth — single-name/personality-driven | — | — | Low |
| Yahoo Finance (~16 remaining items) | blog | Single-stock/ETF-comparison pieces (Costco, Energy Transfer, EAFE vs. EM ETFs) | — | — | Low-Med |
| The Big Picture (~8 remaining items) | blog | Weekend/Sunday reads, podcast transcripts, personal-finance links | — | — | Low |
| Oseille TV / Finary / Investing Simplified (~3 remaining items, title-only) | youtube | Generic personal-finance/motivational content, no market thesis | — | — | Low |
