from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import adfuller
from scipy.stats import jarque_bera


def hoge():
    print("hoge")


def jarque_bera_normal_dist(arr):
    jarque_bera_test = jarque_bera(arr)
    print("Jack Bera:", "\t", jarque_bera_test)


def ljung_box_auto_corr(arr, lags):
    res = acorr_ljungbox(arr, lags=lags)
    lag = 1
    for lb, p in zip(res[0], res[1]):
        print(lag, lb, p)
        lag += 1


def adfuller_unit_root(arr):
    for r in ["ctt", "ct", "c", "nc"]:
        print(f"---{r}---")
        res = adfuller(
            arr, maxlag=None, regression=r, autolag="AIC", store=False, regresults=False
        )
        print(res)
