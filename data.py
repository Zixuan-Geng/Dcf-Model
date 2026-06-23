import yfinance as yf

def get_financials(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    cashflow = ticker.cashflow
    fcf = cashflow.loc['Free Cash Flow'].iloc[0]
    return fcf
    

def get_shares_outstanding(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    shares = ticker.info['sharesOutstanding']
    return shares


print(get_financials("AAPL"))
print(get_shares_outstanding("AAPL"))