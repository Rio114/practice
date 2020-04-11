#include<iostream>
#include<cmath>
using namespace std;
typedef long long llong;
#define NMAX 1000000001

int main(){
    llong a, b, x;
    cin >> a >> b >> x;

    // llong dmax = log10(NMAX) + 1;
    // llong pmax = a * NMAX + b * dmax;
    // if(pmax <= x){
    //     cout << NMAX <<  endl;
    //     return 0;
    // }    

    llong p, d, n=1, r=NMAX, l=0;
    while(abs(r-l) > 1){
        n = (l + r) / 2;
        d = log10(n) + 1;
        // d = to_string(n).length();
        p = a * n + b * d;

        if(p <= x){
            l = n;
            n = (r + n) / 2;
        } else{
            r = n;
        }
    }
    cout << l << endl;
}
