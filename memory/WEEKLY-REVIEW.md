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

## 2026-06-06 — Weekly Review

### HMM Retrain Summary
- Training bars: 343
- n_states selected: 7
- Current regime: NEUTRAL (confidence 100.0%)
- Week dominant regime: NEUTRAL

### Regime Distribution (full window)
- crash: 19 bars (5.5%)
- euphoria: 7 bars (2.0%)
- neutral: 133 bars (38.8%)
- strong_bear: 30 bars (8.7%)
- strong_bull: 34 bars (9.9%)
- weak_bear: 97 bars (28.3%)
- weak_bull: 23 bars (6.7%)

### Portfolio
- Equity: $108,011.71
- Return since inception (Apr 27): +8.01%
- SPY benchmark (Mon-Thu, IEX): -2.77% this week / -2.28% since Apr 27

### Week Performance vs Benchmark
- regime_trader outperforming SPY by ~10.3% since inception
- This week SPY sold off hard (down ~2.77%); regime staying NEUTRAL protected capital

### What the HMM Got Right
- NEUTRAL regime held through SPY weakness this week — avoided chasing declining momentum
- 7-state model selected by BIC; weak_bear (28.3%) and neutral (38.8%) dominate, accurately reflecting choppy/risk-off environment
- No false euphoria signal despite prior +8% gain — model well-calibrated

### What the HMM Got Wrong / Watch
- 100% confidence on NEUTRAL reads as suspicious — HMM viterbi can over-commit when recent bars are unambiguous, but single-regime certainty deserves scrutiny
- convergence warnings during retrain on 4 of 7 state-count candidates; worth monitoring if BIC selection degrades
- weak_bear at 28% of historical window with strong_bear at 8.7% — if these merge next week, check for state collapse

### Should Confidence Threshold Change?
- 55% minimum threshold is appropriate; NEUTRAL at 100% confidence = low-risk hold, not an issue
- If next regime flip arrives at <70%, consider requiring 3-bar stability check before acting (already in rules)
- No change recommended this week

### Should Circuit Breaker Levels Change?
- Market down ~2.77% this week with no circuit trigger — levels appropriately set
- No adjustment needed

### Model Improvements for Next Week
- Add weekly equity snapshot to TRADE-LOG at end of each Friday so week-over-week return can be computed precisely
- Monitor if 7-state count holds after next retrain or oscillates — instability = reduce n_states_max
- Consider logging the Viterbi path confidence distribution (not just latest bar) for richer diagnostics

### Overall Grade: B+
- Strong capital preservation vs benchmark during risk-off week
- Data infrastructure issues (SIP feed → IEX fallback) resolved; IEX adequate for daily bars
- No trades executed; NEUTRAL regime + no clear ETF entry signal = correct hold behavior
