data {
  int n;
  real y[n];
  real sigma[n];
}

parameters {
  real theta[n];
  real mu;
  real<lower=0> tau;
}

model {
  real p = 0;
  for (i in 1:n) p += 1 / square(square(tau) + square(sigma[i]));
  target += 0.5 * log(p) + log(tau);  // Jeffreys prior
  y ~ normal(theta, sigma);
  theta ~ normal(mu, tau);
}
