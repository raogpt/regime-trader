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

## 2026-07-12 — YouTube Intel

NOTE: youtube-transcript-api blocked by YouTube on this cloud IP (all 18/18 transcripts failed —
"IPBlocked" error). Analysis below is title-only, low-confidence. Full transcript analysis needs
a proxy per youtube-transcript-api README.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| George Gammon | The Next Subprime Crisis Was Just Triggered...And It's Bigger Than 2008 | Risk-off / credit stress framing | High (title-only) |
| George Gammon | This Multi Trillion Dollar Bubble May Have Just Broken The Economy | Risk-off / bubble-burst framing | High (title-only) |
| Bravos Research | Something Just Broke in the Financial System... | Risk-off / systemic stress framing | High (title-only) |
| Investing Simplified (Prof G) | BREAKING: 2026 Market Outlook (Expect Major Change in July) | Regime-shift call flagged for July | Medium (title-only) |
| IG France | VIX (volatilité): un rebond marqué...puis une détente | Vol spike then cooling — HIGH_VOL→MID_VOL transition | High (title-only) |
| IG France | Le Japon sous haute surveillance des marchés (yen, BoJ, inflation) | BoJ/yen macro catalyst | Medium (title-only) |
| IG France | MarketLive x2, Fibonacci & Retracements | General TA content | Low |
| Finary | 🚨 Vous devez migrer vos cryptos ? | Crypto risk-mgmt, not SPY/QQQ/IWM relevant | Low |
| Finary | Le plan pour devenir (très) riche / À 25 ans... | Wealth-mgmt allocation content | Low (see report) |
| Oseille TV | Assurance vie : pourquoi le Luxembourg écrase la France ? | Wealth-mgmt / tax (life insurance wrapper) | Medium — wealth mgmt |
| Oseille TV | L'illusion qui vous empêche de quitter la France | Expat/tax wealth-mgmt | Low |
| Oseille TV | 2 other videos (non-financial) | — | None |
| Real Vision Presents | No new videos | — | — |

Full report: reports/2026-07-12-youtube-intel.md
