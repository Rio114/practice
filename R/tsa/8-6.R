#【カルマンフィルタリング】
# フィルタリング処理

kalm_filtering <- function(data){
  #【ローカルレベルモデルにおけるパラメータ値の特定】
  # モデルを定義・構築するユーザ定義関数
  build_dlm <- function(par) {
    mod$W[1, 1] <- exp(par[1])
    mod$V[1, 1] <- exp(par[2])
    return(mod)
  }
  # パラメータの最尤推定（探索初期値を3回変えて結果を確認）
  lapply(list(c(0, 0), c(1, 10), c(20, 3)), function(parms){
    dlmMLE(y = data, parm = parms, build = build_dlm)
  })
  # パラメータの最尤推定（ヘッセ行列を戻り値に含める）
  fit_dlm <- dlmMLE(y = data, parm = c(0, 0), build = build_dlm, hessian = TRUE)
  # デルタ法により最尤推定の（漸近的な）標準誤差をヘッセ行列から求める
  exp(fit_dlm$par) * sqrt(diag(solve(fit_dlm$hessian)))
  # パラメータの最尤推定結果をモデルに設定
  mod <- build_dlm(fit_dlm$par)

  
  
  dlmFiltered_obj <- dlmFilter(y = data, mod = mod)
  # 結果の確認
  str(dlmFiltered_obj, max.level = 1)
  # フィルタリング分布の平均と標準偏差を求める
  m <- dropFirst(dlmFiltered_obj$m)
  m_sdev <- sqrt(
    dropFirst(as.numeric(
      dlmSvd2var(dlmFiltered_obj$U.C, dlmFiltered_obj$D.C)
    ))
  )
  # フィルタリング分布の95%区間のために、2.5%値と97.5%値を求める
  m_quant <- list(m + qnorm(0.025, sd = m_sdev), m + qnorm(0.975, sd = m_sdev))
  # 結果のプロット
  ts.plot(cbind(data, m, do.call("cbind", m_quant)),
          col = c("lightgray", "black", "black", "black"),
          lty = c("solid", "solid", "dashed", "dashed"))
  # 凡例
  legend(legend = c("観測値", "平均 (フィルタリング分布)", "95%区間 (フィルタリング分布)"),
         lty = c("solid", "solid", "dashed"),
         col = c("lightgray", "black", "black"),
         x = "topright", text.width = 32, cex = 0.6)

}
