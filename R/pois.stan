data {
    int n;
    int x[n];
}
parameters {
    real lambda;
}
model {
    x ~ poisson(lambda);
}
