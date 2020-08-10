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
  y ~ binomial_logit(8, logit_q); // �񍀕��z
  beta ~ normal(0, 100); // ����񎖑O���z
  r ~ normal(0, sigma); // �K�w���O���z
  sigma ~ uniform(0, 1.0e+4); // ����񎖑O���z
}
