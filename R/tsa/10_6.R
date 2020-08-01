
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
stan_mod_out <- stan_model(file = "model10-3.stan")
# 平滑化：実行（サンプリング）
dim(mod$m0) <- 1               # ベクトル要素が1つの場合は、明示的に次元を設定
fit_stan <- sampling(object = stan_mod_out,
                     data = list(t_max = t_max, y = matrix(y, nrow = 1), 
                                 G = mod$G, F = t(mod$F),
                                 m0 = mod$m0, C0 = mod$C0),
                     pars = c("W", "V"),
                     seed = 123
)
# 結果の確認
fit_stan
traceplot(fit_stan, pars = c("W", "V"), alpha = 0.5)
