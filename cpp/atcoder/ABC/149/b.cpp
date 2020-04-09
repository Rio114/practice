#include<iostream>
using namespace std;
typedef long long llong;

int main(){
    llong a, b, k;
    cin >> a >> b >> k;
    llong res_a, res_b;
    if(a >= k){
        res_a = a - k;
        res_b = b;
    } else {
        res_a = 0;
        res_b = b - k + a;
        if(res_b < 0) res_b = 0;
    }
    cout << res_a << " " << res_b << endl;
}