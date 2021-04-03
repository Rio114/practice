import pandas as pd
import luigi

from tasks.preprocess_candles import PreprocessCandles


class TrainModel(luigi.Task):
    """
    get candle data from OANDA API
    """

    def requires(self):
        return [PreprocessCandles()]

    def output(self):
        return luigi.LocalTarget("fx/data/lu_df_head.csv")

    def run(self):

        # load preprocessed train/valid data
        # train model
        df = pd.read_csv("fx/data/lu_df.csv")
        df.head().to_csv("fx/data/lu_df_head.csv", index=True)
