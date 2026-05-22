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

## 2026-05-22 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | In 6 Months, It's All Over. | HIGH_VOL / BEARISH (6-month horizon) | ★★★ |
| Bravos Research | Your Last Chance at Generational Wealth. | UNCERTAIN — late-cycle buy or top warning | ★★★ |
| Investing Simplified (Prof G) | 🚨 Expect the Great Market Flip (VERY SOON) | REGIME CHANGE — MID→HIGH_VOL transition | ★★ |
| Investing Simplified (Prof G) | Forget NVDA.. These Quantum Stocks Could Be Bigger | RISK-ON / QQQ-positive, tech rotation | ★ |
| Investing Simplified (Prof G) | The only 5 ETFs you'll ever need | ETF framework, no directional signal | ★ |
| IG France (Baradez) | MarketLive x3 (2026-05-22, 20, 18) | NEUTRAL — orderly daily coverage, no panic | ★★★ |
| IG France (Baradez) | Créer un Robot de Trading en moins d'1h | No regime signal (tutorial) | — |
| Finary | Bourse : les gagnants empochent toute la mise ? | Market concentration → QQQ > IWM | ★★ |
| Finary | La France touche le fond. C'est l'heure du rebond. | Europe risk-on; weak direct US signal | ★ |
| Finary | Combien gagnent nos députés ? | No regime signal (political) | — |
| Finary | Comment devenir riche en étant professeur | Wealth mgmt — no regime signal | ★ |
| Real Vision Presents | AI's Biggest Bottleneck Isn't Chips Anymore | Tech/AI sector shift; QQQ watch | ★ |
| Real Vision Presents | Sui LIVE Miami x6 (crypto/blockchain) | Risk-on institutional appetite for crypto | ★ |
| Oseille TV | Où vivre au Panama ? Le guide complet | Expat/wealth mgmt (UEMOA diaspora) | ★ |

**Cross-channel consensus:** 2 channels (Bravos Research + Prof G) signal upcoming regime transition toward HIGH_VOL within 1–6 months. IG France MarketLive continuity suggests current market remains orderly. Transcripts unavailable (cloud IP block); analysis inferred from titles + channel DNA.
