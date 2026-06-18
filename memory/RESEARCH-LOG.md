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

## 2026-06-18 — YouTube Intel

> Transcripts blocked (cloud IP ban) — title-based analysis only. Confidence reduced one notch.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research ★★★ | Brace Yourself. | HIGH_VOL warning | HIGH |
| Bravos Research ★★★ | The Biggest Stock Market Rug Pull in History is Here. | STRONGLY BEARISH / HIGH_VOL spike | HIGH |
| Oseille TV | Le système va dans le mur : prêt pour le crash ? | BEARISH / crash warning | MEDIUM |
| George Gammon ★★★ | SpaceX, Iran, OpenAI IPO...Here's My Controversial Stock Strategy For 2026 | Geopolitical risk (Iran) → MID/HIGH_VOL | MEDIUM |
| IG France (Baradez) ★★★ | MarketLive x5 (Jun 11–18) | Daily TA — opaque without transcript | PENDING MANUAL REVIEW |
| Real Vision Presents | Discovering a Huge Copper Deposit | Materials/copper → IWM preference | LOW |
| Oseille TV | 20 ans à 0% d'impôts : Erdogan + Exit tax + Quitter la France | Wealth mgmt / expat / tax | WEALTH-MGMT |
| Finary | À quoi ressemble l'investissement quand on a 1M€ ? | HNW allocation | WEALTH-MGMT |

**Cross-channel consensus:** 3/7 channels (Bravos ★★★, George Gammon ★★★, Oseille TV) skew BEARISH. No risk-on signal found. Regime implication: **MID_VOL → HIGH_VOL bias**. Sizing: 60%, no leverage, wide stops until HMM confirms.

**Wealth Mgmt highlights:** Exit tax (FR), digital euro CBDC risk, Turkey 0% tax strategy, HNW ETF allocation at 1M€.

Full report: `reports/2026-06-18-youtube-intel.md`
