
# モデルの設定：ローカルトレンドモデル+周期モデル(時間領域アプローチ)
build_dlm_BEERa <- function(par){
  return(
    dlmModPoly(order = 2, dW = exp(par[1:2]), dV = exp(par[3])) +
      dlmModSeas(frequency = 12, dW = c(exp(par[4]), rep(0, times = 10)), dV = 0)
  )
}
# パラメータの最尤推定と結果の確認
fit_dlm_BEERa <- dlmMLE(y = y, parm = rep(0, 4), build = build_dlm_BEERa)
fit_dlm_BEERa
# パラメータの最尤推定結果をモデルに指定
mod <- build_dlm_BEERa(fit_dlm_BEERa$par)
# カルマン平滑化
dlmSmoothed_obj <- dlmSmooth(y = y, mod = mod)
# 平滑化分布の平均
mu <- dropFirst(dlmSmoothed_obj$s[, 1])
gamma <- dropFirst(dlmSmoothed_obj$s[, 3])
# 結果のプロット
oldpar <- par(no.readonly = TRUE)
par(mfrow = c(3, 1)); par(oma = c(2, 0, 0, 0)); par(mar = c(2, 4, 1, 1))
ts.plot(    y, ylab = "観測値(対数変換後)")
ts.plot(   mu, ylab = "レベル成分")
ts.plot(gamma, ylab = "周期成分")
mtext(text = "Time", side = 1, line = 1, outer = TRUE)
par(oldpar)
# 対数尤度の確認
-dlmLL(y = y, mod = mod)