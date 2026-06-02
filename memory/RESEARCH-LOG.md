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

---

## 2026-06-02 — YouTube Intel

_17 new videos across 6 channels (7-day lookback, first run). Transcripts blocked — cloud IP. Title-only analysis._

| Channel | Video | Regime Signal | Relevance |
|---|---|---|---|
| Bravos Research | The UNTHINKABLE is About to Happen to Stocks (Emergency Update) | HIGH_VOL / RISK-OFF | ★★★ HIGH |
| Investing Simplified | 🚨CAUTION: Quiet Tax the New Fed is About to Charge Every Investor | MID_VOL / FED RISK | ★★ HIGH |
| Real Vision | It Said 2-Months... It Did It In Minutes! | HIGH_VOL (inferred) | ★★ MED |
| Real Vision | Sui Miami crypto conference (4 videos) | NOT RELEVANT | ★ LOW |
| IG France (Baradez) | MarketLive x3 + RSI masterclass | NEUTRAL-WATCHFUL | ★★ MED |
| Finary | Japan demographic collapse — economy collapse? | RISK-OFF / global macro | ★ MED |
| Finary | Consumer finance, royals, benchmark | WEALTH MGMT | ★ LOW |
| Oseille TV | Votre argent en banque n'est plus à vous ! | RISK-OFF / banking | ★★ WEALTH PRIORITY |

**Cross-channel consensus**: 2+ EN channels CAUTION/bearish. Zero bullish/LOW_VOL signal.
**HMM implication**: Stay MID_VOL parameters. Do not increase allocation until 3 confirming bars.
**Full report**: reports/2026-06-02-youtube-intel.md
