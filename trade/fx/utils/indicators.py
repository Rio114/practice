import numpy as np


def add_sma(df, window, align="C"):
    df[f"sma_{window}"] = df[align].rolling(window).mean()
    return df


def add_ema(df, window, align="C"):
    ema = np.zeros(len(df))
    ema[:] = np.nan  # NaN で一旦初期化
    ema[window - 1] = df[align][:window].mean()  # 最初だけ単純移動平均で算出

    for day in range(window, len(df)):
        ema[day] = ema[day - 1] + (df[align][day] - ema[day - 1]) / (window + 1) * 2

    df[f"ema_{window}"] = ema
    return df
