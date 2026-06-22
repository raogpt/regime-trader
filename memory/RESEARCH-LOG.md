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

## 2026-06-22 — YouTube Intel

22 new videos across 7 channels (Jun 15–22). Transcripts unavailable (environment restriction); analysis from titles.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Bravos Research | "The Biggest Trap in Financial History Has Just Been Set." | HIGH_VOL / Risk-OFF ★★★ | Strong bearish warning — crash/trap framing |
| Bravos Research | "Brace Yourself." | HIGH_VOL / Risk-OFF ★★★ | Second consecutive bearish alert |
| Oseille TV | "Le prochain krach sera pire que 2008" | HIGH_VOL / Risk-OFF | Crash worse than 2008 predicted (FR) |
| George Gammon | "You Won't Believe What Just Happened To Interest Rates (New Fed Changed Everything)" | MID→HIGH_VOL catalyst | Fed/rate shock; regime inflection possible |
| George Gammon | "SpaceX, Iran, OpenAI IPO…Here's My Controversial Stock Strategy" | Geopolitical noise | Iran risk + IPO frenzy = elevated uncertainty |
| IG France (Baradez) | MarketLive ×5 (Jun 15–22) | Active technical monitoring | Daily market analysis sessions; no transcript |
| IG France (Baradez) | "3 façons d'acheter SpaceX chez IG" | Neutral | Retail speculative interest in privates |
| Investing Simplified (Prof G) | "Best Fidelity Funds to Buy and Hold FOREVER" | LOW_VOL / long-term bullish | ETF buy-and-hold recommendation |
| Investing Simplified (Prof G) | "🚨Opportunity of a Life Time! (These 6 Stocks Could PRINT…)" | Neutral/Bullish | Individual stocks — not actionable for ETF-only bot |
| Finary | "Médecin millionnaire sans héritage" | Wealth mgmt | Build wealth from zero — case study |
| Finary | "À quoi ressemble l'investissement quand on a 1M € à placer ?" | Wealth mgmt | HNW allocation playbook |
| Oseille TV | "Exit tax : l'impôt qui taxe des gains fictifs" | Wealth mgmt ★ PRIORITY | Exit tax mechanics for French expats |
| Oseille TV | "20 ans à 0% d'impôts : le coup de génie d'Erdogan" | Wealth mgmt ★ PRIORITY | Tax optimization / offshore structuring (UEMOA/Africa relevant) |
| Oseille TV | "L'IA va supprimer 300 millions d'emplois" | Macro — structural | AI disruption; long-term portfolio positioning |
| Real Vision Presents | "Binance Co-CEO on the Future of Blockchain" | Crypto — not actionable | Out of scope for regime bot |

**Cross-channel consensus:** 3 channels (Bravos ×2, Oseille TV ×1) carry explicit crash/trap/brace language → bearish/HIGH_VOL lean. George Gammon adds Fed catalyst uncertainty. Confidence: MODERATE (title-only, no transcripts).

**HMM implication:** If HMM detects MID_VOL or near HIGH_VOL threshold today, YouTube signal supports 60% allocation cap + wide stops. Do not add leverage.
