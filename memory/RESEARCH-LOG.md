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

## 2026-05-03 — YouTube Intel

> Note: Transcripts blocked (cloud IP). Analysis based on video titles + channel context.

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Ces 12 pays ne prélèvent AUCUN impôt (pour l'instant) | Neutral — tax/expat content | ★★★ Wealth Mgmt / UEMOA |
| Bravos Research | History is About to Be Made. | BULLISH — significant market event imminent | ★★★ High |
| Bravos Research | The Damage is done… | HIGH_VOL aftermath / base-building | ★★★ High |
| Finary | Ce marché est en train de tout faire basculer | HIGH_VOL / market disruption | ★★ Medium |
| Finary | Les gérants de fonds peuvent-ils encore faire la différence ? | Active vs passive — no direct regime signal | ★ Low |
| Finary | Comment déceler les objectifs financiers irréalistes ? | Personal finance — no regime signal | ★ Low |
| Finary | À 30 ans, ce salarié en marketing digital a fait le bon départ ! | Personal finance — no regime signal | ★ Low |
| Investing Simplified (Prof G) | EXTREME Market Update: S&P 500 All Time High! May 2026 | LOW_VOL / risk-on — SPY at ATH | ★★★ Critical |
| Investing Simplified (Prof G) | You Do NOT Need $1.46 Million to Retire | Retirement planning — no regime signal | ★ Low |
| Investing Simplified (Prof G) | The Best Tax Strategy: Donor Advised Fund | Tax optimization — no regime signal | ★★ Wealth Mgmt |
| IG France (Alexandre Baradez) | Le cockpit d'un expert — Marc Dagher ProRealTime walkthrough | Technical analysis — no direct signal (no transcript) | ★★ Medium |

**Cross-channel consensus:** Apr 27-29 damage → May 1-2 ATH recovery. Sequence suggests HIGH→MID/LOW vol transition. SPY ATH is primary signal.
