#【ローカルレベルモデル+周期モデル(時間領域アプローチ)】
# モデルの設定：ローカルレベルモデル+周期モデル(時間領域アプローチ)
build_dlm_CO2b <- function(par) {
  return(
    dlmModPoly(order = 1, dW = exp(par[1]), dV = exp(par[2])) +
      dlmModSeas(frequency = 12, dW = c(exp(par[3]), rep(0, times = 10)), dV = 0)
  )
}
# 以降のコードは表示を省略
# パラメータの最尤推定と結果の確認
fit_dlm_CO2b <- dlmMLE(y = y, parm = rep(0, 3), build = build_dlm_CO2b)
fit_dlm_CO2b
# パラメータの最尤推定結果をモデルに指定
mod  <- build_dlm_CO2b(fit_dlm_CO2b$par)
# カルマンフィルタリング
dlmFiltered_obj  <- dlmFilter(y = y, mod = mod)
dlmFiltered_objb <- dlmFiltered_obj              # 後で予測値を比較するために別名で保存
# フィルタリング分布の平均
mu <- dropFirst(dlmFiltered_obj$m[, 1])
gamma <- dropFirst(dlmFiltered_obj$m[, 2])
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