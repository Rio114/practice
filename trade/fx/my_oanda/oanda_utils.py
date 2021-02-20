import os
import pandas as pd

from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments

# accountID = os.environ["oanda_account_id"]
access_token = os.environ["oanda_access_token"]
api = API(access_token=access_token, environment="live")


def get_candles_df(count, granularity, instrument):
    params = {"count": count, "granularity": granularity}
    r = instruments.InstrumentsCandles(instrument=instrument, params=params)
    data = api.request(r)

    records = []

    for c in data["candles"]:
        records.append(
            [
                c["time"],
                c["complete"],
                c["mid"]["o"],
                c["mid"]["h"],
                c["mid"]["l"],
                c["mid"]["c"],
                c["volume"],
            ]
        )

    cols = ["time", "flg", "O", "H", "L", "C", "V"]
    df = pd.DataFrame(records, columns=cols)
    df["time"] = pd.to_datetime(df["time"])
    df[["O", "H", "L", "C"]] = df[["O", "H", "L", "C"]].astype("float")
    df["V"] = df["V"].astype("int")
    df["flg"] = df["flg"].astype("bool")
    return df


def load_assign_dtype(filename):

    df = pd.read_csv(filename)

    df = df[["time", "flg", "O", "H", "L", "C", "V"]]

    df["time"] = pd.to_datetime(df["time"])
    df[["O", "H", "L", "C"]] = df[["O", "H", "L", "C"]].astype("float")
    df["V"] = df["V"].astype("int")
    df["flg"] = df["flg"].astype("bool")

    return df
