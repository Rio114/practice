data {
	int<lower=0> N;
	int<lower=0> y[N];
}

parameters {
  real beta;
  real<lower=0> sigma;
  vector[N] r;
}

transformed parameters {
  vector[N] logit_q = beta + r;
}

model {
  y ~ binomial_logit(8, logit_q); // 二項分布
  beta ~ normal(0, 100); // 無情報事前分布
  r ~ normal(0, sigma); // 階層事前分布
  sigma ~ uniform(0, 1.0e+4); // 無情報事前分布
}
