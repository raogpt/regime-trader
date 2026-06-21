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

## 2026-06-21 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Le prochain krach sera pire que 2008 | HIGH_VOL / RISK-OFF — Buffett Indicator at 228% (vs 146% at Dotcom, 109% at 2008); crash thesis | ★★★ |
| Oseille TV | L'IA va supprimer 300 millions d'emplois | Macro structural risk, AI displacement | ★ |
| Oseille TV | Exit tax: l'impôt qui taxe des gains fictifs | Wealth-mgmt / expat tax planning | WEALTH |
| Oseille TV | 20 ans à 0% d'impôts: le coup de génie d'Erdogan | Wealth-mgmt / jurisdictional tax strategy | WEALTH |
| Oseille TV | Le système va dans le mur: prêt pour le crash? | HIGH_VOL bearish framing | ★★ |
| Oseille TV | L'IA crée deux castes: maîtres et esclaves | Macro structural (no direct trade signal) | ★ |
| Bravos Research | The Biggest Trap in Financial History Has Just Been Set | HIGH_VOL / RISK-OFF — USD down 10%, bonds down 15%, $50B MMF outflow; nominal stock gains = dollar illusion | ★★★ |
| Bravos Research | Brace Yourself. | HIGH_VOL warning (title, no transcript) | ★★ |
| Finary | À quoi ressemble l'investissement quand on a 5M€? | Wealth-mgmt / HNW allocation | WEALTH |
| Finary | À quoi ressemble l'investissement quand on a 1M€ à placer? | Wealth-mgmt / HNW allocation | WEALTH |
| Investing Simplified (Prof G) | Opportunity of a Life Time! (6 Stocks) | Mixed — individual stocks; notes "things at the top"; asks if crash coming | ★ |
| Investing Simplified (Prof G) | Best Fidelity Funds to Buy and Hold FOREVER | ETF / long-term allocation; buy-and-hold bias | ★ |
| George Gammon | You Won't Believe What Just Happened To Interest Rates (New Fed Changed Everything) | HIGH_VOL catalyst — Warsh replaces Powell, market flips to expecting RATE HIKE | ★★★ |
| George Gammon | SpaceX, Iran, OpenAI IPO... Controversial Stock Strategy 2026 | RISK-ON euphoria → contrarian HIGH_VOL warning; gold/crypto/stocks all surging | ★★★ |
| IG France (Baradez) | MarketLive 2026-06-18 (Fed Warsh analysis) | MID→HIGH VOL — new Fed Chair, rate hike expectations, VIX bounced at key technical level | ★★★ |
| IG France (Baradez) | MarketLive (×3 other sessions) | Daily technical analysis, no transcript | ★★ |
| IG France (Baradez) | 3 façons d'acheter SpaceX chez IG | Speculative / IPO euphoria indicator | ★ |
| Real Vision | Binance Co-CEO on Future of Blockchain | Crypto macro; limited ETF relevance | ★ |
