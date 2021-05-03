import yfinance as yf
import pandas as pd

dji = yf.Ticker('^DJI')
#dji.info
#get all available historical data for dow jones industrial average
dji_hist_data = dji.history("MAX")
#add date column in because Power BI doesn't take the index
dji_hist_data['Date'] = dji_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
dji_hist_data['Ticker'] = '^DJI'


gspc = yf.Ticker('^GSPC')
#gspc.info
#get all available historical data for s&p
gspc_hist_data = gspc.history("MAX")
#add date column in because Power BI doesn't take the index
gspc_hist_data['Date'] = gspc_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
gspc_hist_data['Ticker'] = '^GSPC'

ixic = yf.Ticker('^IXIC')
#ixic.info
#get all available historical data for nasdaq
ixic_hist_data = ixic.history("MAX")
#add date column in because Power BI doesn't take the index
ixic_hist_data['Date'] = ixic_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
ixic_hist_data['Ticker'] = '^IXIC'

aapl = yf.Ticker('AAPL')
#aapl.info
#get all available historical data for apple
aapl_hist_data = aapl.history("MAX")
#add date column in because Power BI doesn't take the index
aapl_hist_data['Date'] = aapl_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
aapl_hist_data['Ticker'] = 'AAPL'

amzn = yf.Ticker('AMZN')
#aapl.info
#get all available historical data for amazon
amzn_hist_data = amzn.history("MAX")
#add date column in because Power BI doesn't take the index
amzn_hist_data['Date'] = amzn_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
amzn_hist_data['Ticker'] = 'AMZN'

goog = yf.Ticker('GOOG')
#goog.info
#get all available historical data for amazon
goog_hist_data = goog.history("MAX")
#add date column in because Power BI doesn't take the index
goog_hist_data['Date'] = goog_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
goog_hist_data['Ticker'] = 'GOOG'

msft = yf.Ticker('MSFT')
#msft.info
#get all available historical data for amazon
msft_hist_data = msft.history("MAX")
#add date column in because Power BI doesn't take the index
msft_hist_data['Date'] = msft_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
msft_hist_data['Ticker'] = 'MSFT'

#combine dataframes into a single dataframe
dataframes = [dji_hist_data,gspc_hist_data,ixic_hist_data,aapl_hist_data,amzn_hist_data,goog_hist_data,msft_hist_data]

combined_data = pd.concat(dataframes)
combined_data
