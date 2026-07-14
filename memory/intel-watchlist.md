# Market Intel Watchlist

Sources monitored daily for market intelligence (regime signals + wealth mgmt).
To add a source: ask Claude in a conversation session.
Last updated: 2026-07-14

## Active Sources

| ID | Source | Type | URL | Feed URL | Lang | Categories | Signal Score | Last Checked |
|----|--------|------|-----|----------|------|------------|--------------|-------------|
| 1 | Oseille TV | youtube | https://www.youtube.com/@oseilletv | https://www.youtube.com/feeds/videos.xml?channel_id=UC2hIOaqIHLi2qABoCRxjx_Q | FR | wealth-mgmt, entrepreneurship, expat | — | 2026-07-14 |
| 2 | Bravos Research | youtube | https://www.youtube.com/channel/UCOHxDwCcOzBaLkeTazanwcw | https://www.youtube.com/feeds/videos.xml?channel_id=UCOHxDwCcOzBaLkeTazanwcw | EN | macro, market-signal, trade-ideas | — | 2026-07-14 |
| 3 | Finary | youtube | https://www.youtube.com/@Finary | https://www.youtube.com/feeds/videos.xml?channel_id=UCRCCAnVyzDTcqNYh0pDcq7Q | FR | wealth-mgmt, portfolio, budgeting | — | 2026-07-14 |
| 4 | Investing Simplified (Prof G) | youtube | https://www.youtube.com/channel/UCr4XXQznhlgfzo4mwOgkF8w | https://www.youtube.com/feeds/videos.xml?channel_id=UCr4XXQznhlgfzo4mwOgkF8w | EN | ETF, stocks, retirement, crypto | — | 2026-07-14 |
| 5 | George Gammon | youtube | https://www.youtube.com/channel/UCpvyOqtEc86X8w8_Se0t4-w | https://www.youtube.com/feeds/videos.xml?channel_id=UCpvyOqtEc86X8w8_Se0t4-w | EN | macro, credit-cycles, monetary-policy, trade-ideas | ★★★ | 2026-07-14 |
| 6 | IG France (Alexandre Baradez) | youtube | https://www.youtube.com/channel/UCQ0A2MqahcnKlToIJ_giSEg | https://www.youtube.com/feeds/videos.xml?channel_id=UCQ0A2MqahcnKlToIJ_giSEg | FR | macro, technical-analysis, market-daily | ★★★ | 2026-07-14 |
| 7 | Real Vision Presents | youtube | https://www.youtube.com/channel/UCBH5VZE_Y4F3CMcPIzPEB5A | https://www.youtube.com/feeds/videos.xml?channel_id=UCBH5VZE_Y4F3CMcPIzPEB5A | EN | macro, institutional, liquidity-cycles, commodities | ★★★ | 2026-07-14 |
| 8 | Federal Reserve — Press Releases | blog | https://www.federalreserve.gov | https://www.federalreserve.gov/feeds/press_all.xml | EN | fed-policy, rates, official | ★★★ | 2026-07-14 |
| 9 | Liberty Street Economics (NY Fed) | blog | https://libertystreeteconomics.newyorkfed.org | https://libertystreeteconomics.newyorkfed.org/feed/ | EN | macro, research, banking, liquidity | ★★★ | 2026-07-14 |
| 10 | FRED Blog (St. Louis Fed) | blog | https://fredblog.stlouisfed.org | https://fredblog.stlouisfed.org/feed/ | EN | macro, data-explainer | ★★ | 2026-07-14 |
| 11 | The Big Picture (Ritholtz) | blog | https://ritholtz.com | https://ritholtz.com/feed/ | EN | macro, market-commentary, sentiment | ★★ | 2026-07-14 |
| 12 | WSJ Markets | blog | https://www.wsj.com/market-data | https://feeds.content.dowjones.io/public/rss/RSSMarketsMain | EN | market-news, breaking | ★★ | 2026-07-14 |
| 13 | ETF Trends (VettaFi) | blog | https://www.etftrends.com | https://www.etftrends.com/feed/ | EN | ETF, rotation, SPY, QQQ, IWM | ★★★ | 2026-07-14 |
| 14 | CNBC — Economy | blog | https://www.cnbc.com/economy/ | https://www.cnbc.com/id/20910258/device/rss/rss.html | EN | macro, fed-policy, labor-data, inflation | ★★★ | 2026-07-14 |
| 15 | Investing.com — Market Overview | blog | https://www.investing.com | https://www.investing.com/rss/market_overview.rss | EN | macro, analysis, fed-policy, geopolitics | ★★★ | 2026-07-14 |
| 16 | CNBC — Finance | blog | https://www.cnbc.com/finance/ | https://www.cnbc.com/id/10000664/device/rss/rss.html | EN | market-news, fed-policy, deals | ★★ | 2026-07-14 |
| 17 | Investing.com — Stock Market News | blog | https://www.investing.com | https://www.investing.com/rss/news_25.rss | EN | market-news, sector, geopolitics | ★★ | 2026-07-14 |
| 18 | Yahoo Finance — Market News (S&P 500) | blog | https://finance.yahoo.com | https://feeds.finance.yahoo.com/rss/2.0/headline?s=%5EGSPC&region=US&lang=en-US | EN | market-news, index-level | ★★ | 2026-07-14 |
| 19 | Motley Fool | blog | https://www.fool.com | https://www.fool.com/feeds/index.aspx | EN | stock-picks, wealth-mgmt, sentiment | ★ | 2026-07-14 |
| 20 | Seeking Alpha — Market Currents | blog | https://seekingalpha.com | https://seekingalpha.com/market_currents.xml | EN | market-news, earnings-calendar, movers | ★ | 2026-07-14 |

