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

## 2026-05-04 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Ces 12 pays ne prélèvent AUCUN impôt (pour l'instant) | NEUTRAL — expat tax planning | WEALTH-MGMT HIGH |
| Bravos Research | History is About to Be Made. | BULLISH — pivotal macro moment, ATH narrative | MACRO HIGH |
| Bravos Research | The Damage is done… | RISK-OFF resolved — prior event damage priced in | MACRO MEDIUM |
| Finary | Comment déceler les objectifs financiers irréalistes ? | NEUTRAL — financial planning psychology | WEALTH-MGMT LOW |
| Finary | Les gérants de fonds peuvent-ils encore faire la différence ? | NEUTRAL — active vs passive; ETF preference reinforced | MACRO LOW |
| Finary | Ce marché est en train de tout faire basculer | BULLISH REVERSAL — market phase-shift narrative | REGIME MEDIUM |
| Investing Simplified (Prof G) | 🚨 EXTREME Market Update: S&P 500 All Time High! May 2026 | LOW_VOL / RISK-ON — ATH confirms bull regime | REGIME HIGH |
| Investing Simplified (Prof G) | You Do NOT Need $1.46 Million to Retire | NEUTRAL — retirement planning | WEALTH-MGMT MEDIUM |
| Investing Simplified (Prof G) | The Best Tax Strategy: Donor Advised Fund | NEUTRAL — tax-efficient giving | WEALTH-MGMT HIGH |
| IG France (Baradez) | MarketLive: Analyse graphique des marchés (2026-05-04) | UNDETERMINED — live TA session, no transcript | REGIME HIGH |
| IG France (Baradez) | Le cockpit d'un expert — Marc Dagher ProRealTime | UNDETERMINED — pro charting session | MACRO MEDIUM |

**Cross-channel consensus (2+ sources):** S&P 500 at ALL TIME HIGH (Bravos Research + Prof G). Regime bias = LOW_VOL → MID_VOL, RISK-ON. No vol-spike warnings. SPY large-cap momentum dominant.
**Wealth Mgmt flags:** Oseille TV (0-tax countries for expats) + Prof G (DAF strategy) = actionable.
*Transcripts unavailable — YouTube IP-blocked in cloud env. Analysis from titles + channel metadata.*
