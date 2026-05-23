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

## Week ending 2026-05-23 — INAUGURAL WEEKLY REVIEW

### Stats
| Metric | regime_trader | trading-bot |
|--------|--------------|-------------|
| Starting portfolio (Apr 27) | $100,000 | N/A |
| Ending portfolio | $110,914.84 | N/A |
| Week return (est. May 15–22) | ~+3.31% | N/A (cloud) |
| S&P 500 week | +0.89% | — |
| Alpha vs S&P (week) | ~+2.42% | — |
| ITD return (Apr 27 → May 23) | +10.91% | — |
| S&P 500 ITD | +4.27% | — |
| Alpha vs S&P (ITD) | +6.64% | — |
| Open positions | 3 | — |
| Win rate | 3/3 open (100%) | — |
| Dominant regime (week) | WEAK_BULL | — |
| HMM n_states selected | 6 | — |

### HMM Retrain Summary
- Training bars: 343 (504 daily bars fetched, ~343 clean after feature NaN drop)
- n_states selected: **6** (BIC=5114.24 — best fit)
- BIC by state count: 3→5785, 4→5501, 5→5380, **6→5114** ✓, 7→5500
- Current regime: **WEAK_BULL** (confidence 100.0%)
- Week dominant regime: **WEAK_BULL**

### Regime Distribution (full 504-bar training window)
| Regime | Bars | % of time |
|--------|------|-----------|
| weak_bull | 126 | 36.7% |
| weak_bear | 104 | 30.3% |
| strong_bear | 51 | 14.9% |
| strong_bull | 36 | 10.5% |
| euphoria | 14 | 4.1% |
| crash | 12 | 3.5% |

### Open Positions (EOW)
| ETF | Qty | Avg Entry | Current | Mkt Value | Unreal. P&L | P&L% |
|-----|-----|-----------|---------|-----------|-------------|------|
| IWM | 287 | $275.30 | $285.12 | $81,829 | +$2,817 | +3.57% |
| QQQ | 88 | $691.47 | $717.54 | $63,144 | +$2,294 | +3.77% |
| SPY | 100 | $729.51 | $745.64 | $74,564 | +$1,613 | +2.21% |
| **Total** | | | | **$219,537** | **+$6,724** | **+3.1% avg** |

**Note:** Account using ~2x margin leverage (equity $110,914 vs $219,537 exposure).

### Week P&L Estimate (positions held all week, no closes)
| ETF | Week move | Contrib |
|-----|-----------|---------|
| IWM 287sh | +2.68% (+$7.45/sh) | +$2,138 |
| QQQ 88sh | +1.21% (+$8.58/sh) | +$755 |
| SPY 100sh | +0.89% (+$6.57/sh) | +$657 |
| **Total** | | **+$3,550** |
_Week return est. = $3,550 / ~$107,360 starting equity ≈ **+3.31%**_

### What Worked
- **WEAK_BULL regime correctly identified** — all 3 ETFs long, all profitable
- **IWM overweight** paid off; small-caps outperformed (+2.68% vs SPY +0.89%)
- **2x leverage** in constructive regime amplified gains vs benchmark
- **6-state HMM** provided better granularity than lower state counts (BIC confirmed)
- **Confidence threshold 55%** working well — no false positives observed

### What Didn't Work
- **No trade log granularity** — TRADE-LOG.md only has baseline entry; daily EOD snapshots were not running. Cannot reconstruct entry dates or verify exact week equity.
- **SIP data subscription error** on first run — had to switch to IEX feed (paper account limitation). Fixed in episodic_runner.py.
- **`compute_features` method name bug** — was calling wrong method; fixed to `build_feature_matrix`. Both call sites patched.
- **2x leverage risk** — cash = -$108k is aggressive. One crash regime shift could cause >10% drawdown in a session.

### Model Adjustments / Lessons Learned
- **Confidence threshold:** Keep at 55%. Model is showing 100% confidence in WEAK_BULL; no reason to lower.
- **6-state model is optimal** per BIC — keep `n_states_range` at [3,7].
- **Leverage concern:** With $219k exposure on $110k equity, circuit breakers must be respected absolutely. If `crash` or `strong_bear` detected, position reduction should be immediate.
- **IEX feed fix:** Patch is in place. All future Alpaca data calls use `feed=DataFeed.IEX`.
- **Add EOD logging:** The lack of daily equity snapshots made week return estimation approximate. EOD cron should be running.
- **Crash/euphoria states** are each <5% of bars — model has limited training examples. Watch for misclassification at turning points.
- **Next week:** Monitor for WEAK_BULL→STRONG_BULL transition (regime flip risk if macro data surprises).

### Overall Grade: **B+**
_Strong ITD alpha (+6.64%). Week outperformance solid (+2.42% over S&P). Grade capped at B+ due to 2x leverage risk, missing EOD log infrastructure, and two code bugs found during first run._
