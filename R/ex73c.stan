
data {
  int n;
  real y[n];
}

parameters {
  real mu;
  real<lower=0,upper=10> sigma;
}

model {
  y ~ normal(mu, sigma);
}
