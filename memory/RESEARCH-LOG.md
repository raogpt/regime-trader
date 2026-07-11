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

## 2026-07-11 — YouTube Intel

First check (all channels previously "never checked", 7-day lookback). 17 new
videos across 6 channels; transcripts blocked by YouTube for 16/17 (cloud IP
rate-limited). Full report: `reports/2026-07-11-youtube-intel.md`.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|----------------|-----------|
| George Gammon | This Multi Trillion Dollar Bubble May Have Just Broken The Economy | GDPNow collapsed 4.5%→1.2%, weak NFP (57K vs ~115K, -74K revisions), Blackstone AI-datacenter cancellation — recession-risk/HIGH_VOL lean (transcript-confirmed, medium confidence) | High |
| Bravos Research | Something Just Broke in the Financial System... | Alarmist recession-risk framing, consistent w/ Gammon (title-only, unconfirmed) | Medium |
| IG France | VIX (volatilité): un rebond marqué...puis une détente | Vol spike already fading as of 2026-07-10 (title-only) | Medium |
| IG France | Le Japon sous haute surveillance des marchés (yen, BoJ) | Possible yen/carry-trade vol catalyst (title-only, unconfirmed) | Low |
| IG France | 2x MarketLive round-ups, Fibonacci technical entry piece | No transcript, generic market-daily/technical content | Low |
| Finary | 3 videos (crypto migration, "get rich" plan, concentrated PEA risk) | No regime signal; wealth-mgmt/investor-education | Low |
| Investing Simplified (Prof G) | 3 videos (dividend income, $2M retirement, portfolio growth) | No regime signal; wealth-mgmt | Low |
| Oseille TV | 3 videos (France-exit/expat, Luxembourg assurance-vie, press story) | No regime signal; no Africa/UEMOA content this cycle | Low |
| Real Vision Presents | — | No new videos | — |

**Consensus:** Gammon (confirmed) + Bravos (title-only) both flag recession-risk /
"something broke" in the 07-07 to 07-09 window; IG France's VIX title suggests the
associated vol spike is already cooling. Soft 2-channel confirmation only — HMM's own
regime signal should lead. No SPY/QQQ/IWM rotation signal found.
**Data quality:** transcript fetch structurally blocked from this cloud IP; see report
for detail.
