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

## 2026-06-20 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | The Biggest Trap in Financial History Has Just Been Set. (2026-06-18) | MID_VOL — nominal S&P rally driven by dollar debasement; real corporate profits flat since 2021; inflation 4.2% and re-accelerating | ★★★ |
| IG France (Baradez) | MarketLive 18 juin — Kevin Warsh premier FOMC (2026-06-18) | MID→HIGH_VOL risk — new Fed chair hawkish; market now pricing rate HIKE in 2026; VIX spiked at technical oblique; "market didn't digest well" | ★★★ |
| IG France (Baradez) | MarketLive 15 juin — US-Iran deal, VIX 16.6 (2026-06-15) | LOW→MID_VOL border — oil falling on Iran deal; VIX 16.6 approaching key oblique support (~15); European equities at record highs | ★★★ |
| George Gammon | You Won't Believe What Just Happened To Interest Rates (New Fed) (2026-06-20) | No transcript — title signals hawkish Fed rate surprise; likely corroborates Baradez view | ★★ |
| George Gammon | SpaceX, Iran, OpenAI IPO...Controversial Stock Strategy (2026-06-18) | No transcript — geopolitical/IPO event risk for market structure | ★★ |
| Oseille TV | 20 ans à 0% d'impôts : le coup de génie d'Erdogan (2026-06-17) | No regime signal — Turkey Article 20D: 20yr exemption on foreign-source income for new residents | ★★★ WEALTH |
| Oseille TV | Exit tax : l'impôt qui taxe des gains fictifs (2026-06-16) | No regime signal — France exit tax taxes unrealized gains on departure | ★★ WEALTH |
| Oseille TV | Le système va dans le mur : prêt pour le crash ? (2026-06-15) | No transcript — title bearish; aligned with Bravos "illusion" thesis | ★★ |
| Finary | À quoi ressemble l'investissement quand on a 1M € à placer ? (2026-06-17) | No regime signal — 1M€ wealth structuring: assurance-vie + bonds + SCPI + ETF + private equity | ★★ WEALTH |
| Investing Simplified (Prof G) | Best Fidelity Funds to Buy and Hold FOREVER (2026-06-16) | No regime signal — passive index fund guide; FXAIX/FSKAX as core | ★ |
| Oseille TV | Ces métiers bizarres qui payent 200 000€/an (2026-06-19) | No regime signal — income diversification/expat perspective | ★ |
| IG France (Baradez) | 3 façons d'acheter SpaceX chez IG (2026-06-18) | No transcript — SpaceX pre-IPO positioning | ★ |
| Real Vision | Binance Co-CEO — Future of Blockchain (2026-06-19) | No transcript — crypto/macro context | ★ |
| Real Vision | Discovering a Huge Copper Deposit (2026-06-13) | No transcript — commodities; copper as risk-on proxy | ★ |

**Cross-channel consensus:** 2 of 3 macro channels (Bravos + Baradez) agree: MID_VOL regime. The key variable is whether VIX breaks below ~15 (LOW_VOL) or Fed rate hike expectations push it back above 20 (HIGH_VOL). Current balance: MID_VOL with a LOW_VOL lean if Iran deal holds. Prefer SPY/QQQ over IWM if rate hike risk firms.
