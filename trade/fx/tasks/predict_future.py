import pandas as pd
import luigi

from tasks.preprocess_candles import PreprocessCandles
from tasks.train_model import TrainModel


class PredictFuture(luigi.Task):
    """"""

    def requires(self):
        return [PreprocessCandles(), TrainModel()]

    def output(self):
        return luigi.LocalTarget("fx/data/")

    def run(self):

        # load preprocessed test data
        # load trained model
        # predict future
        df = pd.read_csv("fx/data/")
        df.head().to_csv("fx/data/", index=True)
