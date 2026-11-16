# Quant Trading Strategies

Eight Python notebooks for researching mean reversion, momentum, market regimes, and machine learning. Each notebook downloads real daily market data from Yahoo Finance through `yfinance`. No API key is required. [yfinance documentation](https://ranaroussi.github.io/yfinance/)

## Strategies

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
