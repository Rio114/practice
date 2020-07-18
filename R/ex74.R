ydata = c(11, 13, 16)
s2data = c(1, 1, 4)
n = length(ydata)             # データの個数
s2bar = 1 / mean(1/s2data)    # 平均の誤差分散
data = list(n=n, ydata=ydata, s2data=s2data, s2bar=s2bar)
fit = stan("ex74a.stan", data=data)
e = extract(fit)
hist(e$m, freq=FALSE, col="gray")
