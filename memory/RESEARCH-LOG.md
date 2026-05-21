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

## 2026-05-21 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | In 6 Months, It's All Over. | HIGH_VOL warning / macro deterioration 6m horizon | ★★★ HIGH |
| Bravos Research | Your Last Chance at Generational Wealth. | MID→HIGH_VOL; generational buying opportunity or last-rally framing | ★★★ MEDIUM |
| Investing Simplified | BREAKING: Expect the Great Market Flip (VERY SOON) | Regime inflection imminent — bull or bear flip unclear without transcript | ★★ MEDIUM |
| Investing Simplified | Add this ONE Sector to 3 Fund Portfolio | Sector rotation hint; allocation signal for ETF sizing | ★ LOW |
| IG France (Baradez) | MarketLive 2026-05-20 | Technical regime read on EU/global markets; MID_VOL likely | ★★★ HIGH |
| IG France (Baradez) | MarketLive 2026-05-18 | Technical confirmation; watch for SPY/QQQ breakout/breakdown levels | ★★★ HIGH |
| Finary | La France touche le fond. C'est l'heure du rebond. | Bullish EU narrative; risk-on sentiment in FR media | ★ LOW |
| Finary | Comment devenir riche en étant professeur | Wealth mgmt / patrimoine building | ★ WEALTH-MGMT |
| Oseille TV | Où vivre au Panama ? Le guide complet | Expat/relocation; UEMOA wealth mgmt relevance | ★ WEALTH-MGMT |
| Real Vision | Adventures in US Capital Markets (Sui Live Miami) | Crypto/institutional; peripheral macro | — |

**Cross-channel consensus (2+ agree):** Bravos Research + Investing Simplified both signal near-term macro inflection → elevated uncertainty → MID_VOL bias with HIGH_VOL watch. No transcript confirmation available (cloud environment blocked).
