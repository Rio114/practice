#【MCMCを活用したローカルレベルモデルの平滑化（パラメータが既知）】
# 前処理
set.seed(123)
library(rstan)
# Stanの事前設定：コードのHDD保存、並列演算、グラフの縦横比
rstan_options(auto_write = TRUE)
options(mc.cores = parallel::detectCores())
theme_set(theme_get() + theme(aspect.ratio = 3/4))
# 人工的なローカルレベルモデルに関するデータを読み込み
load(file = "ArtifitialLocalLevelModel.RData")
# モデル：生成・コンパイル
stan_mod_out <- stan_model(file = "model10-1.stan")
# 平滑化：実行（サンプリング）
fit_stan <- sampling(object = stan_mod_out,
                     data = list(t_max = t_max, y = y, 
                                 W = mod$W, V = mod$V, 
                                 m0 = mod$m0, C0 = mod$C0),
                     pars = c("x"),
                     seed = 123
)
# 結果の確認
oldpar <- par(no.readonly = TRUE); options(max.print = 99999)
fit_stan
options(oldpar)
traceplot(fit_stan, pars = c(sprintf("x[%d]", 100), "lp__"), alpha = 0.5)
# 必要なサンプリング結果を取り出す
stan_mcmc_out <- rstan::extract(fit_stan, pars = "x")
str(stan_mcmc_out)
# 周辺化を行い、平均・25%値・75%値を求める
s_mcmc <- colMeans(stan_mcmc_out$x)
s_mcmc_quant <- apply(stan_mcmc_out$x, 2, FUN = quantile, probs=c(0.25, 0.75))
# 以降のコードは表示を省略
# 結果のプロット
ts.plot(cbind(y, s), col = c("lightgray", "blue"))
lines(s_mcmc, col = "red", lty = "dashed")
# 凡例
legend(legend = c("観測値", "平均 （カルマン平滑化)",  "平均 （MCMC)"),
       lty = c("solid", "solid", "dashed"),
       col = c("lightgray", "blue", "red"),
       x = "topright", text.width = 50, cex = 0.6)
# 結果のプロット
ts.plot(cbind(y, do.call("cbind", s_quant)),
        col = c("lightgray", "blue", "blue"))
lines(s_mcmc_quant["25%", ], col = "red", lty = "dashed")
lines(s_mcmc_quant["75%", ], col = "red", lty = "dashed")
# 凡例
legend(legend = c("観測値", "50%区間 （カルマン平滑化)",  "50%区間 （MCMC)"),
       lty = c("solid", "solid", "dashed"),
       col = c("lightgray", "blue", "red"),
       x = "topright", text.width = 60, cex = 0.6)