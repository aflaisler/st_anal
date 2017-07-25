from pandas_datareader import data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
from pandas_summary import DataFrameSummary

# http://www.learndatasci.com/python-finance-part-yahoo-finance-api-pandas-matplotlib/
# Define the instruments to download. We would like to see Apple,
# Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', 'SPY']


s1 = ["A2", "AMZN", "AN", "AZO", "BBBY", "BBY", "BWA", "KMX",
      "CCL", "CBS", "CHTR", "CMG", "COH", "CMCSA", "DHI", "DRI"]
s2 = ["DLPH", "DISCA", "DISCK", "DISH", "DG", "DLTR", "EXPE", "FL",
      "F", "GPS", "GRMN", "GM", "GPC", "GT", "HBI", "HOG", "HAS"]
s3 = ["HLT", "HD", "IPG", "KSS", "LB", "LEG", "LEN", "LKQ", "LOW",
      "M", "MAR", "MAT", "MCD", "KORS", "MHK", "NWL", "NWSA", "NWS"]
s4 = ["NKE", "JWN", "ORLY", "OMC", "RL", "PCLN", "PHM", "PVH",
      "ROST", "RCL", "SNI", "SIG", "SNA", "SWK", "SPLS", "SBUX", "TGT"]
s5 = ["TIF", "TWX", "TJX", "TSCO", "TRIP", "FOXA", "FOX", "ULTA",
      "UA", "UAA", "VFC", "VIAB", "DIS", "WHR", "WYN", "WYNN", "YUM"]
s6 = ["MO", "ADM", "BF.B", "CPB", "CHD", "CLX", "KO", "CL", "CAG",
      "STZ", "COST", "COTY", "CVS", "DPS", "EL", "GIS", "HSY", "HRL"]
s7 = ["SJM", "K", "KMB", "KHC", "KR", "MKC", "TAP", "MDLZ", "MNST",
      "PEP", "PM", "PG", "RAI", "SYY", "TSN", "WMT", "WBA", "WFM"]
s8 = ["APC", "APA", "BHGE", "COG", "CHK", "CVX", "XEC", "CXO", "COP",
      "DVN", "EOG", "EQT", "XOM", "HAL", "HP", "HES", "KMI", "MRO"]
s9 = ["MPC", "MUR", "NOV", "NFX", "NBL", "OXY", "OKE", "PSX", "PXD",
      "RRC", "SLB", "FTI", "TSO", "RIG", "VLO", "WMB", "AMG", "AFL"]
