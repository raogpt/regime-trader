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

## 2026-07-25 — Market Intel (regime_trader)
| Source | Type | Item | Regime Signal | Vol Bias | Relevance |
|--------|------|------|----------------|----------|-----------|
| WSJ Markets | blog | Oil crossed $100/barrel first time in 2 months; "Oil Prices Roar Back, Threatening Economy and GOP's Midterm Hopes" — Treasury yields hit 2026 highs | Renewed Iran war escalation (Houthis now threatening Red Sea too), sharper than the 7/13 flare-up | HIGH | High — direct SPY/QQQ/IWM driver |
| WSJ Markets | blog | "Is the Fed About to Hike Rates?"; "Odds of Federal Reserve rate hike surge as oil prices rip higher" (CNBC) | Hawkish Fed repricing intensifying into next week's FOMC decision | HIGH | High — 2-day catalyst filter relevant |
| CNBC — Economy | blog | Kevin Warsh (confirmed Fed Chair) vows "regime change" at the Fed; repeats "family fight," "inflation is a choice"; Dallas Fed's Logan calls for "modestly higher" rates | Hawkish institutional shift, contested internally | HIGH | High — direct HMM Fed-regime input |
| CNBC — Economy | blog | June CPI +3.5% y/y, below 3.8% forecast (energy eased); NY Fed's Williams says inflation "has peaked" | Partial dovish counter-signal, now stale given oil's re-spike | MID | Med — contested/dated by oil move |
| WSJ Markets | blog | "$890 Billion Tech Wipeout Puts Focus on Runaway AI Spending"; Alphabet capex guided to $205B, stock fell despite strong cloud growth; Moody's flags AI-spend credit risk at Amazon/Meta/Alphabet | AI-capex/credit stress escalating, QQQ-concentrated | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | "Semiconductor Crossroads" — chip pullback from profit-taking, valuation, leveraged-trade unwind; Intel -8% despite earnings beat on foundry/AI-spend worries | Tech/semis volatility elevated | HIGH (QQQ-specific) | High |
| ETF Trends (VettaFi) | blog | "The Defensive Shift: This Week's Top 10 ETF Inflows" — capital rotating from concentrated US tech into defensive broad-market, short-duration bonds, commodities | Confirms rotation away from mega-cap tech continuing from 7/13 | Rotation (QQQ risk) | High — direct SPY/QQQ split |
| ETF Trends (VettaFi) | blog | "S&P 500 Snapshot" — 2nd straight weekly decline (longest since March), index 2.6% below June 2 record; T. Rowe Price: small-cap earnings "turning" after 10 quarters of declines | Broad-market softening + IWM tailwind resuming | Mixed-HIGH | High — direct IWM signal |
| CNBC — Finance | blog | Jamie Dimon: "markets underestimate risks," wouldn't buy stocks or Treasurys at current prices | Bearish outlier from major bank CEO | Cautionary | Med-High |
| CNBC — Finance | blog | John Paulson: early stage of long-term gold bull market; Comex gold +1.37% on the week to $4067.60 (WSJ) | Gold now rising WITH oil (unlike 7/13's inflation-fear-driven gold selloff) — reads as genuine flight-to-safety this time | HIGH | Med-High — regime-character shift vs. 7/13 |
| WSJ Markets | blog | WSJ Dollar Index up 5 of 6 sessions; "Dollar Could Stay Strong Until U.S.-Iran Ceasefire Agreed" | Dollar strength alongside gold — classic risk-off, not just rate-differential trade | HIGH | Med-High |
| CNBC — Economy | blog | China Q2 growth slowest since 2022, missed 4.5-5% target, stimulus calls; India CPI still elevated (carried over from 7/13) | Global growth deceleration adds to HIGH_VOL case | MID-HIGH | Med |
| Motley Fool | blog | SpaceX down 23% in 27 trading days post-IPO, worse than 90% of $1B+ IPOs since 2009; Tesla -15% on earnings, off 50% from highs | Single-name but signals fragile risk appetite in high-flying growth names | Sentiment/vol proxy | Low-Med — outside ETF mandate |
| Yahoo Finance — Market News | blog | "Nasdaq lags on angst over AI spending ahead of earnings" — Nasdaq -0.64% Friday vs S&P flat, Dow +0.5% | Direct QQQ-vs-SPY divergence this week | Rotation signal | High |
| Investing.com — Market Overview (title-only, 10 items) | blog (title-only) | "Inflation Fears Pummel Stocks as Yields Surge," "Gulf Escalation Keeps Markets Risk-Off," "FOMC Preview: Fed to Stay on Hold After June's Hawkish Shift," "US Dollar Breakout Puts Bulls in Control" | Consistent with HIGH-vol/hawkish-Fed narrative above; note FOMC-preview headline conflicts with WSJ's "About to Hike" framing — Fed path genuinely contested | HIGH (directionally) | High — but headline-only |
| Liberty Street Economics (NY Fed) | blog | 3-part series on Basel III bank-capital reallocation and nonbank-subsidiary "regulatory arbitrage" within BHCs | Structural banking-system research, not a near-term vol driver | Low | Low-Med — background |
| FRED Blog (St. Louis Fed) | blog | Crude oil → jet fuel → airfare pass-through explainer; Q1 2026 state GDP data (47/50 states grew, national avg 2.1%) | Confirms oil-price transmission mechanism; growth still positive but below prior quarters | Context | Med |
| The Big Picture (Ritholtz) | blog | "Tariffs, Yet Again" — new Section 301 tariffs on 60 countries overnight, legally contested; Vanguard's Joe Davis interview (investor-mistakes piece, content available) | Fresh trade-policy catalyst layered on top of Iran/Fed | HIGH | Med-High |
| WSJ Markets | blog | "Insurers Find Workarounds on Risky Debt as Regulators Play Whac-A-Mole"; "Private-Equity Assets Stuck in 'Zombie Funds' Are at a Record High" | Credit-market plumbing stress, adjacent to AI-bond concerns from 7/13 | Vol risk | Med |
| WSJ Markets (2 items) | blog | "10 of the Best Financial Advisor Companies" / "5 of the Top Financial Advisor Companies for Retirees" | Wealth-mgmt reference, evergreen | n/a | Low |
| The Big Picture (Ritholtz) | blog | Transcript: Jason Wenk, Altruist (RIA custody platform) founder/CEO — full MiB interview | Wealth-mgmt industry context (advisor tooling, not allocation advice) | n/a | Low-Med |
| Motley Fool / Yahoo Finance (multiple) | blog | Social Security COLA forecast cut to 3.7% from 4.7%; "dividend ETFs for retirees" pieces; working-in-retirement SS impact explainer | Wealth-mgmt, evergreen retirement content | n/a | Low |
| Oseille TV | youtube (title-only) | "Ces pays d'Afrique vendent leur passeport (et c'est 100% légal)" | Passport/residency content, not wealth-allocation — title-only, transcript not yet available | Low confidence | Low — flagged for UEMOA/Africa priority once transcript lands |
| George Gammon (3 items) | youtube (title-only) | "$10 Trillion Derivatives Timebomb," "Economic Sign That Can't Be Ignored," "AI Bubble Just Popped" | Titles align directionally with AI-stress/credit themes above but unconfirmed — title-only | Unknown confidence | Med (if confirmed) |
| IG France (7 items) | youtube (title-only) | Weekly "MarketLive" technical-analysis videos, EUR/USD signal video, Iran-oil-rates impact video | Unknown content — title-only | Low confidence | Low |
| Investing Simplified (Prof G) / Bravos Research / Finary (10 items) | youtube (title-only) | Wealth-mgmt/dip-buying/currency-devaluation titles, mostly evergreen framing ("Best Buying Opportunity of 2026") | Unknown content — title-only | Low confidence | Low |
| Real Vision Presents | youtube | No new items this period | — | — | — |
| Motley Fool (~44 remaining items) | blog | Single-stock/AI-name deep dives (Nvidia, Amazon, Oracle, Micron, Bitcoin/XRP, earnings-call transcripts, etc.) | — | — | Low — outside ETF-only mandate |
| ETF Trends (VettaFi) (~40 remaining items) | blog | Niche ETF product coverage (CLOs, nuclear, materials, crypto, robotics) | — | — | Low-Med — product-level, not macro |
| Investing.com — Stock Market News (10 items, title-only) | blog (title-only) | Single-company/deal headlines (Samsung/SK $950B chip deals, Nvidia/SK $500B AI datacenter, China/Trip.com fine) | — | — | Low-Med — title-only, some macro-adjacent (AI capex scale) |
| Seeking Alpha — Market Currents (7 items, title-only) | blog (title-only) | Single-company headlines; one Iran/oil item (China pushing to resume U.S.-Iran talks) echoes de-escalation hope from WSJ/Yahoo Friday coverage | — | — | Low — title-only |
| Federal Reserve (official, 3 items) | blog | Discount-rate meeting minutes (June 8/17); bank-examination and enforcement press releases | Institutional/procedural, low direct signal | Neutral | Low-Med |
