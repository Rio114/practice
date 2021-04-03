import luigi
from utils.oanda_utils import get_candles_df


class GetCandles(luigi.Task):
    """
    get candle data from OANDA API
    """

    def requires(self):
        pass

    def output(self):
        return luigi.LocalTarget("fx/data/usd_jpy_m1.csv")

    def run(self):
        params = {
            # "count": 5000,
            "granularity": "M1",
            "from": "2021-3-23",
            "to": "2021-3-28",
        }
        instrument = "USD_JPY"

        df = get_candles_df(instrument, params)
        df.to_csv("fx/data/usd_jpy_m1.csv", index=True)
