#include<iostream>
using namespace std;
typedef long long llong;

int main(){
    llong a, b;
    cin >> a >> b;
    llong x = max(a, b);
    llong y = min(a, b);
    llong z;
    while(x % y){
        z = x % y;
        x = y;
        y = z;
    }
    cout << a / y * b << endl;
}