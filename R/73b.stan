data {
  int n;
  real y[n];
}

parameters {
  real mu;
  real logsigma;
}

model {
  y ~ normal(mu, exp(logsigma));
}

