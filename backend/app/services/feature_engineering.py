import pandas as pd

def compute_features(df: pd.DataFrame):
    df["return"] = df["Close"].pct_change()

    df["ma5"] = df["Close"].rolling(5).mean()
    df["ma20"] = df["Close"].rolling(20).mean()

    df["volume_ratio"] = df["Volume"] / df["Volume"].rolling(20).mean()

    latest = df.iloc[-1]

    return {
        "price": latest["Close"],
        "ma5": latest["ma5"],
        "ma20": latest["ma20"],
        "volume_ratio": latest["volume_ratio"]
    }