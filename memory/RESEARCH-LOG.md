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

## 2026-06-27 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Le prochain krach sera pire que 2008 | HIGH_VOL / RISK-OFF — Buffett indicator 228% (record high; 2000 peak was 146%) | HIGH |
| Oseille TV | Turquie : 20 ans sans impôt sur les revenus étrangers | N/A regime — Turkey 20yr foreign income tax exemption for 2026 residents | HIGH (wealth mgmt) |
| Oseille TV | S'expatrier à Dubaï en 2026 | N/A regime — Dubai still viable despite Middle East tensions | MED (wealth mgmt) |
| Finary | Bienvenue dans le siècle chinois | Geopolitical rebalancing; long-term SPY/QQQ headwind | MED |
| Finary | Médecin millionnaire sans héritage | Wealth building model (SEL + SCPI + ETF) | HIGH (wealth mgmt) |
| Investing Simplified | 🚨Opportunity of a Life Time! | MID-HIGH VOL sentiment — retail sees markets "at the top" | MED |
| Investing Simplified | SCHD STILL BEATS every dividend ETF | Defensive rotation; dividend ETFs gaining interest | MED |
| George Gammon | A $100 Trillion Currency Crisis Just Started | HIGH_VOL / RISK-OFF — DXY weakness, USD safe-haven status eroding | HIGH |
| IG France (Baradez) | Inflation américaine, vers une réaction de la Fed ? | HIGH_VOL / RATE HEADWIND — PCE expected 4.1% YoY (3yr high); Fed Chair Worsh hawkish, no pivot | HIGH |
| IG France (Baradez) | MarketLive 24 Jun | MID_VOL — Micron beat (tech bounce) but NASDAQ trend unconfirmed | MED |
| IG France (Baradez) | MarketLive 22 Jun | MID_VOL — Bond market stressed post-Fed; SP500 structure fragile | MED |
| Real Vision Presents | What Finance Looks Like in 5 Years? | Long-term structural (TradFi/DeFi convergence); LOW immediate signal | LOW |
| Bravos Research | (no new videos) | — | — |

**Cross-channel consensus (2026-06-27):** 3+ sources independently signal HIGH_VOL / bearish macro.
- Oseille TV + George Gammon: crash risk + USD crisis (strongest alignment)
- IG France Baradez: PCE 4.1% + hawkish Worsh = rates elevated, no cut
- **HMM watch:** If PCE Thursday exceeds 4.1% → HIGH_VOL regime likely; reduce to 60% allocation; prefer IWM over QQQ
