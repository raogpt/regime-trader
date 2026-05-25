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

## 2026-05-25 — YouTube Intel

**22 new videos | 7 channels | 9 transcripts retrieved**

| Channel | Video | Regime Signal | Relevance |
|---------|-------|--------------|----------|
| Bravos Research | The Entire Financial System Just Changed Forever… | 🔴 HIGH VOL — 30-yr yield breakout, 2007 analog, bond market "breaking" | ★★★ Critical |
| IG France (Baradez) | MarketLive May 20 — tendances graphiques | 🔴 HIGH VOL — 30-yr US at 5.2%+ (subprime-era highs), real yields rising, equity/bond rotation risk building | ★★★ Critical |
| Investing Simplified | Investors Could Get Blindsided (May 23) | 🔴 HIGH VOL — bond crisis warning, Iran war + Strait of Hormuz closed, ATH equities = complacency | ★★★ Critical |
| Finary | Bourse : les gagnants empochent toute la mise | 🟡 NEUTRAL — market concentration (top-10 stocks = ⅓ of all wealth), SPY/QQQ risk | ★★ Context |
| Finary | Les mystérieux trades du président | 🟡 MID→HIGH — Trump trade policy uncertainty (no transcript) | ★ Signal |
| Finary | La France touche le fond | 🟡 WEALTH MGMT — French fiscal bottom, European contrarian signal | ★ WM |
| Oseille TV | Où vivre au Panama ? | ⚪ WEALTH MGMT — expat/domicile planning, Panama analysis | ★ WM |
| Real Vision | From Lagos to the World (Paga/Oviosu) | 🌍 WEALTH MGMT PRIORITY — Africa fintech, 57% unbanked, crypto-friendly 12 African nations | ★★★ WM |
| Real Vision | AI's Biggest Bottleneck Isn't Chips | 🟡 NEUTRAL — power infrastructure bottleneck (Bloom Energy, GE Vernova) | ★ Signal |
| Real Vision | Sui Miami conference (x5 videos) | ⚪ Crypto/DeFi/Web3 — irrelevant to HMM ETF regime | ✗ |
| Investing Simplified | Quantum stocks / ETF basics | ⚪ Stock picks / educational — outside universe | ✗ |
| IG France | Trading bot tutorial | ⚪ Technical tools — no market signal | ✗ |

**Cross-channel consensus (3 channels):** 30-yr US Treasury yield at 5.2%+ = bond market stress. Equity/bond rotation risk real. Geopolitical: Iran war + Strait of Hormuz closed.

**Net regime signal: LEAN HIGH VOL**
- SPY: Neutral-negative (rate competition)
- QQQ: Short-term quantum/AI tailwind, rate-vulnerable
- IWM: Most rate-sensitive → most defensive posture

**Full report:** reports/2026-05-25-youtube-intel.md
