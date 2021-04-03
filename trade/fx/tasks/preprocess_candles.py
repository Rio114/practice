import luigi

from tasks.get_candles import GetCandles
from utils.oanda_utils import load_candles_df


class PreprocessCandles(luigi.Task):
    """
    get candle data from OANDA API
    """

    def requires(self):
        return [GetCandles()]

    def output(self):
        return luigi.LocalTarget("fx/data/usd_jpy_m1_head.csv")

    def run(self):
        # preprocess
        # split train/valid/test
        df = load_candles_df("fx/data/usd_jpy_m1.csv")
        df.head().to_csv("fx/data/usd_jpy_m1_head.csv", index=True)
