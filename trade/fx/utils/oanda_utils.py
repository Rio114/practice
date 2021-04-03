import os
import datetime
import time

import pandas as pd

from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments

# accountID = os.environ["oanda_account_id"]
access_token = os.environ["oanda_access_token"]
api = API(access_token=access_token, environment="live")


def assign_dtype(df):
    df["time"] = pd.to_datetime(df["time"])
    df[["O", "H", "L", "C"]] = df[["O", "H", "L", "C"]].astype("float")
    df["V"] = df["V"].astype("int")
    df["flg"] = df["flg"].astype("bool")
    return df


def get_candles_df(instrument, params):

    start = datetime.datetime.strptime(params["from"], "%Y-%m-%d")
    end = datetime.datetime.strptime(params["to"], "%Y-%m-%d")

    days = (end - start).days

    dfs = []
    for d in range(days):
        start_temp = start + datetime.timedelta(days=d)
        end_temp = start_temp + datetime.timedelta(days=1)

        from_temp = f"{start_temp.year}-{start_temp.month}-{start_temp.day}"
        from_temp += "T00:00:00.000000000Z"

        end_temp = f"{end_temp.year}-{end_temp.month}-{end_temp.day}"
        end_temp += "T00:00:00.000000000Z"

        params_temp = {"granularity": "M1", "from": from_temp, "to": end_temp}

        res = instruments.InstrumentsCandles(instrument=instrument, params=params_temp)
        data = api.request(res)

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
        dfs.append(pd.DataFrame(records, columns=cols))
        time.sleep(0.5)

    df = assign_dtype(pd.concat(dfs, axis=0))
    return df


def load_candles_df(filename):
    df = pd.read_csv(filename)
    df = df[["time", "flg", "O", "H", "L", "C", "V"]]
    df = assign_dtype(df)
    return df
