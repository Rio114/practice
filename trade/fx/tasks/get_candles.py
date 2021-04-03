import os

import luigi
import pandas as pd

from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments


class GetCandles(luigi.Task):
    """
    get candle data from OANDA API
    """

    def requires(self):
        pass

    def output(self):
        return luigi.LocalTarget("fx/data/lu_df.csv")

    def run(self):

        access_token = os.environ["oanda_access_token"]

        api = API(access_token=access_token, environment="live")

        params = {"count": 1000, "granularity": "M1"}
        r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
        data = api.request(r)

        prices = []
        for c in data["candles"]:
            prices.append(
                [
                    c["time"],
                    c["mid"]["o"],
                    c["mid"]["h"],
                    c["mid"]["l"],
                    c["mid"]["c"],
                    c["volume"],
                ]
            )

        df = pd.DataFrame(
            prices, columns=["time", "open", "high", "low", "close", "volume"]
        )
        df["time"] = pd.to_datetime(df["time"])
        df = df.set_index("time")

        df.to_csv("fx/data/lu_df.csv", index=True)
