data {
  int n;
  real ybar;
  real s2;
}

parameters {
  real x1;
  real x2;
}

model {
  target += -0.5 * (n*x2 + ((n-1)*s2+n*(ybar-x1)^2) / exp(x2));
}
