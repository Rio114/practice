#include<iostream>
#include<cmath>
using namespace std;
typedef long long llong;
#define NMAX 1000000000

int main(){
    llong a, b, x;
    cin >> a >> b >> x;

    llong dmax = log10(NMAX) + 1;
    llong pmax = a * NMAX + b* dmax;
    if(pmax <= x){
        cout << NMAX <<  endl;
        return 0;
    }    

    llong p, d, n=1, nmax=NMAX-1, nmin=1;
    while(1){
        d = log10(n) + 1;
        p = a * n + b * d;

        if(p < x){
            nmin = n;
            if(nmax - nmin == 1) break;
            else n = (nmax + nmin) / 2 ;
        }else{
            nmax = n;
            n = n / 2;
            if(n < 1) {
                break;
            }
        }
    }
    cout << n << endl;
}
