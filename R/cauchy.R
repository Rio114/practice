N = 100000              # 繰返し回数
a = numeric(N)          # 値を保存するための長さNの配列
x = 0                   # 初期値
p = 1 / (1 + x^2)       # 確率
for (i in 1:N) {
     y = rnorm(1, x, 1)    # 候補（選び方は対称なら何でもよい）
     q = 1 / (1 + y^2)     # 確率
     if (runif(1) < q/p) { # 更新
         x = y
         p = q
       }
     a[i] = x
   }
hist(a, freq=FALSE, breaks=seq(-1000,1000,0.2), xlim=c(-5,5), col="gray")
curve(dcauchy(x), add=TRUE)