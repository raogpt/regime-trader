# YouTube / Market Intel — 2026-11-21 (regime_trader)

**Data caveat:** 194 new items since 2026-11-14 (24 YouTube, 170 blog/news). YouTube transcripts still blocked from this environment → 23 more queued, 168 pending in `memory/transcript-queue.json`. **All YouTube rows are title-only → low confidence.** Verified signal comes from WSJ, Yahoo, Motley Fool market wraps, Ritholtz, Fed. Feeds that failed today (not covered): FRED Blog (timeout), ETF Trends (403), CNBC Economy + Finance (403). FOMC Oct 27–28 minutes released 11/18: the feed has the title only, and the hawkish read below comes from WSJ's summary. `youtube_monitor.py` / `youtube-watchlist.md` no longer exist; used `intel_monitor.py` / `intel-watchlist.md` instead. First check run failed silently (pip went to the wrong interpreter); deps reinstalled via `python -m pip` and rerun.

## Executive Summary (vol regime implications)
- **HIGH-vol regime, now in full drawdown.** S&P 500 −8.6% on the week, −3.7% Fri 11/20 to 6,910 → **in correction** (first close < 7,000 since April); 7 down days in a row (longest streak since Feb 2020). Dow also in correction (−1.93% Fri to 48,147). Nasdaq −5.3% Fri to ~22,618, **down for the year**, ~18% below the 10/6 record close (27,600). Nasdaq-100 had its worst week since 2020; WSJ: mega-cap tech "skirted bear-market territory". Fear gauge "soaring" (Yahoo/IBD). ~$4T of AI market value wiped out (WSJ).
- **Driver = AI trade unwinding:** Nvidia −23% on the week, −14% Fri (SEC civil probe on disclosures + California AG subpoena, after Jensen Huang's departure); Broadcom −12% Fri; Anthropic IPO (Thu 11/19) +17% on day 1, then −8.5% Fri and briefly only 5 cents above its IPO price on day 2 — it did not revive the trade. Global contagion: Europe and Asia tech also fell; Bitcoin < $60k.
- **Hawkish rates despite the selloff:** FOMC minutes (11/18) showed "mounting inflation concerns" → dollar index at a 52-week high; gold at a ~15-month low "amid concerns the Fed will continue raising interest rates" (−38% from January per Investing.com). 10Y slipped to 4.91% Fri (WSJ: "Treasury yields plunge") — some flight to quality, but the level is still high. **No Fed put priced** → bad for vol mean-reversion.
- **Oil not the issue:** crude down for the 3rd straight week (Middle East supply rising); gasoline easing. Energy and utilities were the only gaining sectors on Fri.
- **ETF tilt:** **QQQ is the epicenter** (semis, mega-cap AI). SPY is in correction, but its defensives cushion it (Dow fell less). IWM: data on small caps is thin in today's feeds; it is less AI-exposed, but hike pricing is a headwind → no long conviction. Relative order of risk: QQQ > SPY ≳ IWM.
- **Catalysts within 2 days:** Thanksgiving week (shortened session Fri 11/27), Black Friday spending read, Amazon re:Invent on 11/30. Lower-tier events, but liquidity will be thin into the holiday, which amplifies vol. The Nvidia SEC/CA probes add headline risk that can land at any time.
- **Contrarian voices:** Goldman sees the S&P +26% over 12 months; Ritholtz (11/15) says tech volatility ≠ broad weakness, but warned 11/19 of an "intraday reversal" (gap up, close on the lows), which then played out with downside follow-through.
- **Bot action: none.** TRADE-LOG shows no positions. The HMM should be printing a HIGH-vol / bearish state; act only if confidence ≥55% and the state holds for 3 bars. After a shock this size, expect unstable bars and smaller sizes.

## Per-video (YouTube, title-only)
| Channel | Title (date) | Thesis (inferred) | Regime signal | Confidence |
|---|---|---|---|---|
| Bravos Research | "Don't Fall For It…" (11/15) | Warns against the bounce / dip-buy (reverses the 11/08 "opportunity" call) | Bearish; matched the following week | Low |
| George Gammon | "You Won't Believe The Fed's New Plan (Interest Rate Reset)" (11/14) | Fed policy shift | Rates uncertainty | Low |
| George Gammon | "The Stock Market May Not Survive What Just Happened…" (11/19) | Crash risk | Bearish / high vol | Low |
| Investing Simplified | "What a mess.. How to invest" (11/14) | Navigating the volatility | Elevated vol | Low |
| Investing Simplified | "The Only 5 ETFs you NEED 2027" (11/16); "Overhyped Investing Habits" (11/17) | Long-term passive ETFs | Neutral | Very low |
| Investing Simplified | "This MASSIVE Investing Opportunity Won't Last (6 Top Growth Stocks 2027)" (11/19) | Buy the growth dip | Risk-on, retail dip-buying (wrong-footed 11/20) | Low |
| Finary | "Comment Claude a doublé ChatGPT" (11/15); "Le plus gros scandale de l'IA" (11/17); GTA VI ×2 (11/18) | AI competition / Nvidia scandal; gaming | AI-trade caution | Low |
| Oseille TV | 13 shorts: Panama tax residency, Thailand, US bank account, PEA/PER, Revolut, a Russian ETF that vanished (11/14–11/20) | Expat / tax / wealth themes | None (regime) | Very low |

## Cross-channel consensus (2+ sources agree)
- **HIGH-vol regime confirmed:** WSJ, Yahoo, Motley Fool, Ritholtz, Investing.com ("Extreme Fear: Nasdaq Is Facing Another Major Selloff"), plus Gammon and Bravos titles. High confidence on the *level* of vol. Direction: bearish momentum, with capitulation risk (worst week since 2020, fear gauge spiking).
- **AI trade is the epicenter:** WSJ ("End of the No-Brainer AI Trade", "AI Boom Turns to Bust"), Barron's via Ritholtz, Motley Fool, Investing.com ("Markets Reassess the AI Growth Story for 2027"), Finary. → QQQ underweight vs SPY.
- **Hawkish Fed + strong dollar:** WSJ (minutes, dollar at 52-week high, gold low on hike expectations), Motley Fool ("newly identified source of inflation"), Investing.com ("Dollar Shines"). Medium-high confidence; partly offset by the Friday yield drop and falling oil.
- **Retail dip-buyers wrong-footed:** Investing Simplified (11/19 growth buy), Anthropic retail allocation (up to 20% of shares) slid on day 2. Contrarian sentiment marker; low confidence.
- **Cyber/outage risk is a new tail:** Ritholtz Friday reads (vulnerabilities at ~7× the monthly average, AI-assisted attacks), WSJ (Visa/Mastercard/JPM data leak; "Outages Were Only the Start"). Low-medium; it hit financials 11/19.

## Wealth Management TLDR
1. **Don't panic-sell a correction; rebalance into it.** S&P corrections come about every 1.5 years (Motley Fool); Goldman has a 12-month +26% call. Use set rebalancing bands rather than discretionary dip-buying in a market that keeps making new lows.
2. **Check AI concentration.** The Nasdaq is negative YTD and Nvidia is −23% in a week. Look through index and "value" funds (see 11/14 note) to see how much of the portfolio is AI exposure.
3. **Inflation protection** (WSJ 11/20 "Grabbing Inflation Protection Now Is a No-Brainer"): with the Fed still hawkish and the 10Y near 4.9%, TIPS / short duration beat long nominal bonds. Gold failed as a hedge this cycle (−38% from January).
4. **Estate planning lesson** (Yahoo 11/21): Huang moved ~60M NVDA shares into a family trust years ahead, avoiding gift/estate tax on the appreciation. Concentrated founder or employee stock → set up a trust/transfer plan early, before a drawdown or event. US-specific; check your jurisdiction.
5. **US retirement milestones** (WSJ via Ritholtz): catch-up contributions from age 50 (Roth-only above $150k income); Rule of 55 for penalty-free 401(k) withdrawals. Applies only if you have US accounts.
6. **France/expat (Oseille TV, title-only):** Panama territorial taxation (foreign income untaxed; residency < $10k), opening a US bank account, PEA/PER origins, "Revolut doesn't diversify your accounts" (counterparty/deposit-guarantee concentration), a Russian ETF wiped out overnight (sanctions/custody risk). Takeaways: spread cash across institutions and jurisdictions, and know the custody chain of exotic ETFs. Verify tax residency rules with an advisor; do not act on titles.
7. **UEMOA/Africa (PRIORITY):** **no relevant content this week** from any of the 20 sources. Gap persists for the 4th run. Recommendation stands: add a dedicated UEMOA/BRVM/Africa wealth source to `memory/intel-watchlist.md`.
