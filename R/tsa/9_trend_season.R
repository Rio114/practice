library(dlm)


#y <- window(y_all, end = end)

trend_season <- function(y, frequency = 1){
  
  build_dlm <- function(par) {
    return(
      dlmModPoly(order = 2, dW = exp(par[1:2]), dV = exp(par[3])) +
        dlmModSeas(frequency = 12, dW = c(exp(par[4]), rep(0, times = 10)), dV = 0)
    )
  }
  
  fit_dlm <- dlmMLE(y = y, parm = rep(0, 4), build = build_dlm)
  fit_dlm
  
  mod  <- build_dlm(fit_dlm$par)
  
  dlmFiltered_obj  <- dlmFilter(y = y, mod = mod)
  dlmFiltered_obja <- dlmFiltered_obj              # 後で予測値を比較するために別名で保存
  
  mu <- dropFirst(dlmFiltered_obj$m[, 1])
  gamma <- dropFirst(dlmFiltered_obj$m[, 3])
  
  oldpar <- par(no.readonly = TRUE)
  par(mfrow = c(3, 1)); par(oma = c(2, 0, 0, 0)); par(mar = c(2, 4, 1, 1))
  ts.plot(    y, ylab = "観測値")
  ts.plot(   mu, ylab = "レベル成分", ylim = c( 107,   110))
  ts.plot(gamma, ylab = "周期成分"  , ylim = c( -1,   1))
  mtext(text = "Time", side = 1, line = 1, outer = TRUE)
  par(oldpar)
  # 対数尤度の確認
  -dlmLL(y = y, mod = mod)  
  
  
}
