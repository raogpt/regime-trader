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

## 2026-09-26 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| Federal Reserve — Press Releases | blog | FOMC met Sept 15-16, 2026; statement + Summary of Economic Projections released | Hawkish shift now confirmed via official SEP, not just odds | HIGH | High — primary Fed event |
| FRED Blog | blog | SEP writeup: median core PCE inflation 3.4% for 2026 (returns to 2% only by 2029); unemployment 4.1% through 2029; GDP growth revised up 2.2%→2.3% | Inflation stickier/hawkish-for-longer confirmed with primary data | HIGH | High — Fed/HMM relevant |
| Liberty Street Economics (NY Fed) | blog | DSGE Model Forecast Sept 2026: "slightly more persistent inflation" vs June; r* lower 2026, higher after | Independently corroborates hawkish-for-longer thesis | HIGH | High |
| WSJ Markets | blog | "A Perfect Storm Is Raging in the Bond Market" — 10y Treasury yield jumped above 5.1%, biggest one-day rise in >1 year | Acute bond-market vol event, ~19-20yr yield high | HIGH | High — strongest hard-data vol signal in batch |
| WSJ Markets | blog | "U.S. Stocks Decline as Treasury Selloff Deepens" — Nasdaq-led decline, yields "highest in nearly two decades," dollar strengthens | Confirms rate-driven equity vol | HIGH | High |
| WSJ Markets | blog | "Bond Selloff Worsens, Dinging Stocks" (9/24) → "Yields Subside, Stocks Breathe Easier" (9/25) | Acute stress unwinding within ~48hrs, coincides with Iran de-escalation | Easing from HIGH | High |
| WSJ Markets | blog | "Dollar Jumps to 8-Week High on Fed Rate-Hike Bets" | Confirms active Fed hiking, not just odds | HIGH | High |
| WSJ Markets | blog | "Don't Count Out Corporate Bonds Just Because the Fed Is Raising Rates" / "The Robust U.S. Economy Powers Through Rate Hikes and Rising Bond Yields" | Fed described as actively hiking (regime shift vs July's "odds" framing) | HIGH | High |
| Motley Fool | blog | "Only a Handful of S&P 500 Stocks Can Match 10-Year Treasuries at 5%" — 10y yield at 19-year high (~5%) vs S&P ~1% div yield | Bonds now competitive with equities for income | Context | High — allocation-relevant |
| FRED Blog | blog | RecessionRisk.com series: August 2026 US recession probability = 0.08% | Mitigates HIGH_VOL/hard-landing narrative | Counter-signal (LOW) | Med-High |
| WSJ Markets | blog | "Oil Prices Fall for Fourth Day as Supply Concerns Ease" (9/21) — Hormuz flows improving, diplomacy prospects | Iran/Hormuz conflict (from 7/13 report) beginning to de-escalate | Easing from HIGH | High |
| Yahoo Finance | blog | "S&P 500, Dow, Nasdaq End Week Higher... Amid Signs Of Easing US-Iran Conflict" — Iran pitched 7-day roadmap to end conflict (NYT) | Multi-month war shock potentially resolving | Easing from HIGH | High — direct index driver |
| WSJ Markets | blog | "Bond Traders Are Paying Too Much Attention to the Oil Price" | Caution: yield/oil linkage may be a crowded-trade artifact | Contrarian caveat | Med-High |
| Yahoo Finance / Motley Fool | blog | "Small-Cap Stocks Are Struggling... history shows they lag large-caps at the beginning of interest-rate-hike cycles" | Direct IWM headwind, reverses July's small-cap-rotation-in thesis | Rotation (IWM negative) | High — direct IWM signal |
| WSJ Markets | blog | "European AI-Related Stocks Rally as Confidence Returns" | QQQ/tech resilience despite bond storm | Rotation (QQQ positive) | High |
| Yahoo Finance | blog | "Review & Preview: Snapping the Streak" — Nasdaq +2.1% week, S&P +1.2% week (snapped 2-week losing streak) | QQQ outperformed SPY on the week | Rotation (QQQ positive) | High |
| WSJ Markets | blog | "Cracks in Oracle's AI Data-Center Build-Out Appear in Massive New Mexico Project" (Project Jupiter) | AI-capex execution tail risk | Vol risk (QQQ-specific) | Med-High |
| Motley Fool | blog | Bank of America: stocks "overdue for a pullback"; JPMorgan's Dimon "tectonic plates" framing | Institutional caution despite index highs | Mixed | Med |
| Motley Fool | blog | Gas $4.48/gal national avg (+42% YoY from $3.16); diesel record $6.53/gal (9/22, AAA data) | Hard inflation-input confirmation, independent of Fed commentary | Supports HIGH | High |
| Liberty Street Economics (NY Fed) | blog | Credit-card 90+ day delinquency rose 7.6% (2022:Q3) → 12.8% (2026:Q1) | Consumer credit stress building gradually | Supports MID-HIGH | Med-High |
| FRED Blog | blog | Subprime credit methodology change (Equifax 3.0→VantageScore 4.0) added 33M borrowers; Manhattan subprime share 17.72%→30.27% — flagged by source as methodology artifact, not real deterioration | Data-quality caveat on credit-stress reads | Caution | Med |
| Liberty Street Economics (NY Fed) | blog | "Are Central Banks Moving Out of Dollar Assets?" — dollar FX-reserve share decline (64%→56%, 2015-2025) driven by a handful of large holders, not systemic shift | Pushes back on de-dollarization narrative | Context | Med |
| Motley Fool | blog | Bitcoin ETFs flipped from $5.8B outflows to $800M inflows; BTC back above $80k | Partial re-risking in correlated risk asset, reverses July's outflow-streak framing | Risk-on tilt (sentiment) | Low-Med (outside ETF mandate) |
| Seeking Alpha / Investing.com (title-only) | blog | "Fed Hawkishness Puts Pressure on Gold: Can It Hold Above $4,300?" / "Gold edges higher but falls for the week on hawkish Fed" | Gold pressured by hawkish Fed, not acting as pure safe haven (same atypical pattern as July) | Supports HIGH | Med — headline-only |
| WSJ Markets | blog | NY State sues Polymarket; "$5B Flurry of Nearly Identical Kalshi Trades Draws Scrutiny" | Prediction-market venue/integrity risk — caveat on any Kalshi-derived signal | Context | Med |
| WSJ Markets | blog | "The IRS Is Cracking Down on a Favorite Way the Ultrawealthy Pass On Money" — $736M gift-tax case on GRATs | Wealth-mgmt/tax-strategy content (priority) | n/a | High — wealth-mgmt priority |
| WSJ Markets | blog | "A Guide to Owning Bonds When They Are Selling Off" — advisers say fixed income still belongs in portfolio | Wealth-mgmt, counter-cyclical framing | Context | Med |
| Investing.com — Market Overview (headlines) | blog (title-only) | "Nasdaq at Record High Amid AI Stocks and Oil Price Drop"; "Strong Durable Goods and AI Spending Keep US Growth Story Running Hot" | Corroborates QQQ resilience + growth-still-hot narrative | Med-HIGH | Med — headline-only, corroborative |
| Bravos Research / George Gammon (YouTube, title-only, 27 items) | youtube | Sensational macro-doom titles: "The Bubble's Final Phase Has Begun," "The Money Supply Is EXPLODING...Hyperinflation?," "The Entire House of Cards Is About To Fall" | Directionally consistent with HIGH_VOL/hawkish narrative | Low confidence | Low — title-only |
| IG France (Alexandre Baradez) (15 items, title-only) | youtube | Daily "MarketLive" technical-analysis streams + 2 Anthropic-valuation items | Unknown content — untranscribed | Low confidence | Low |
| Federal Reserve — Press Releases (~17 remaining items) | blog | Bank enforcement actions, charter approvals, community-bank regulatory-burden proposals | — | — | Low — institutional/regulatory, no market signal |
| Motley Fool (~46 remaining items) | blog | Single-stock deep-dives (Nvidia, Broadcom, Palantir, SpaceX, Microsoft, quantum-computing names, etc.) | — | — | Low — outside ETF-only mandate |
| WSJ Markets (~40 remaining items) | blog | Deals/opinion/single-company stories, "Market Talk" sector roundups, evergreen wealth-mgmt listicles | — | — | Low |
| The Big Picture (Ritholtz) (10 items) | blog | Mostly weekly link-roundup titles ("10 Monday/Tuesday/Wednesday/Thursday/Friday AM Reads") with no excerpted content this batch | — | — | Low-Med — lower usable signal than July edition |
| Investing.com — Stock Market News (10 items, title-only) | blog | Single-company/political headlines (Oracle hack, TikTok settlement, Trump-Xi summit, etc.) | — | — | Low — title-only |
| Seeking Alpha — Market Currents (6 remaining items, title-only) | blog | Single-name/commodity wire items (Eli Lilly, Northrop Grumman, Rio Tinto, grain futures, etc.) | — | — | Low — title-only |
| Finary / Oseille TV / Investing Simplified / Real Vision (61 items, title-only) | youtube | Personal-finance/lifestyle/expat-tax content, single-stock mining video; no direct macro signal | — | — | Low — title-only |
| ETF Trends / CNBC — Economy / CNBC — Finance | — | Zero new items this cycle — all three were high-relevance sources in the 2026-07-13 report | — | — | Flagged as likely feed issue, not "no news" |
