#【ローカルレベルモデルに従う人工的なデータの作成】
# 前処理
set.seed(23)
library(dlm)
# ローカルレベルモデルの設定
W <- 1
V <- 2
m0 <- 10
C0 <- 9
mod <- dlmModPoly(order = 1, dW = W, dV = V, m0 = m0, C0 = C0)
# カルマン予測を活用して観測値を作成
t_max <- 200
sim_data <- dlmForecast(mod = mod, nAhead = t_max, sampleNew = 1)
y <- sim_data$newObs[[1]]
# 結果をts型に変換
y <- ts(as.vector(y))
# 結果のプロット
plot(y, ylab = "y")