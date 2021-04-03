import pandas as pd
import luigi

from tasks.get_candles import GetCandles


class PreprocessCandles(luigi.Task):
    """
    get candle data from OANDA API
    """

    def requires(self):
        return [GetCandles()]

    def output(self):
        return luigi.LocalTarget("fx/data/lu_df_head.csv")

    def run(self):
        # preprocess
        # split train/valid/test
        df = pd.read_csv("fx/data/lu_df.csv")
        df.head().to_csv("fx/data/lu_df_head.csv", index=True)
