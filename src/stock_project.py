import pandas as pd
import numpy as np
from pandas_summary import DataFrameSummary
from __future__ import division
import matplotlib.pyplot as plt
# load data into df


def load_data(filepath):
    '''
    Load intraday data from text file

    Parameters
    ----------
    filepath  : str - path to find the intraday data

    Returns
    -------
    df_filter : pandas df
    '''
    df = pd.read_csv(filepath, sep=',', header=None,
                     parse_dates=[0], infer_datetime_format=True)
    df.head()
    # We remove the columns we don't need
    df.drop([3, 4, 5], axis=1, inplace=True)
    # We rename columns for clarity
    df.rename(columns={0: 'date', 1: 'time', 2: 'price',
                       6: 'volume'}, inplace=True)
    # round by hours
    df['hour'] = pd.to_datetime(
        df['time'], format='%H:%M', errors='ignore').dt.hour
    # pivot it to get hours as col and date as index
    df_pivot = pd.pivot_table(df, index='date', values='price',
                              columns='hour', aggfunc=np.mean)
    # add the volatility back
    df_vol = df.groupby(['date'])['volume'].sum()
    df_pivot = pd.concat([df_pivot, df_vol], axis=1)
    # pandas summary shows that the col with less than 1% missing data are 9
    # to 16 (hours)
    # dfs = DataFrameSummary(df_pivot)
    # print dfs.columns_stats
    # we drop the other columns and drop the rows with NAs
    col_to_keep = range(9, 17)
    # col_to_keep.append('volume')
    df_vol = df_pivot['volume']
    df_pivot = df_pivot[col_to_keep]
    df_pivot = df_pivot.dropna(axis=0).reset_index(drop=True)
    # drop rows with low volume
    return df, df_pivot, df_vol

# df = df_pivot
# i = 0


def standerdize(df, df_volume):
    '''
    return a df with standerdize rows

    Parameters
    ----------
    df  : pandas df with col 'colume'

    Returns
    -------
    df_out : pandas df
    '''
    df_ = df
    df_vol = df_volume
    lst_ = []
    for i in range(df_.shape[0]):
        n = df_vol.iloc[i]
        mu = np.mean(df_.iloc[i])
        lst_.append([((x - mu)**2 / n)**0.5 for x in df_.iloc[i]])
    # convert to pandas df
    df_out = pd.DataFrame(lst_)
    # Print detailed summary
    # dfs = DataFrameSummary(df_out)
    # print dfs.columns_stats
    return df_out


def normalise_sod(df):
    '''
    divide each observation with the first data point to avoid start of the day
    leakage (due to off line trading)
    '''
    lst_ = []
    for row in range(df.shape[0]):
        sod = df.iloc[row, 0]
        r_ = df.iloc[row, :] / sod
        # print r_
        lst_.append(r_)

        # lst_.append()
    return pd.DataFrame(lst_)


def analyze_day(df_):
    '''
    return slope for each row
    '''
    # df_ = df[range(9, 17)]
    slope = []
    for i in range(df_.shape[0]):
        start = df_.iloc[i, 0]
        end = df_.iloc[i, -1]
        rate = (end - start) / end
        slope.append(rate)
    return slope


def analyze_half_day(df_):
    '''
    return slope for each row
    '''
    # df_ = df[range(9, 17)]
    slope = []
    for i in range(df_.shape[0]):
        start = df_.iloc[i, 0]
        end = df_.iloc[i, -5]
        rate = (end - start) / end
        slope.append(rate)
    return slope


if __name__ == '__main__':
    filepath = 'data/IBM_adjusted.txt'
    df_raw, df_day, df_volume = load_data(filepath)
    df_norm = normalise_sod(df_day)
    # df.head()

    # df.to_clipboard()
    df_std = standerdize(df_norm, df_volume)

    df_raw.head()
    stock_price = df_raw.price

    plt.plot(stock_price)
    plt.show()

    df_std.head()
    df_std.shape
    print df_std.shape[0]
    # df_std.columns.tolist()
    # slopes = np.array(analyze_day(df_std))
    # slopes_half_day = np.array(analyze_half_day(df_std))
    #
    # n = slopes
    # n_neg = (slopes < 0).astype(int)
    # n_neg_half_day = (slopes_half_day < 0).astype(int)
    # df = pd.DataFrame(
    #     {'day_slope': n, 'half_day': n_neg_half_day, 'eod': n_neg})
    # df['eod-halfday'] = df['eod'] - df['half_day']
    # # to check again - this is the % of day following same pattern am and PM
    # # also need to start the day at 0
    # # scraper titles
    # # find when to sell (profit curve)
    # # level prediction
    # # http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
    # # slope by hour / day / mid day
    # # predict next day (healthyness of the company)
    # len(df[df['eod-halfday'] == 0]) / len(df)
