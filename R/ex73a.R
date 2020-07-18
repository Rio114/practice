y = 1:3   # データの例
n = length(y)
ybar = mean(y)
s2 = var(y)
#data = list(n=n, ybar=ybar, s2=s2)
#fit = stan("ex73a.stan", data=data, iter=26000, warmup=1000)
data = list(n=n, y=y)
fit = stan("ex73c.stan", data=data, iter=26000, warmup=1000)


e = extract(fit)

hist(e$mu, col="gray", freq=FALSE, xlim=c(-5,5), breaks=seq(-1000,1000,0.2))

#hist((e$x1-ybar)/sqrt(s2/n), col="gray", freq=FALSE, xlim=c(-5,5), breaks=seq(-1000,1000,0.2))
#curve(dt(x,n-1), add=TRUE)

#hist((n-1)*s2/exp(e$x2), col="gray", freq=FALSE, xlim=c(0,10), breaks=(0:500)/5)
#curve(dchisq(x,n-1), add=TRUE)

