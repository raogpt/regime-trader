# Weekly Review — regime_trader

Friday reviews appended here.

## Week ending YYYY-MM-DD

### Stats
| Metric | regime_trader | trading-bot |
|--------|--------------|-------------|
| Starting portfolio | $X | $X |
| Ending portfolio | $X | $X |
| Week return | +-X% | +-X% |
| S&P 500 week | +-X% | +-X% |
| Alpha vs S&P | +-X% | +-X% |
| Trades | N | N |
| Win rate | X% | X% |
| Sharpe (est.) | X.XX | X.XX |
| Dominant regime | X | — |

### Regime Distribution This Week
| Regime | Bars | % of time |
|--------|------|-----------|

### Closed Trades
| ETF | Entry | Exit | P&L | Regime |

### What Worked
- ...

### What Didn't Work
- ...

### Model Adjustments
- ...

### Overall Grade: X

## 2026-05-16 — Weekly Review

### HMM Retrain Summary
- Training bars: 343 (IEX feed, ~1.4yr window)
- n_states selected: 5 (BIC-optimal; tested 3–7)
- Current regime: **BEAR** (confidence 99.9%) — regime shifted Friday
- Week dominant regime: **EUPHORIA** (Mon–Thu bullish run)

### Regime Distribution (full 343-bar window)
| Regime   | Bars | % of window |
|----------|------|-------------|
| bear     | 119  | 34.7%       |
| bull     | 94   | 27.4%       |
| neutral  | 58   | 16.9%       |
| euphoria | 40   | 11.7%       |
| crash    | 32   | 9.3%        |

### Portfolio
| Metric | Value |
|--------|-------|
| Starting equity | $100,000.00 |
| Current equity  | $106,635.15 |
| Total return (inception) | +6.64% |
| Week regime shift | EUPHORIA → BEAR (Friday) |
| Dominant regime this week | EUPHORIA |

### Week Regime Narrative
- Mon–Thu: EUPHORIA regime — market rallying strongly, positions likely benefitted
- Friday close: HMM flipped to BEAR at 99.9% confidence — sharp intraday reversal signal
- This regime flip is a critical signal: exposure should be cut going into next week

### What the HMM Got Right
- 5-state model (vs simpler 3-state) captured the EUPHORIA vs BULL distinction — important for sizing
- BEAR detection at 99.9% confidence on Friday is unambiguous; no marginal call
- Week-dominant EUPHORIA correctly identified the Mon–Thu rally

### What the HMM Got Wrong / Risks
- **Data gap**: TRADE-LOG.md shows no recorded trades since bot launch (Apr 27); equity gain of $6,635 is unaccounted — either positions ran without trade-log entries, or paper account had a different starting state. Must audit.
- **IEX vs SIP feed**: switched from SIP to IEX data feed this session (free tier). IEX is less liquid for some prints; may affect bar quality slightly — monitor for anomalies.
- **Convergence warnings**: multiple states showed non-convergence during BIC sweep (especially n=6,7). n=5 converged cleanly. Not a problem this week but worth watching.
- **Regime flip on final bar**: if BEAR is a single-bar call, it may not meet the 3-bar stability rule required to act. Verify before opening short/defensive next week.

### Model Adjustments for Next Week
- **Stability check before acting on BEAR**: confirm 3 consecutive BEAR bars before reducing exposure. Current signal is 1 bar.
- **Confidence threshold**: 55% minimum is fine; this week's signals were high-confidence (99.9% BEAR). No change needed.
- **Circuit breakers**: no reason to reconsider. BEAR at 99.9% is exactly what circuit breakers are designed to route through, not around.
- **Trade log audit**: run pre-market Monday to reconcile $6,635 gain vs empty trade log.
- **IEX feed**: keep as default (SIP subscription not available on paper tier). IEX data quality is sufficient for daily HMM training.

### Overall Grade: B
- HMM model clean, BIC selection working, data pipeline fixed (IEX feed)
- Strong equity gain (+6.64%) but unaudited source
- Regime flip to BEAR is the dominant signal heading into next week — must confirm stability
