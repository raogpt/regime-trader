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

## 2026-07-07 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| George Gammon | Are We On The Brink Of Another Financial Crisis? | CPI +1.9pp (Jan-May) mirrors 2008 GFC path (+1.6pp Jan-Jul); 2yr UST +~100bps since Mar, matching 2008; oil +65% off Middle East (Hormuz) shock; "subprime" now = private credit; labor data flagged as deteriorating | HIGH — crisis/vol-spike warning, ★★★ channel |
| IG France (Baradez) | MarketLive 2 juillet | VIX ~16-17, retesting 10-15 support zone after late-June bounce to 20; support "fragile" — any catalyst (NFP, Fed, geopolitics) could re-ignite vol | HIGH — confirms current LOW_VOL regime but flags fragility, ★★★ channel |
| IG France (Baradez) | Le Japon sous haute surveillance | BoJ hiked 5x since 2024 (now +1%), JGB 10yr >2.8% (highest since 1990s), yen at 40-yr low, another BoJ hike priced by year-end | MED — yen-carry unwind is a known HIGH_VOL trigger (cf. Aug-2024) |
| IG France (Baradez) | Ce qui fait la différence en trading | No transcript (subs disabled) | LOW |
| IG France (Baradez) | MarketLive (2nd, no title date) | No transcript (subs disabled) | LOW |
| Investing Simplified (Prof G) | The ETF that CRUSHED the S&P500 | VGT 10yr CAGR 25.4%, Mag7-heavy — tech/AI concentration momentum context for QQQ | LOW-MED — QQQ concentration risk context |
| Investing Simplified (Prof G) | $2M Invested - Can I Retire? | FI number = annual spend × 25 (4% rule) | LOW — wealth-mgmt |
| Investing Simplified (Prof G) | The Real Reason Your Portfolio Isn't Growing Faster | SPIVA stats, behavioral investing basics | LOW — wealth-mgmt |
| Investing Simplified (Prof G) | 14 Money Truths from the Bible | DCA vs. single-stock FOMO (Peloton vs QQQ case study) | LOW — wealth-mgmt |
| Finary | À 37 ans, il a parié tout son PEA | Portfolio-analysis format, single-stock concentration risk | LOW — wealth-mgmt |
| Finary | L'erreur que tout le monde fait avec l'argent | Goal-setting psychology, not market-relevant | LOW — wealth-mgmt |
| Oseille TV | 5 videos (CBDC, impôts, expatriation, etc.) | Expat/tax/CBDC commentary, no direct regime signal | LOW — wealth-mgmt, UEMOA/Africa priority (none this batch) |
| Bravos Research | no new videos | — | — |
| Real Vision Presents | no new videos | — | — |

Cross-channel consensus: Gammon + Baradez (2 channels, independent) both flag current low-vol regime as **fragile** — VIX sitting on thin support while GFC-echo macro data (CPI, rates, credit stress) and BoJ/yen tightening build in the background. No trade action taken (regime gate unchanged); logged as elevated-risk watch.

Full report: reports/2026-07-07-youtube-intel.md
