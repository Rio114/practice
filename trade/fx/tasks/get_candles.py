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
        count = 5000
        granularity = "M1"
        instrument = "USD_JPY"

        df = get_candles_df(count, granularity, instrument)

        df.to_csv("fx/data/lu_df.csv", index=True)
