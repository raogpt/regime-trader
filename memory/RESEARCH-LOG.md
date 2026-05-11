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

## 2026-05-11 — YouTube Intel

_15 new videos across 6 channels. Transcripts blocked (cloud IP). Title-based analysis._

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Passeport GRATUIT pour vos enfants (et pour vous ensuite) | None | Wealth/expat — UEMOA passport strategy ★ |
| Bravos Research | Brace Yourself. | HIGH_VOL / bearish warning | Macro caution ★★★ |
| Finary | Retraite à 45 ans... projet impossible ? | None | Wealth/FIRE planning ★ |
| Finary | Un système au bord du gouffre ? | HIGH_VOL / systemic risk | Risk-OFF framing ★★ |
| Finary | Finary Life est disponible en gestion libre | None | Product promo |
| Finary | Je quitte la chaîne Finary... ? | None | Channel update |
| Finary | Les États-Unis... en faillite technique ? | HIGH_VOL / US fiscal risk | Risk-OFF, sovereign stress ★★★ |
| Investing Simplified | 7 Money Rules 95% of Americans Break | None | Personal finance ★ |
| Investing Simplified | $300k to live off dividends FOREVER | Mild risk-OFF (defensive income) | Wealth/dividend strategy ★★ |
| IG France (Baradez) | MarketLive 2026-05-07 | Unknown (no transcript) | TA market update ★★ |
| IG France (Baradez) | CFD chez IG guide complet 2026 | None | Sponsored content |
| IG France (Baradez) | MarketLive 2026-05-06 | Unknown (no transcript) | TA market update ★★ |
| IG France (Baradez) | MarketLive 2026-05-04 | Unknown (no transcript) | TA market update ★★ |
| Real Vision | Sui Live Miami 2026 (Raoul Pal) | Mixed — crypto risk-ON vs macro caution | Macro/crypto lens ★★ |
| Real Vision | Top Picks in the Gold Miners | HIGH_VOL / defensive rotation | Gold bull = risk-OFF signal ★★★ |

**Cross-channel consensus**: 3+ channels (Bravos, Finary ×2, Real Vision) pointing toward HIGH_VOL / risk-OFF. No channel publishing risk-ON content.
**Wealth Mgmt highlights**: Passport strategy (Oseille TV), FIRE planning (Finary), dividend income threshold $300k (Prof G), US fiscal risk (Finary), gold miners (Real Vision).
**Full report**: reports/2026-05-11-youtube-intel.md
