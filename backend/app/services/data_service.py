import yfinance as yf

def get_price_data(ticker, start, end):
    ticker = ticker + ".JK"  # IDX format
    df = yf.download(ticker, start=start, end=end)
    df.reset_index(inplace=True)
    return df
