data {
  int n;
  real ydata[n];
  real s2data[n];
  real s2bar;
}

parameters {
  real m;
  real<lower=log(s2bar)> u;
}

model {
  real t2 = exp(u) - s2bar;
  real z1 = 0;
  real z2 = 0;
  for (i in 1:n) z1 += 1/square(t2+s2data[i]);
  for (i in 1:n) z2 += square(ydata[i]-m)/(t2+s2data[i]) + log(t2+s2data[i]);
  target += (log(z1) - z2) / 2 + u;
}
