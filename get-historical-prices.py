import yfinance as yf
import pandas as pd

dji = yf.Ticker('^DJI')
#dji.info

#get all available historical data
dji_hist_data = dji.history("MAX")

#add date column in because Power BI doesn't take the index
dji_hist_data['Date'] = dji_hist_data.index

#add column for ticket to accomodate multiple stocks in same dataframe later
dji_hist_data['Ticker'] = '^DJI'



gspc = yf.Ticker('^GSPC')
#gspc.info

#get all available historical data
gspc_hist_data = gspc.history("MAX")

#add date column in because Power BI doesn't take the index
gspc_hist_data['Date'] = gspc_hist_data.index

#add column for ticket to accomodate multiple stocks in same dataframe later
gspc_hist_data['Ticker'] = '^GSPC'



#combine dataframes into a single dataframe
dataframes = [dji_hist_data,gspc_hist_data]

combined_data = pd.concat(dataframes)
combined_data