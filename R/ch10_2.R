library(dlm)
y <- log(UKDriverDeaths)
t_max <- length(y)
mod <- dlmModPoly(order = 1) + dlmModSeas(frequency = 12)
build_dlm_UKD <- function(par) {
  mod$W[1,1] <- exp(par[1])
  mod$W[2,2] <- exp(par[2])
  mod$V[1,1] <- exp(par[3])
  return(mod)
}

fit_dlm_UKD <- dlmMLE(y=y, parm=rep(0, times=3), build = build_dlm_UKD)

mod <- build_dlm_UKD(fit_dlm_UKD)
cat(diag(mod$W)[1:2], mod$V, "\n")
