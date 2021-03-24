import pandas as pd


def df_assign(df):
    df["datetime"] = pd.to_datetime(df["DATE"] + " " + df["TIME"])
    df["year"] = df["datetime"].dt.year
    df["month"] = df["datetime"].dt.month
    df["day"] = df["datetime"].dt.day
    df["hour"] = df["TIME"].apply(lambda x: x.split(":")[0]).astype("int")
    df["dayofweek"] = df["datetime"].dt.dayofweek  # Monday:0 ~ Sunday:6
    df["power"] = df["実績(万kW)"] / 100  # GW unit
    df = df.set_index("datetime")
    return df
