# 前処理
library(dlm)
# データの読み込み
beer <- read.csv("data/BEER.csv")
# データをts型に変換
y <- ts(beer$Shipping_Volume, frequency = 12, start = c(2003, 1))
# プロット
plot(y)
# データの対数変換
y <- log(y)
# 対数変換後のデータのプロット
plot(y, ylab = "log(y)")