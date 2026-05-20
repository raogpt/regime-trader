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

## 2026-05-20 — YouTube Intel

**17 new videos | 5 channels | 0 transcripts (YouTube blocking) | Analysis: title + channel context**

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | Your Last Chance at Generational Wealth. | BULLISH / near-term dip-buy | Low (title-only) |
| Bravos Research | This Time Is NOT Different. | MID→HIGH_VOL late-cycle warning | Medium |
| Finary | Combien gagnent nos députés ? | Neutral — policy context | Wealth mgmt |
| Finary | Comment devenir riche en étant professeur | Neutral — salaried wealth building | UEMOA ★★★ |
| Finary | Comment le Real Madrid gagne-t-il autant ? | Neutral — revenue diversification | Wealth mgmt |
| Finary | Le cours d'économie que vous auriez dû avoir | Macro-educational | UEMOA ★★ |
| Investing Simplified (Prof G) | Forget NVDA.. These Quantum Stocks Will Be Bigger | QQQ rotation, speculative risk-on | Low |
| Investing Simplified (Prof G) | The only 5 ETFs you'll ever need | ETF flow neutral | Low |
| Investing Simplified (Prof G) | 🚨BREAKING: Expect the Great Market Flip VERY SOON | HIGH_VOL warning | Medium |
| Investing Simplified (Prof G) | Add this ONE Sector to 3 Fund Portfolio | Sector rotation (IWM or tech) | Low |
| IG France (Baradez) ★★★ | MarketLive — tendances graphiques (May 20) | MID_VOL confirmed — normal market | Medium |
| IG France (Baradez) ★★★ | MarketLive — tendances graphiques (May 18) | MID_VOL confirmed — normal market | Medium |
| IG France (Baradez) ★★★ | MarketLive — tendances graphiques (May 13) | MID_VOL confirmed — normal market | Medium |
| Real Vision ★★★ | The Next-Gen Dollar: Stablecoins & Payments | USD/de-dollarization background | Low |
| Real Vision ★★★ | Up 13% Overnight!? Why Hyperliquid Exploded! | Crypto risk-on froth → vol watch +1-3wk | Low-Med |
| Real Vision ★★★ | Why Sui Is Building AI Agent Infrastructure | Non-correlated / speculative | None |
| Real Vision ★★★ | Can Sui Become the Internet's Money Layer? | Non-correlated / speculative | None |

**Consensus:** MID_VOL sustained (IG France ★★★ running daily MarketLive = market in normal chartable state). Minority HIGH_VOL warning from Bravos + Prof G. Crypto risk-on froth (Hyperliquid +13%) = late-cycle speculative indicator — watch for vol pickup 1-3 weeks. Real Vision pivoted to crypto conference; traditional macro signal LOW this cycle.

**ETF bias:** QQQ slight edge (tech rotation active). IWM neutral. SPY core.

**Action:** No regime change triggered. Maintain MID_VOL positioning. Elevate alert threshold for HIGH_VOL trigger.

**Full report:** reports/2026-05-20-youtube-intel.md