# , "ALL", "AXP", "AIG", "AMP", "AON", "AJG", "AIZ", "BAC", "BK", "BBT", "BRK.B", "BLK", "HRB", "COF", "CBOE", "SCHW", "CB", "CINF", "C", "CFG", "CME", "CMA", "DFS", "ETFC", "RE", "FITB", "BEN", "GS", "HIG", "HBAN", "ICE", "IVZ", "JPM", "KEY", "LUK", "LNC", "L", "MTB", "MMC", "MET", "MCO", "MS", "NDAQ", "NAVI", "NTRS", "PBCT", "PNC", "PFG", "PGR", "PRU", "RJF", "RF", "SPGI", "STT", "STI", "SYF", "TROW", "TMK", "TRV", "USB", "UNM", "WFC", "WLTW", "XL", "ZION", "ABT", "ABBV", "AET", "A", "ALXN", "ALGN", "AGN", "ABC", "AMGN", "ANTM", "BCR", "BAX", "BDX", "BIIB", "BSX", "BMY", "CAH", "CELG", "CNC", "CERN", "CI", "COO", "DHR", "DVA", "XRAY", "EW", "EVHC", "ESRX", "GILD", "HCA", "HSIC",
# "HOLX", "HUM", "IDXX", "ILMN", "INCY", "ISRG", "JNJ", "LH", "LLY", "MNK", "MCK", "MDT", "MRK", "MTD", "MYL", "PDCO", "PKI", "PRGO", "PFE", "DGX", "REGN", "SYK", "TMO", "UNH", "UHS", "VAR", "VRTX", "WAT", "ZBH", "ZTS", "MMM", "AYI", "ALK", "ALLE", "AAL", "AME", "ARNC", "BA", "CHRW", "CAT", "CTAS", "CSX", "CMI", "DE", "DAL", "DOV", "ETN", "EMR", "EFX", "EXPD", "FAST", "FDX", "FLS", "FLR", "FTV", "FBHS", "GD", "GE", "GWW", "HON", "INFO", "ITW", "IR", "JEC", "JBHT", "JCI", "KSU", "LLL", "LMT", "MAS", "NLSN", "NSC", "NOC", "PCAR", "PH", "PNR", "PWR", "RTN", "RSG", "RHI", "ROK", "COL", "ROP", "LUV", "SRCL", "TXT",
# "TDG", "UNP", "UAL", "UPS", "URI", "UTX", "VRSK", "WM", "XYL", "ACN", "ATVI", "ADBE", "AMD", "AKAM", "ADS", "GOOGL", "GOOG", "APH", "ADI", "ANSS", "AAPL", "AMAT", "ADSK", "ADP", "AVGO", "CA", "CSCO", "CTXS", "CTSH", "GLW", "CSRA", "DXC", "EBAY", "EA", "FFIV", "FB", "FIS", "FISV", "FLIR", "IT", "GPN", "HRS", "HPE", "HPQ", "INTC", "IBM", "INTU", "JNPR", "KLAC", "LRCX", "MA", "MCHP",
#  "MU", "MSFT", "MSI", "NTAP", "NFLX", "NVDA", "ORCL", "PAYX", "PYPL", "QRVO", "QCOM", "RHT", "CRM", "STX", "SWKS", "SYMC", "SNPS", "TEL", "TXN", "TSS", "VRSN", "V", "WDC", "WU", "XRX", "XLNX", "APD", "ALB", "AVY", "BLL", "CF", "DOW", "DD", "EMN", "ECL", "FMC", "FCX", "IP", "IFF", "LYB", "MLM", "MON", "MOS", "NEM", "NUE", "PPG", "PX", "SEE", "SHW", "VMC", "WRK", "ARE", "AMT", "AIV", "AVB", "BXP", "CBG", "CCI", "DLR", "EQIX", "EQR", "ESS", "EXR", "FRT", "GGP", "HCP", "HST", "IRM", "KIM", "MAC", "MAA", "PLD", "PSA", "O", "REG", "SPG", "SLG", "UDR", "VTR", "VNO", "HCN", "WY", "T", "CTL", "LVLT", "VZ", "AES", "LNT", "AEE", "AEP", "AWK", "CNP", "CMS", "ED", "D", "DTE", "DUK", "EIX", "ETR", "ES", "EXC", "FE", "NEE", "NI", "NRG", "PCG", "PNW", "PPL", "PEG", "SCG", "SRE", "SO", "WEC", "XEL"]
lst = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s9]
# lst = [s1]
tickers = []
for ls in lst:
    tickers.extend(ls)

# len(tickers)

# Define which online source one should use
data_source = 'google'

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2016-01-04'
end_date = datetime.date.today().strftime('%Y-%m-%d')

# User pandas_reader.data.DataReader to load the desired data. As simple
# as that.
panel_data = data.DataReader(tickers, data_source, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data.loc['Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# close.tail(10)


#
# close['AMZN']

# Getting just the  closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data.loc['Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
adj_close = close.fillna(method='ffill')

# adj_close = adj_close.dropna(axis=1, how='all')

adj_close = adj_close.dropna(thresh=adj_close.shape[0] - 2, axis=1)
# adj_close=adj_close.dropna(axis=0)
# adj_close.tail(10)


# adj_close.describe()
dfs = DataFrameSummary(adj_close)
dfs.columns_stats
adj_close.shape

# adj_close.to_clipboard()
# tickers = ['AMZN']
stocks = adj_close.columns

for stock in stocks:
    # Get the stock time series. This now returns a Pandas Series object
    # indexed by date
    stk_name = stock
    stock = adj_close.loc[:, stock]
    # Calculate the 20 and 100 days moving averages of the closing prices
    short_rolling_stock = stock.rolling(window=20).mean()
    long_rolling_stock = stock.rolling(window=100).mean()

    # Plot everything by leveraging the very powerful matplotlib package
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.title(stk_name)
    ax.plot(stock.index, stock, label=stock)
    ax.plot(short_rolling_stock.index,
            short_rolling_stock, label='20 days rolling')
    ax.plot(long_rolling_stock.index,
            long_rolling_stock, label='100 days rolling')
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Adjusted closing price ($)')
    # ax.legend()
plt.show()
