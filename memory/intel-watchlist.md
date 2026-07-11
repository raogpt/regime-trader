# Market Intel Watchlist

Sources monitored daily for market intelligence (regime signals + wealth mgmt).
To add a source: ask Claude in a conversation session.
Last updated: 2026-07-11

## Active Sources

| ID | Source | Type | URL | Feed URL | Lang | Categories | Signal Score | Last Checked |
|----|--------|------|-----|----------|------|------------|--------------|-------------|
| 1 | Oseille TV | youtube | https://www.youtube.com/@oseilletv | https://www.youtube.com/feeds/videos.xml?channel_id=UC2hIOaqIHLi2qABoCRxjx_Q | FR | wealth-mgmt, entrepreneurship, expat | — | 2026-07-11 |
| 2 | Bravos Research | youtube | https://www.youtube.com/channel/UCOHxDwCcOzBaLkeTazanwcw | https://www.youtube.com/feeds/videos.xml?channel_id=UCOHxDwCcOzBaLkeTazanwcw | EN | macro, market-signal, trade-ideas | — | 2026-07-11 |
| 3 | Finary | youtube | https://www.youtube.com/@Finary | https://www.youtube.com/feeds/videos.xml?channel_id=UCRCCAnVyzDTcqNYh0pDcq7Q | FR | wealth-mgmt, portfolio, budgeting | — | 2026-07-11 |
| 4 | Investing Simplified (Prof G) | youtube | https://www.youtube.com/channel/UCr4XXQznhlgfzo4mwOgkF8w | https://www.youtube.com/feeds/videos.xml?channel_id=UCr4XXQznhlgfzo4mwOgkF8w | EN | ETF, stocks, retirement, crypto | — | 2026-07-11 |
| 5 | George Gammon | youtube | https://www.youtube.com/channel/UCpvyOqtEc86X8w8_Se0t4-w | https://www.youtube.com/feeds/videos.xml?channel_id=UCpvyOqtEc86X8w8_Se0t4-w | EN | macro, credit-cycles, monetary-policy, trade-ideas | ★★★ | 2026-07-11 |
| 6 | IG France (Alexandre Baradez) | youtube | https://www.youtube.com/channel/UCQ0A2MqahcnKlToIJ_giSEg | https://www.youtube.com/feeds/videos.xml?channel_id=UCQ0A2MqahcnKlToIJ_giSEg | FR | macro, technical-analysis, market-daily | ★★★ | 2026-07-11 |
| 7 | Real Vision Presents | youtube | https://www.youtube.com/channel/UCBH5VZE_Y4F3CMcPIzPEB5A | https://www.youtube.com/feeds/videos.xml?channel_id=UCBH5VZE_Y4F3CMcPIzPEB5A | EN | macro, institutional, liquidity-cycles, commodities | ★★★ | 2026-07-11 |
| 8 | Federal Reserve — Press Releases | blog | https://www.federalreserve.gov | https://www.federalreserve.gov/feeds/press_all.xml | EN | fed-policy, rates, official | ★★★ | never |
| 9 | Liberty Street Economics (NY Fed) | blog | https://libertystreeteconomics.newyorkfed.org | https://libertystreeteconomics.newyorkfed.org/feed/ | EN | macro, research, banking, liquidity | ★★★ | never |
| 10 | FRED Blog (St. Louis Fed) | blog | https://fredblog.stlouisfed.org | https://fredblog.stlouisfed.org/feed/ | EN | macro, data-explainer | ★★ | never |
| 11 | The Big Picture (Ritholtz) | blog | https://ritholtz.com | https://ritholtz.com/feed/ | EN | macro, market-commentary, sentiment | ★★ | never |
| 12 | WSJ Markets | blog | https://www.wsj.com/market-data | https://feeds.content.dowjones.io/public/rss/RSSMarketsMain | EN | market-news, breaking | ★★ | never |
| 13 | ETF Trends (VettaFi) | blog | https://www.etftrends.com | https://www.etftrends.com/feed/ | EN | ETF, rotation, SPY, QQQ, IWM | ★★★ | never |

## Type Legend
- `youtube` — RSS gives title + publish date only. Transcript extraction is NOT
  attempted: this environment's egress IP is caught by YouTube/Google's
  bot-detection checkpoint (redirects to `google.com/sorry/index`, a CAPTCHA
  wall) before any page or caption content loads. This is IP-reputation-based,
  not client-specific — a headless browser from the same IP hits the same wall.
  Treat all YouTube signal as **title-only, low confidence**.
- `blog` — RSS is fetched directly (no bot-wall issue observed); the entry's
  full/teaser content is analyzed alongside the title. Treat as **higher
  confidence** than title-only YouTube signal, though paywalled sources
  (e.g. WSJ) may only expose a teaser in the feed.

## Considered but excluded
- **Calculated Risk** (calculatedriskblog.com) — feed resolves but is stale
  (most recent entry Jan 2026 as of this write-up); re-check before adding.
- **ZeroHedge** — feed is live and frequently updated, but mixes legitimate
  macro/markets content with unrelated political/tabloid posts in the same
  feed with no reliable category filter. Left out by default; add manually
  if you want the extra signal and are OK filtering noise in the analysis
  step.
- **MarketWatch Top Stories** — mostly general consumer-finance content
  (travel, personal budgeting), not macro/regime-relevant enough to justify
  a slot; WSJ Markets covers the same publisher family with tighter focus.

## Signal Score Legend
- ★★★ Highly actionable (generated 2+ good trade ideas / official source)
- ★★  Occasionally useful (good macro context)
- ★   Background noise (informational only)
- —   Not yet rated

## Adding Sources
Tell Claude: "Add [source name] to the intel watchlist" in any conversation.
Claude will find the feed URL (verifying it resolves and is fresh, not
guessed from memory) and update this file.
