"""Download daily historical OHLCV from Yahoo Finance."""

import pandas as pd
import yfinance as yf


def download_ohlcv(symbol, start, end, *, auto_adjust=False, end_inclusive=True):
    """Return one symbol's daily prices, indexed by exchange date.

    The requested end date is inclusive by default. Enable ``auto_adjust``
    to use dividend-adjusted OHLC.
    """
    start_date = pd.Timestamp(start).normalize()
    end_date = pd.Timestamp(end).normalize()
    if end_inclusive:
        end_date += pd.Timedelta(days=1)
    if pd.isna(start_date) or pd.isna(end_date) or start_date >= end_date:
        raise ValueError("Choose a valid date range with at least one calendar day.")

    prices = yf.download(
        symbol,
        start=start_date.date().isoformat(),
        end=end_date.date().isoformat(),
        interval="1d",
        auto_adjust=auto_adjust,
        ignore_tz=True,
        multi_level_index=False,
        progress=False,
        threads=False,
        timeout=20,
    )
    columns = ["Open", "High", "Low", "Close", "Volume"]
    if prices is None or prices.empty or not set(columns).issubset(prices.columns):
        raise RuntimeError(f"Yahoo Finance returned no daily OHLCV for {symbol} in the requested range.")

    if "Adj Close" in prices:
        columns.append("Adj Close")
    prices = prices[columns].astype(float).dropna(subset=["Open", "High", "Low", "Close"])
    if prices.empty:
        raise RuntimeError(f"Yahoo Finance returned no complete daily prices for {symbol}.")
    return prices.sort_index()


def download_price_records(symbol, start, end):
    """Return dated records with lowercase OHLCV fields and optional adjClose."""
    prices = download_ohlcv(symbol, start, end)
    columns = {column: column.lower() for column in prices}
    columns["Adj Close"] = "adjClose"
    return prices.rename(columns=columns).rename_axis("date").reset_index().to_dict("records")
