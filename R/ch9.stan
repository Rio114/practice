
data{
  int num;
  real x[num];
  int y[num];
}

parameters{
  real beta1;
  real beta2;
}

model{
  for (t in 1:num){
    y[t] ~ poisson(exp(beta1+beta2*(x[t] - mean(x))));
  }
}

