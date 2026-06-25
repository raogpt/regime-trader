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

## 2026-06-25 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Le prochain krach sera pire que 2008 | BEARISH — Buffett Indicator 228%, highest in 100 yrs; previous crises peaked at 109–146% | HIGH |
| Bravos Research | The Biggest Trap in Financial History Has Just Been Set | MIXED — Nominal melt-up likely (dollar debasement + positive GDP), but real profits flat since 2021; inflation re-accelerating 2.4→4.2% | HIGH |
| Finary | Bienvenue dans le siècle chinois | NEUTRAL — China tech/AI/EV dominance thesis; no direct SPY/QQQ/IWM signal | LOW |
| Finary | Médecin millionnaire sans héritage | NEUTRAL — Wealth mgmt case study; PER/PEA/AV tax optimization | WEALTH |
| Investing Simplified | 7 Best ETFs for ROTH IRA 2026 | NEUTRAL — Buffett Indicator ~230%; VOO core + SPMO momentum tilt favored | MEDIUM |
| Investing Simplified | SCHD Still Beats Every Dividend ETF | NEUTRAL — Dividend quality focus; low vol positioning | MEDIUM |
| George Gammon | A $100 Trillion Currency Crisis Just Started | BEARISH/HIGH-VOL — Dollar reset triggered; DXY 99→101; oil $120 spike; JPY at 160; rate hike expectations replacing cuts | HIGH |
| George Gammon | What Just Happened to Interest Rates (New Fed) | HAWKISH/HIGH-VOL RISK — Kevin Warsh replaces Powell; 2yr yield +14bps in 5 min post-presser; no forward guidance; hike now priced in | HIGH |
| IG France (Baradez) | MarketLive 2026-06-24 | MID_VOL — VIX 19.2, brief spike >20; KOSPI -9% after +300% run; tech selling; Micron earnings; yield curve flattening | HIGH |
| IG France (Baradez) | MarketLive 2026-06-22 | MID_VOL — VIX ~17.6 at oblique support; BCE 62% chance of Sep hike; ECB rates not retreating post-Iran de-escalation | HIGH |
| IG France (Baradez) | MarketLive 2026-06-19 | MID_VOL transitioning — VIX 16→18→16; yield curve flattening 2yr/10yr; oil -35% from peak; rates sticky above pre-war levels | HIGH |
| IG France (Baradez) | MarketLive 2026-06-18 | HAWKISH PIVOT — Warsh presser; no forward guidance; 2% inflation mandate reaffirmed; market pricing rate HIKE this year | HIGH |
| Real Vision | Finance in 5 Years / Binance CEO | NEUTRAL — Crypto/TradFi convergence; no SPY/QQQ/IWM signal | LOW |

**Cross-channel consensus (2026-06-25):**
- Vol regime: MID_VOL; VIX 16-20 range, watching 16 support — break lower = LOW_VOL rally; break higher = HIGH_VOL
- Rate trajectory: Hawkish inflection. Warsh committed to 2%. Rate HIKE risk real in 2026 H2
- Macro risk: Buffett Indicator 228-230% (extreme). Dollar debasement masking real profit stagnation
- ETF rotation: SPY > QQQ (tech concentration, recent selloff). IWM headwind from rates. Momentum (SPMO) outperforming
- Catalyst watch: PCE inflation data due 2026-06-26; BCE Sep decision; Micron earnings
