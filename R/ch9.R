library(rstan)

fit <- stan("ch9.stan", data = input)