## Type Legend
- `youtube` — RSS gives title + publish date. Live transcript fetch from this
  environment's IP is blocked (YouTube/Google bot-detection checkpoint,
  redirects to `google.com/sorry/index` — IP-reputation-based, not
  client-specific). `intel_monitor.py` instead checks `memory/transcripts/`
  for a cached transcript and, if absent, queues the video to
  `memory/transcript-queue.json` for `fetch_transcripts.py` to fetch on a
  residential IP (self-hosted GitHub Actions runner — see
  `.github/workflows/fetch-transcripts.yml`). Treat YouTube items as
  **title-only, low confidence** until a cached transcript appears
  (`content_available: true`).
- `blog` — RSS is fetched directly (no bot-wall issue observed). Most sources'
  entries carry full/teaser body text alongside the title — treat those as
  **higher confidence** than title-only YouTube signal (paywalled sources
  like WSJ may only expose a teaser). **Exception:** Investing.com (both
  feeds, IDs 15/17) and Seeking Alpha — Market Currents (ID 20) return
  **headline-only** RSS entries — no description/summary/content field at
  all, confirmed by inspecting the parsed feed directly, not a fetch bug.
  Treat those three specifically as **title-only, same confidence tier as
  YouTube**, despite being `type=blog`.

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
- **Investopedia** — every RSS path tested (`/rss`, `/feed`, `/feedbuilder/...`,
  category feeds) returns `HTTP 402 Payment Required` pointing at
  `support@people.inc` — their new owner (People Inc / Dotdash Meredith) has
  gated the feed behind a content-licensing wall, not a normal user paywall.
  Not accessible without a commercial licensing arrangement; a subscription
  login wouldn't fix this since it's a machine/API-access gate, not a
  reader paywall.
- **Barron's** — RSS returns `HTTP 403`; blocked at the edge, no accessible
  feed found.
- **Investing.com — All News** (`/rss/news.rss`) — mixes in non-financial
  wire content (a general-news item about an earthquake showed up in
  testing); the narrower `market_overview` and `news_25` feeds (added above)
  cover the same publisher with tighter relevance. Your Investing.com Pro
  subscription doesn't change what's exposed over public RSS — Pro adds
  site features (alerts, ad-free, extra data), not a richer feed; the free
  RSS endpoints already carry full article text, so there's nothing to gain
  by authenticating the feed fetch itself.
- **Seeking Alpha — All Articles** (`/feed.xml`) — dominated by single-name
  deep-dive analysis (e.g. individual small/mid-cap earnings previews),
  which cuts directly against this bot's ETF-only mandate. Kept the
  `market_currents.xml` (breaking news / movers) feed instead, which is
  still noisy (some non-market items slip in) but closer to market-wide
  relevance.
- **Yahoo Finance — general Top Stories** (`/news/rssindex`) — noisier and
  more single-stock-pick-heavy than the S&P 500-framed feed added above;
  skipped in favor of the narrower one.

## Signal Score Legend
- ★★★ Highly actionable (generated 2+ good trade ideas / official source)
- ★★  Occasionally useful (good macro context)
- ★   Background noise (informational only)
- —   Not yet rated

## Adding Sources
Tell Claude: "Add [source name] to the intel watchlist" in any conversation.
Claude will find the feed URL (verifying it resolves and is fresh, not
guessed from memory) and update this file.
