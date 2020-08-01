

mypois <- function(n, beta1, beta2, x, mu) {
  lambda <- exp(beta1 + beta2 * (x - mu))
  out <- rpois(n=n, lambda=lambda)
  return (out)
}

beta1 <- 3
beta2 <- 0.2
num <- 1000

x <- runif(num, min=3, max=7)
mu <- mean(x)
y <- c()

for (t in 1:num){
  y <- c(y, mypois(1, beta1, beta2, x[t]+runif(1, 0.1, 0.9), mu))
}

input <- list(num=num, x=x, y=y)
