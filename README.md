# Quant Trading Strategies

Python notebooks for researching mean reversion, momentum, market regimes, portfolio allocation, and machine learning. Equity and ETF history comes from Yahoo Finance through `yfinance`. Notebooks with additional inputs describe their data sources and configuration in the opening cell. [yfinance documentation](https://ranaroussi.github.io/yfinance/)

## Core strategies

| Notebook | Strategy |
| --- | --- |
| [Bollinger Bands and RSI](notebooks/bollinger-rsi.ipynb) | Combines Bollinger Bands with the Relative Strength Index to identify mean-reversion signals. |
| [Internal Bar Strength and Rate of Change](notebooks/ibs-roc.ipynb) | Tests two strategies that combine the close's position within the daily range with the rate of price change. |
| [Internal Bar Strength and Exponential Moving Averages](notebooks/ibs-ema.ipynb) | Filters AAPL's Internal Bar Strength signals using 8- and 24-day exponential moving averages. |
| [Time-Series Momentum](notebooks/tsmom.ipynb) | Trades in the direction of the asset's trend and sizes exposure using volatility. |
| [Gaussian Mixture Regimes](notebooks/gmm-regimes.ipynb) | Re-estimates a Gaussian mixture model in successive windows and simulates signals for each test window. |
| [Volatility Threshold Regimes](notebooks/volatility-threshold-regimes.ipynb) | Applies rolling thresholds to Yang–Zhang volatility and tests each rule using walk-forward validation. |
| [HMM and Semivariance Allocation](notebooks/hmm-semivariance-allocation.ipynb) | Estimates market regimes with a hidden Markov model and adjusts portfolio weights by regime. |
| [Regime-Adaptive XGBoost](notebooks/xgboost-regime-adaptive.ipynb) | Combines XGBoost with hidden Markov regimes and recalibrates entry and exit thresholds in each window. |

## Additional strategies

- [Adaptive Time-Series Momentum](notebooks/adaptive-time-series-momentum.ipynb)
- [Alphabet Volatility Regimes](notebooks/google-volatility-regimes.ipynb)
- [Alphabet Volatility Regimes with Extended Validation](notebooks/google-volatility-regimes-extended.ipynb)
- [Bayesian Change-Point Regimes](notebooks/bayesian-change-point-regimes.ipynb)
- [Bayesian Hierarchical Risk Parity](notebooks/bayesian-hierarchical-risk-parity.ipynb)
- [Bayesian Regime Allocation](notebooks/bayesian-regime-allocation.ipynb)
- [Beta Instability for the Nasdaq-100](notebooks/beta-instability-nasdaq100.ipynb)
- [Beta Instability Long–Short](notebooks/beta-instability-long-short.ipynb)
- [Consensus Mean Reversion and Momentum](notebooks/consensus-mean-reversion-momentum.ipynb)
- [Consensus Mean Reversion with Volatility Thresholds](notebooks/consensus-mean-reversion-volatility-thresholds.ipynb)
- [Consensus with Adaptive Thresholds](notebooks/consensus-adaptive-thresholds.ipynb)
- [DCC-GARCH Allocation with Trading Costs](notebooks/dcc-garch-walk-forward-allocation.ipynb)
- [DCC-GARCH Consensus](notebooks/dcc-garch-consensus.ipynb)
- [DCC-GARCH Minimum-Variance Allocation](notebooks/dcc-garch-minimum-variance.ipynb)
- [Dynamic-Scaled Momentum for S&P 500 Stocks](notebooks/dynamic-scaled-momentum-sp500.ipynb)
- [Dynamic-Scaled Momentum with a Stochastic Filter](notebooks/dynamic-scaled-momentum-stochastic.ipynb)
- [Enhanced Volatility-Regime Momentum](notebooks/enhanced-volatility-regime-momentum.ipynb)
- [Entropy and Volatility Spread Allocation](notebooks/entropy-volatility-spread.ipynb)
- [Entropy and Volatility Spread with MST-HRP](notebooks/entropy-volatility-spread-mst-hrp.ipynb)
- [Factor-Adaptive Mean Reversion](notebooks/factor-adaptive-mean-reversion.ipynb)
- [Factor-Adaptive Mean Reversion Extended](notebooks/factor-adaptive-mean-reversion-extended.ipynb)
- [Gaussian Mixture Regime Allocation](notebooks/gaussian-mixture-regime-allocation.ipynb)
- [Gaussian Mixture Regimes with Robustness Diagnostics](notebooks/gaussian-mixture-regime-robustness.ipynb)
- [GDP-Driven Equity Allocation](notebooks/gdp-dynamic-allocation.ipynb)
- [GMM with Risk-Adjusted Regime Signals](notebooks/gmm-risk-adjusted-regime-signals.ipynb)
- [GMM with Stochastic and Volatility Features](notebooks/gmm-stochastic-volatility-regimes.ipynb)
- [Hierarchical HMM allocation](notebooks/hierarchical-hmm-allocation.ipynb)
- [HMM allocation with long-short risk parity](notebooks/hmm-long-short-risk-parity.ipynb)
- [HMM and Ridge Long-Cash Regimes](notebooks/hmm-ridge-long-cash.ipynb)
- [HMM and Ridge Long-Short Regimes](notebooks/hmm-ridge-long-short.ipynb)
- [HMM and Yang–Zhang Regime Strategy](notebooks/hmm-yang-zhang-regime-strategy.ipynb)
- [HMM Consensus with Robustness Diagnostics](notebooks/hmm-consensus-robustness.ipynb)
- [HMM multi-optimizer allocation](notebooks/hmm-multi-optimizer-allocation.ipynb)
- [HMM with Rate of Change and Yang-Zhang Volatility](notebooks/hmm-roc-yang-zhang.ipynb)
- [Hourly BTC Direction with GJR-GARCH](notebooks/btc-hourly-gjr-garch.ipynb)
- [Hourly BTC Feature Selection](notebooks/btc-hourly-feature-selection.ipynb)
- [Hourly BTC Historical Kelly Sizing](notebooks/btc-hourly-kelly-sizing.ipynb)
- [Hourly BTC Market Microstructure](notebooks/btc-hourly-microstructure.ipynb)
- [Hourly BTC Realized GARCH Ensemble](notebooks/btc-hourly-realized-garch-ensemble.ipynb)
- [Hourly BTC Volatility and Jumps](notebooks/btc-hourly-volatility-jumps.ipynb)
- [IBS and Yang–Zhang Volatility Walk-Forward](notebooks/ibs-yang-zhang-walk-forward.ipynb)
- [IBS with Volatility Thresholds](notebooks/ibs-volatility-thresholds.ipynb)
- [Intraday Robust Median Reversion](notebooks/intraday-robust-median-reversion.ipynb)
- [Long QQQ Regime Allocation](notebooks/long-qqq-regime-allocation.ipynb)
- [Long-Cash Mean Reversion](notebooks/long-cash-mean-reversion.ipynb)
- [Long-Cash Volatility Thresholds](notebooks/long-cash-volatility-thresholds.ipynb)
- [Long-Short Volatility Thresholds](notebooks/long-short-volatility-thresholds.ipynb)
- [Machine Learning and MSTR Market Regimes](notebooks/machine-learning-mstr-market-regimes.ipynb)
- [Machine-Learning Feature Ensemble](notebooks/machine-learning-feature-ensemble.ipynb)
- [Minimum Spanning Tree Regimes](notebooks/minimum-spanning-tree-regimes.ipynb)
- [Minimum-Volatility and Maximum-Sharpe Portfolios](notebooks/minimum-volatility-portfolio.ipynb)
- [Momentum Crash Risk](notebooks/momentum-crash-risk.ipynb)
- [Momentum with Holdout Validation](notebooks/momentum-with-holdout-validation.ipynb)
- [Multi-Feature Volatility Regimes](notebooks/multi-feature-volatility-regimes.ipynb)
- [Multi-Level HMM Portfolio Allocation](notebooks/multi-level-hmm-portfolio-allocation.ipynb)
- [NVDA Relative Strength and Machine Learning](notebooks/nvda-relative-strength-machine-learning.ipynb)
- [Online Portfolio Momentum with HMM Regimes](notebooks/online-portfolio-momentum-hmm.ipynb)
- [Online Portfolio Selection](notebooks/online-portfolio-selection.ipynb)
- [Optimized Online Portfolio Selection](notebooks/online-portfolio-selection-optimized.ipynb)
- [Out-of-Sample Portfolio Allocation](notebooks/portfolio-allocation-out-of-sample.ipynb)
- [Particle filter regime allocation](notebooks/particle-filter-regime-allocation.ipynb)
- [QQQ Regime Backtest](notebooks/qqq-regime-backtest.ipynb)
- [RSI Mean Reversion](notebooks/rsi-mean-reversion.ipynb)
- [Rule-Based Market Regimes](notebooks/rule-based-market-regimes.ipynb)
- [Semivolatility-Scaled Momentum with a Fixed Universe](notebooks/semivolatility-scaled-momentum-current-universe.ipynb)
- [Semivolatility-Scaled Momentum with Historical Membership](notebooks/semivolatility-scaled-momentum-historical-universe.ipynb)
- [Spatio-Temporal Momentum](notebooks/spatio-temporal-momentum.ipynb)
- [Student-t HMM regime consensus](notebooks/student-t-hmm-regime-consensus.ipynb)
- [Student-t HMM volatility strategy](notebooks/student-t-hmm-volatility.ipynb)
- [TEMA trend strategy with HMM regimes](notebooks/tema-hmm-trend.ipynb)
- [TEMA with volatility-based position sizing](notebooks/tema-volatility-sizing.ipynb)
- [Triple exponential moving average crossover](notebooks/tema-crossover.ipynb)
- [VaR-Filtered Mean Reversion](notebooks/var-filtered-mean-reversion.ipynb)
- [VaR-Filtered Mean Reversion with Holdout Analysis](notebooks/var-filtered-mean-reversion-validation.ipynb)
- [Volatility-Adaptive Market Regimes](notebooks/volatility-adaptive-market-regimes.ipynb)
- [Walk-Forward Long-Cash Mean Reversion](notebooks/walk-forward-long-cash-mean-reversion.ipynb)
- [Walk-Forward Minimum Spanning Tree Regimes](notebooks/walk-forward-mst-regimes.ipynb)
- [Walk-Forward Momentum](notebooks/walk-forward-momentum.ipynb)
- [Walk-Forward MST-HRP Allocation](notebooks/mst-hrp-allocation.ipynb)
- [Walk-Forward Regime Momentum](notebooks/walk-forward-regime-momentum.ipynb)
- [Walk-Forward Time-Series Momentum](notebooks/walk-forward-time-series-momentum.ipynb)
- [Walk-Forward Volatility-Regime Allocation](notebooks/walk-forward-volatility-regime-allocation.ipynb)

## Run a notebook

From the repository root, create a virtual environment with Python 3.13.

```bash
python -m venv .venv
```

Activate it using the command for your shell.

- macOS and Linux use `source .venv/bin/activate`.
- Windows PowerShell uses `.\.venv\Scripts\Activate.ps1`.

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open a file in `notebooks/` and run its cells in order. Symbols and dates are set in each notebook. The volatility-threshold parameter search and the XGBoost multi-asset validation can take several minutes. Some notebooks write CSVs and figures to the current directory or a `results/` subdirectory. The assumptions about trading costs, execution, and price adjustments vary by strategy.
