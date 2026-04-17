from fastapi import APIRouter, Query
from app.services.data_service import get_price_data
from app.services.feature_engineering import compute_features
from app.services.signal_engine import generate_signal

router = APIRouter()

@router.get("/analysis")
def analyze(
    ticker: str = Query(...),
    start: str = Query(...),
    end: str = Query(...)
):
    df = get_price_data(ticker, start, end)
    features = compute_features(df)
    signal = generate_signal(features)

    return {
        "ticker": ticker,
        "signal": signal,
        "latest_price": df.iloc[-1]["Close"]
    }
