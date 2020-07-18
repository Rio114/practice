parameters {
  real x;
}

model {
  target += -log(1 + square(x));
}
