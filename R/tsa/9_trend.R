

trend <- function(y){
  W <- 1
  V <- 2
  m0 <- 10
  C0 <- 9
  mod <- dlmModPoly(order = 1, dW = W, dV = V, m0 = m0, C0 = C0)
  dlmFiltered_obj <- dlmFilter(y = y, mod = mod)
  m <- dropFirst(dlmFiltered_obj$m)
  m_sdev <- sqrt(
    dropFirst(as.numeric(
      dlmSvd2var(dlmFiltered_obj$U.C, dlmFiltered_obj$D.C)
    ))
  )
  m_quant <- list(m + qnorm(0.25, sd = m_sdev), m + qnorm(0.75, sd = m_sdev))
  ts.plot(cbind(y, m, do.call("cbind", m_quant)),
          col = c("lightgray", "black", "black", "black"),
          lty = c("solid", "solid", "dashed", "dashed"),
          ylim=c(107.5, 109))
  legend(legend = c("観測値", "平均 (フィルタリング分布)", "50%区間 (フィルタリング分布)"),
         lty = c("solid", "solid", "dashed"),
         col = c("lightgray", "black", "black"),
         x = "topright", text.width = 70, cex = 0.6)  
}
