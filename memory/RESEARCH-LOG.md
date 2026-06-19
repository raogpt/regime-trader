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

## 2026-06-19 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | Stocks Are About to Do the UNTHINKABLE. | MID_VOL melt-up; dollar debasement driving nominal gains; real corp profits flat since 2021; GDP 2-4% = no recession | ★★★ HIGH — quantitative vol/macro framework |
| George Gammon | SpaceX, Iran, OpenAI IPO...My Controversial Stock Strategy | MID_VOL euphoria; Iran Hormuz MOU → oil $92→$78; SpaceX IPO $2-3T absorbing $85B; risk-on while SpaceX holds | ★★ MEDIUM — sentiment/narrative lens |
| IG France (Baradez) | MarketLive June 17 — Fed Day | MID→LOW vol transition; VIX ~16 on support oblique 15.6-15.7; new Fed chair Kevin Warch HOLD; 58% prob ≥1 cut Dec 2026 | ★★★ HIGH — technical levels + Fed catalyst |
| IG France (Baradez) | MarketLive June 12 | HIGH→MID transition; VIX 22→18; oil $82; SpaceX IPO rotating capital from QQQ (Nvidia, Alphabet) | ★★★ HIGH — daily market structure |
| IG France (Baradez) | Comment investir SpaceX | Neutral — platform tutorial; SpaceX tradeable; space sector rotation active | ★ LOW |
| Investing Simplified (Prof G) | These Space ETFs Could 10x by 2030! | Neutral/speculative; SpaceX IPO 94x revenue = overvalued; prefer XOVR ETF for space exposure | ★ LOW |
| Oseille TV | 20 ans à 0% d'impôts : le coup de génie d'Erdogan | WEALTH MGMT PRIORITY — Turkey Art.20D: 20yr exemption on foreign-source income; estate tax 1%; corp 100%/95% exemption; retro Jan 2026 | ★★★ WEALTH MGMT |
| Oseille TV | [6 other videos — no transcript] | Titles: AI jobs displacement, exit tax, crash warning, AI two castes, digital euro, leaving France | Context only |
| Finary | [3 videos — no transcript] | 1M€ portfolio allocation; 0→millionaire; Mike Tyson spending | Context only |
| Real Vision Presents | [2 videos — no transcript] | Binance co-CEO blockchain; copper deposit | Low relevance |

**Cross-channel consensus:** VIX declining (MID→LOW), equities melt-up (dollar debasement + narrative), oil lower (Hormuz MOU), Fed on hold. SPY > QQQ near-term (SpaceX capital rotation from QQQ components). Monitor VIX 15.6-15.7 support as LOW_VOL regime trigger.

**Full report:** reports/2026-06-19-youtube-intel.md
