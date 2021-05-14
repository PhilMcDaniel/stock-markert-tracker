import yfinance as yf
import pandas as pd

ticker_list = ['^DJI','^GSPC','^IXIC','AAPL','AMZN','GOOG','MSFT','VOO','VTI','QQQM','QQQ','VXUS','NVDA','AMD','PLTR','INTC','DIS','CVX','TSLA','SQ','BA','GE','IBM','NKE','SBUX','FB','NFLX']

#initialize combined data frame to solve Power BI error
combined_data = pd.DataFrame()
#loop through list of tickers to create and enhance historical data dataframe
for ticker in ticker_list:
    #print(ticker)
    stock = yf.Ticker(ticker)
    #dji.info
    
    #get all available historical data for dow jones industrial average
    stock_hist_data = stock.history("MAX")
    
    #add date column in because Power BI doesn't take the index
    stock_hist_data['Date'] = stock_hist_data.index
    
    #add column for ticket to accomodate multiple stocks in same dataframe later
    stock_hist_data['Ticker'] = ticker
    
    #add more additional columns for quotetype, stock name, and sector
    stock_hist_data['Quote Type'] = stock.info['quoteType']
    stock_hist_data['Short Name'] = stock.info['shortName']
    if 'sector' in stock.info:
        stock_hist_data['Sector'] = stock.info['sector']
    else:
        stock_hist_data['Sector'] = ''
  
    if 'sharesOutstanding' in stock.info:
        stock_hist_data['Outstanding Shares'] = stock.info['sharesOutstanding']
    else:
        stock_hist_data['Outstanding Shares'] = ''

    if 'marketCap' in stock.info:
        stock_hist_data['Market Cap'] = stock.info['marketCap']
    else:
        stock_hist_data['Market Cap'] = ''



    #stock_hist_data
    combined_data = combined_data.append(stock_hist_data)
    
combined_data