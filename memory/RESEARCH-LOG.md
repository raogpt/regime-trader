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

## 2026-05-28 — YouTube Intel

| Channel | Video | Regime Signal | Relevance |
|---------|-------|---------------|-----------|
| Oseille TV | Votre argent en banque n'est plus à vous ! | RISK-OFF — banking system trust eroding | ★★ wealth-mgmt / bail-in awareness |
| Bravos Research | The Entire Financial System Just Changed Forever… | HIGH_VOL RISK-OFF — systemic macro shift narrative | ★★★ direct regime signal |
| Finary | Bourse : les gagnants empochent toute la mise ? | MID — market concentration (Mag7 analogy) | ★★ equity structure |
| Finary | Le piège du « Achetez maintenant, payez plus tard » | NEUTRAL — consumer credit risk | ★ wealth-mgmt |
| Finary | J'ai retracé le patrimoine de Donald Trump | NEUTRAL — political/entertainment | ★ no signal |
| Finary | La richesse réelle de la famille royale britannique | NEUTRAL — asset allocation context | ★ no signal |
| Investing Simplified (Prof G) | 🚨 Investors Could Get Blindsided.. CRUCIAL Market Update 2026 | HIGH_VOL WARNING — caution signal | ★★★ direct regime |
| Investing Simplified (Prof G) | America's #1 Retirement Risk | MID_VOL — sequence-of-returns / inflation | ★★ macro tail risk |
| Investing Simplified (Prof G) | 5 Best Stocks & Hottest Investing Sectors for 2026? | RISK-ON lean — sector rotation optimism | ★★ sector rotation |
| IG France (Baradez) | MarketLive 2026-05-28 (today) | LIVE TA — current trend analysis FR/EU mkts | ★★★ real-time signal |
| IG France (Baradez) | MarketLive 2026-05-27 | TA signals prior session | ★★★ |
| IG France (Baradez) | MarketLive 2026-05-22 | TA signals mid-week | ★★★ |
| IG France (Baradez) | Comment maîtriser le RSI en trading | EDUCATIONAL — no direct signal | ★ |
| IG France (Baradez) | Créer un Robot de Trading sans coder | EDUCATIONAL — no direct signal | ★ |
| Real Vision | AI Isn't Worried About Chips Anymore! | RISK-ON — AI/tech positive → QQQ tailwind | ★★★ |
| Real Vision | AI Eats Software: Agentic Finance / Machine GDP | RISK-ON — AI productivity → QQQ positive | ★★★ |
| Real Vision | RWAs: Every Asset Will Be Onchain — $100T Migration | RISK-ON structural — institutional crypto/RWA | ★★ macro |
| Real Vision | From Lagos to the World: African Payments (Tayo Oviosu) | AFRICA PRIORITY — UEMOA fintech context | ★★★ wealth-mgmt |
| Real Vision | Sui Overflow Hackathon / DeFi suite (×4 videos) | NEUTRAL — crypto ecosystem, no ETF signal | ★ no regime signal |
| Real Vision | One Wallet Cost Me Everything! | NEUTRAL — crypto cautionary tale | ★ no signal |

**Note:** Transcripts unavailable (YouTube IP block on cloud runner). Analysis based on titles + channel context.

**Cross-channel vol consensus:** Mixed — 2 clear risk-off/warning signals (Bravos, Prof G) vs. 2 AI-driven risk-on signals (Real Vision). Net bias: **MID_VOL caution**. No 2-channel consensus on directional move.

**Wealth Mgmt priority:** Oseille banking risk + Real Vision African Payments = watch for UEMOA capital controls / bail-in risk narrative.
