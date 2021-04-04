from utils.indicators import add_sma


def split_df(df, train_start, valid_start, test_start, test_end):
    cond_train = df.index >= train_start
    cond_train &= df.index < valid_start
    df_train = df[cond_train].copy()

    cond_valid = df.index >= valid_start
    cond_valid &= df.index < test_start
    df_valid = df[cond_valid].copy()

    cond_test = df.index >= test_start
    cond_test &= df.index < test_end
    df_test = df[cond_test].copy()

    return df_train, df_valid, df_test


def add_target(df, target_window, align="C"):
    df["target"] = add_sma(df, target_window, align)[f"sma_{target_window}"].shift(
        -target_window
    )
    df["future_highest"] = df.rolling(target_window)["H"].max().shift(-target_window)
    df["future_lowest"] = df.rolling(target_window)["L"].min().shift(-target_window)
    return df
