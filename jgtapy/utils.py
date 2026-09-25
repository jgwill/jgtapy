import numpy as np
import pandas as pd
from numpy import mean, absolute


def calculate_sma(df, period, column_name, apply_to):
    """Calculate Simple Moving Averaga"""
    df[column_name] = df[apply_to].rolling(window=period).mean()


def calculate_ao(df, column_name):
    """Calculate Awesome Oscillator"""
    # Data frame for storing temporary data
    df_tmp = pd.DataFrame()

    mp_col = '_median_price'
    df_tmp[mp_col] = (df['High'] + df['Low']) / 2

    sma5_col = '_sma5'
    calculate_sma(df_tmp, 5, sma5_col, mp_col)

    sma34_col = '_sma34'
    calculate_sma(df_tmp, 34, sma34_col, mp_col)

    # Calculate Awesome Oscillator
    df[column_name] = df_tmp[sma5_col] - df_tmp[sma34_col]


def calculate_smma(df, period, column_name, apply_to):
    """Calculate Smoothed Moving Average

    SMMA[period] is the mean of the first `period` values, then
    SMMA[i] = (SMMA[i - 1] * (period - 1) + x[i]) / period.

    The recursion runs over plain floats in that exact order, so the result is
    bit-identical to the row loop below while skipping pandas' per-row access,
    which cost about 1.2 s per line on 3000 bars. Frames not indexed 0..n-1
    keep the row loop, whose `.at[period]` addressing depends on labels.
    """
    index = df.index
    if not (isinstance(index, pd.RangeIndex) and index.start == 0 and index.step == 1):
        return _calculate_smma_by_rows(df, period, column_name, apply_to)
    values = df[apply_to]
    x = values.to_numpy(dtype="float64")
    out = np.full(len(x), np.nan)
    if len(x) > period:
        prev = values.iloc[:period].mean()
        out[period] = prev
        for i in range(period + 1, len(x)):
            prev = (prev * (period - 1) + x[i]) / period
            out[i] = prev
    return pd.DataFrame({column_name: out}, index=index)


def _calculate_smma_by_rows(df, period, column_name, apply_to):
    """The original row loop, kept for frames not indexed 0..n-1."""
    df_tmp = df[[apply_to]]
    first_val = df_tmp[apply_to].iloc[:period].mean()
    df_tmp = df_tmp.assign(column_name=None)
    df_tmp.at[period, column_name] = first_val
    for index, row in df_tmp.iterrows():
        if index > period:
            smma_val = (df_tmp.at[index - 1, column_name] *
                        (period - 1) + row[apply_to]) / period
            df_tmp.at[index, column_name] = smma_val
    df_tmp = df_tmp[[column_name]]
    return df_tmp


def mad(data, axis=None):
    """Calculate Average absolute deviation"""
    return mean(absolute(data - mean(data, axis)), axis)
