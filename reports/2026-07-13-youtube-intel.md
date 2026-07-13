# YouTube Intel — 2026-07-13

## ⚠️ Data Limitation
YouTube blocked all transcript requests from this cloud IP (`RequestBlocked` — cloud-provider IPs are commonly banned by YouTube's transcript endpoint). **19/19 new videos returned no transcript.** Everything below is inferred from **titles only** — treat as noise, not signal. No HMM-relevant conclusion should be drawn from this report alone.

## Executive Summary (vol regime implications)
No transcript-grounded regime read possible today. Title scan shows a cluster of high-alarm macro titles (George Gammon x2, Bravos Research x1) using "crisis/bubble/broke" framing, plus one IG France title explicitly referencing a VIX spike-then-fade. This is consistent with — but does not confirm — a recent vol pop that's mean-reverting. **Do not feed into HMM confidence scoring; titles are clickbait-optimized and unreliable as standalone signal.**

## Per-Video (title-only, no transcript)

| Channel | Title | Published | Inferred Thesis | Regime Signal | Confidence |
|---|---|---|---|---|---|
| George Gammon | The Next Subprime Crisis Was Just Triggered...And It's Bigger Than 2008 | 07-11 | Credit stress narrative | Risk-off (unconfirmed) | Very Low |
| George Gammon | This Multi Trillion Dollar Bubble May Have Just Broken The Economy | 07-09 | Bubble-bursting narrative | Risk-off (unconfirmed) | Very Low |
| Bravos Research | Something Just Broke in the Financial System... | 07-07 | Systemic stress narrative | Risk-off (unconfirmed) | Very Low |
| IG France | VIX (volatilité) : un rebond marqué...puis une détente | 07-10 | VIX spiked, then eased | HIGH→MID vol reversion (unconfirmed) | Very Low |
| IG France | Le Japon sous haute surveillance (chute du yen, BoJ, inflation) | 07-06 | JPY/BoJ catalyst | Possible cross-asset vol trigger | Very Low |
| IG France | MarketLive ×3 (07-13, 07-10, 07-07) | — | Routine daily technical recap | None discernible | n/a |
| IG France | Fibonacci & Retracements: Zones d'Entrée | 07-09 | TA methodology video | None | n/a |
| Prof G | 🚨BREAKING: 2026 Market Outlook (Expect Major Change in July) | 07-11 | Vague "major change" teaser | Unclear | Very Low |
| Prof G | How to Make $4,100/Month in Dividends | 07-08 | Income strategy | None | n/a |
| Prof G | $2M Invested - Can I retire soon? | 07-06 | Retirement planning | None | n/a |
| Finary | Ce qui lui rapporte le plus n'a rien à voir avec la bourse | 07-12 | Non-market wealth topic | None | n/a |
| Finary | 🚨 Vous devez migrer vos cryptos ? | 07-10 | Crypto platform migration advisory | None (not SPY/QQQ/IWM relevant) | n/a |
| Finary | Le plan pour devenir (très) riche | 07-08 | Wealth-building framework | None | n/a |
| Oseille TV | Pourquoi la plupart des gens ne veulent pas être libres | 07-11 | Lifestyle/mindset | None | n/a |
| Oseille TV | L'illusion qui vous empêche de quitter la France | 07-10 | Expat lifestyle | None | n/a |
| Oseille TV | Assurance vie : pourquoi le Luxembourg écrase la France ? | 07-07 | Insurance/tax wrapper comparison | None | Wealth-mgmt relevant |
| Oseille TV | 6 mois de prison pour un journaliste qui a enquêté | 07-06 | Non-financial/press freedom | None | n/a |

## Cross-Channel Consensus
Cannot establish — no transcript content to compare. Title-level pattern (3 channels using crisis/bubble framing same week) is a weak, unconfirmed coincidence signal at best; these channels routinely use alarmist titles regardless of underlying content.

## Wealth Management TLDR
1. **Oseille TV — Assurance vie Luxembourg vs France**: Title suggests Luxembourg life-insurance wrappers outperform French ones on flexibility/tax. No transcript to confirm mechanism — flag for manual review, potentially relevant to UEMOA/Africa-adjacent expat tax planning.
2. **Finary — crypto migration alert**: Title implies a platform/regulatory deadline forcing crypto migration (possibly MiCA-related). No transcript — needs manual follow-up given urgency framing ("Vous devez migrer").
3. No other wealth-mgmt content had extractable substance from titles alone this cycle.

## Recommendation
Consider adding a fallback transcript source (e.g., proxy rotation per the youtube-transcript-api README, or a non-cloud transcript proxy) if title-only intel proves insufficient over multiple cycles — current setup has produced zero usable transcript content since inception.
