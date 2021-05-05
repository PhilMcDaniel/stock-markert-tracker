import yfinance as yf
import pandas as pd

dji = yf.Ticker('^DJI')
dji.info
#get all available historical data for dow jones industrial average
dji_hist_data = dji.history("MAX")
#add date column in because Power BI doesn't take the index
dji_hist_data['Date'] = dji_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
dji_hist_data['Ticker'] = '^DJI'
dji_hist_data['Quote Type'] = dji.info['quoteType']
dji_hist_data['Short Name'] = dji.info['shortName']
dji_hist_data['Sector'] = dji.info['sector']

gspc = yf.Ticker('^GSPC')
#gspc.info
#get all available historical data for s&p
gspc_hist_data = gspc.history("MAX")
#add date column in because Power BI doesn't take the index
gspc_hist_data['Date'] = gspc_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
gspc_hist_data['Ticker'] = '^GSPC'
gspc_hist_data['Quote Type'] = gspc.info['quoteType']
gspc_hist_data['Short Name'] = gspc.info['shortName']
gspc_hist_data['Sector'] = gspc.info['sector']

ixic = yf.Ticker('^IXIC')
#ixic.info
#get all available historical data for nasdaq
ixic_hist_data = ixic.history("MAX")
#add date column in because Power BI doesn't take the index
ixic_hist_data['Date'] = ixic_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
ixic_hist_data['Ticker'] = '^IXIC'
ixic_hist_data['Quote Type'] = ixic.info['quoteType']
ixic_hist_data['Short Name'] = ixic.info['shortName']
ixic_hist_data['Sector'] = ixic.info['sector']

aapl = yf.Ticker('AAPL')
#aapl.info
#get all available historical data for apple
aapl_hist_data = aapl.history("MAX")
#add date column in because Power BI doesn't take the index
aapl_hist_data['Date'] = aapl_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
aapl_hist_data['Ticker'] = 'AAPL'
aapl_hist_data['Quote Type'] = aapl.info['quoteType']
aapl_hist_data['Short Name'] = aapl.info['shortName']
aapl_hist_data['Sector'] = aapl.info['sector']

amzn = yf.Ticker('AMZN')
amzn.info
#get all available historical data for amazon
amzn_hist_data = amzn.history("MAX")
#add date column in because Power BI doesn't take the index
amzn_hist_data['Date'] = amzn_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
amzn_hist_data['Ticker'] = 'AMZN'
amzn_hist_data['Quote Type'] = amzn.info['quoteType']
amzn_hist_data['Short Name'] = amzn.info['shortName']
amzn_hist_data['Sector'] = amzn.info['sector']


goog = yf.Ticker('GOOG')
#goog.info
#get all available historical data for amazon
goog_hist_data = goog.history("MAX")
#add date column in because Power BI doesn't take the index
goog_hist_data['Date'] = goog_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
goog_hist_data['Ticker'] = 'GOOG'
goog_hist_data['Quote Type'] = goog.info['quoteType']
goog_hist_data['Short Name'] = goog.info['shortName']
goog_hist_data['Sector'] = goog.info['sector']

msft = yf.Ticker('MSFT')
#msft.info
#get all available historical data for amazon
msft_hist_data = msft.history("MAX")
#add date column in because Power BI doesn't take the index
msft_hist_data['Date'] = msft_hist_data.index
#add column for ticket to accomodate multiple stocks in same dataframe later
msft_hist_data['Ticker'] = 'MSFT'
msft_hist_data['Quote Type'] = msft.info['quoteType']
msft_hist_data['Short Name'] = msft.info['shortName']
msft_hist_data['Sector'] = msft.info['sector']

#combine dataframes into a single dataframe
dataframes = [dji_hist_data,gspc_hist_data,ixic_hist_data,aapl_hist_data,amzn_hist_data,goog_hist_data,msft_hist_data]

combined_data = pd.concat(dataframes)
combined_data
