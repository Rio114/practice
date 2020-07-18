y = 1:3         # データ
n = length(y)
ybar = mean(y)
s2 = var(y)
logpost = function(x1, x2) {
  -0.5 * (n*x2 + ((n-1)*s2+n*(ybar-x1)^2) / exp(x2))
}
x1 = ybar      # 適当な初期値
x2 = log(s2)   # 適当な初期値
lp = logpost(x1, x2)  # 現在の事後分布の対数
N = 100000     # 繰返し数（とりあえず10万）
x1trace = x2trace = numeric(N)  # 事後分布のサンプルを格納する配列
for (i in 1:N) {
  y1 = rnorm(1, x1, 1)  # 次の候補
  y2 = rnorm(1, x2, 1)  # 次の候補
  lq = logpost(y1, y2)  # 次の候補の事後分布の対数
  if (lp - lq < rexp(1)) {  # メトロポリスの更新（対数版）
    x1 = y1
    x2 = y2
    lp = lq
  }
  x1trace[i] = x1  # 配列に格納
  x2trace[i] = x2  # 配列に格納
}
