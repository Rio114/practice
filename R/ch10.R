library(rstan)

d <- read.csv(url("https://kuboweb.github.io/-kubo/stat/iwanamibook/fig/hbm/data7a.csv"))

input <- list(N=nrow(d),y=d$y)

d.fit <- stan(file='ch10.stan', data=input, iter=1000, chains=4)

