
# 前処理
library(dlm)
# データの読み込み
Ryori <- read.csv("data/CO2.csv")
# データをts型に変換し、2014年12月までで打ち切る
y_all <- ts(data = Ryori$CO2, start = c(1987, 1), frequency = 12)
y <- window(y_all, end = c(2014, 12))
# モデルの設定：ローカルトレンドモデル+周期モデル(時間領域アプローチ)
build_dlm_CO2a <- function(par) {
  return(
    dlmModPoly(order = 2, dW = exp(par[1:2]), dV = exp(par[3])) +
      dlmModSeas(frequency = 12, dW = c(exp(par[4]), rep(0, times = 10)), dV = 0)
  )
}
# パラメータの最尤推定と結果の確認
fit_dlm_CO2a <- dlmMLE(y = y, parm = rep(0, 4), build = build_dlm_CO2a)
fit_dlm_CO2a
# パラメータの最尤推定結果をモデルに指定
mod  <- build_dlm_CO2a(fit_dlm_CO2a$par)
# カルマンフィルタリング
dlmFiltered_obj  <- dlmFilter(y = y, mod = mod)
dlmFiltered_obja <- dlmFiltered_obj              # 後で予測値を比較するために別名で保存
# フィルタリング分布の平均
mu <- dropFirst(dlmFiltered_obj$m[, 1])
gamma <- dropFirst(dlmFiltered_obj$m[, 3])
# 結果のプロット
oldpar <- par(no.readonly = TRUE)
par(mfrow = c(3, 1)); par(oma = c(2, 0, 0, 0)); par(mar = c(2, 4, 1, 1))
ts.plot(    y, ylab = "観測値")
ts.plot(   mu, ylab = "レベル成分", ylim = c(350, 405))
ts.plot(gamma, ylab = "周期成分"  , ylim = c( -9,   6))
mtext(text = "Time", side = 1, line = 1, outer = TRUE)
par(oldpar)
# 対数尤度の確認
-dlmLL(y = y, mod = mod)