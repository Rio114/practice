

library(dlm)
mod <- dlmModPoly(order = 1)
str(mod)

build_dlm <- function(par) {
  mod$W[1, 1] <- exp(par[1])
  mod$V[1, 1] <- exp(par[2])
  return(mod)
}
lapply(list(c(0, 0), c(1, 10), c(20, 3)), function(parms){
  dlmMLE(y = Nile, parm = parms, build = build_dlm)
})
fit_dlm <- dlmMLE(y = Nile, parm = c(0, 0), build = build_dlm, hessian = TRUE)
exp(fit_dlm$par) * sqrt(diag(solve(fit_dlm$hessian)))
mod <- build_dlm(fit_dlm$par)
mod


dlmFiltered_obj <- dlmFilter(y = Nile, mod = mod)
str(dlmFiltered_obj, max.level = 1)
m <- dropFirst(dlmFiltered_obj$m)
m_sdev <- sqrt(
  dropFirst(as.numeric(
    dlmSvd2var(dlmFiltered_obj$U.C, dlmFiltered_obj$D.C)
  ))
)
m_quant <- list(m + qnorm(0.025, sd = m_sdev), m + qnorm(0.975, sd = m_sdev))
ts.plot(cbind(Nile, m, do.call("cbind", m_quant)),
        col = c("lightgray", "black", "black", "black"),
        lty = c("solid", "solid", "dashed", "dashed"))
legend(legend = c("観測値", "平均 (フィルタリング分布)", "95%区間 (フィルタリング分布)"),
       lty = c("solid", "solid", "dashed"),
       col = c("lightgray", "black", "black"),
       x = "topright", text.width = 32, cex = 0.6)
