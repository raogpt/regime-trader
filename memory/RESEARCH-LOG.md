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

## 2026-05-29 — YouTube Intel

> Transcripts unavailable (cloud IP block by YouTube). Analysis based on video titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Entire Financial System Just Changed Forever… | ⚠️ HIGH — structural macro shift narrative | ★★★ |
| Investing Simplified | 🚨 Investors Could Get Blindsided.. (CRUCIAL Market Update 2026) | ⚠️ MID-HIGH — volatility warning, potential risk-off | ★★★ |
| IG France (Baradez) | MarketLive x4 + RSI Method | NEUTRAL — technical analysis, elevated activity signals active market | ★★★ |
| Real Vision | RWAs: Every Asset Will Be Onchain — The $100T Migration | NEUTRAL-BULLISH — structural crypto/DeFi rotation | ★★ |
| Real Vision | From Lagos to the World: the Future of African Payments | WEALTH-MGMT — UEMOA/Africa fintech | ★★★ |
| Finary | Le Japon perd 1 habitant toutes les 35 secondes… | MID — Japan economic risk, global growth concern | ★★ |
| Finary | Le crédit caché de millions de Français | MID — hidden credit exposure, banking risk | ★★ |
| Oseille TV | Votre argent en banque n'est plus à vous ! 🏦 | ⚠️ RISK-OFF — bank deposit safety narrative, bail-in concern | ★★★ |
| Investing Simplified | 5 Best Stocks & Hottest Investing Sectors for 2026? | MIXED — sector rotation hints, individual stocks (ignore picks) | ★ |
| Investing Simplified | The Only Retirement Video You Ever Need to Watch | WEALTH-MGMT — passive income/ETF allocation | ★★ |

**Cross-channel consensus (2+ channels):** Financial system disruption narrative (Bravos + Real Vision) → watch for structural vol regime shift. Banking/credit concern (Oseille + Finary) → mild risk-off bias for traditional finance.

**HMM Regime Implication:** MID→HIGH vol bias. No immediate action trigger (no stable 3-bar confirmation). Monitor SPY/IWM for risk-off rotation vs QQQ tech resilience.
