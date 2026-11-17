"""Download completed hourly candles from the public Binance spot API."""

import pandas as pd
import requests


KLINE_URL = "https://api.binance.com/api/v3/klines"
KLINE_COLUMNS = [
    "open_time", "Open", "High", "Low", "Close", "Volume", "close_time",
    "quote_vol", "trades", "taker_base", "taker_quote", "ignore",
]


def download_hourly_candles(symbol, start, end=None):
    """Return hourly spot candles with UTC timestamps and exchange trade fields.

    The start is inclusive and the end is exclusive. Without an end, the
    download ends at the current UTC hour. Only completed candles are used.
    """
    start_time = pd.to_datetime(start, utc=True)
    closed_through = pd.Timestamp.now(tz="UTC").floor("h")
    end_time = closed_through if end is None else min(pd.to_datetime(end, utc=True), closed_through)
    if pd.isna(start_time) or pd.isna(end_time) or start_time >= end_time:
        raise ValueError("Choose a valid range that contains completed historical candles.")

    cursor_ms = int(start_time.timestamp() * 1000)
    end_ms = int(end_time.timestamp() * 1000)
    rows = []
    with requests.Session() as session:
        while cursor_ms < end_ms:
            response = session.get(
                KLINE_URL,
                params={"symbol": symbol, "interval": "1h", "startTime": cursor_ms,
                        "endTime": end_ms - 1, "limit": 1000},
                timeout=30,
            )
            response.raise_for_status()
            page = response.json()
            if not page:
                break
            rows.extend(row for row in page if row[6] < end_ms)
            cursor_ms = page[-1][0] + 3_600_000
            if len(page) < 1000:
                break
    if not rows:
        raise RuntimeError(f"Binance returned no completed hourly candles for {symbol}.")

    frame = pd.DataFrame(rows, columns=KLINE_COLUMNS)
    frame["open_time"] = pd.to_datetime(frame["open_time"], unit="ms", utc=True)
    frame = frame.set_index("open_time").sort_index()
    numeric_columns = ["Open", "High", "Low", "Close", "Volume", "quote_vol",
                       "trades", "taker_base", "taker_quote"]
    frame[numeric_columns] = frame[numeric_columns].astype(float)
    return frame.loc[~frame.index.duplicated(keep="last")]
