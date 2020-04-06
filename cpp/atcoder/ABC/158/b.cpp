#include<iostream>
using namespace std;
typedef long long llong;

int main(){
    llong N, A, B;
    cin >> N >> A >> B;
    llong res = N % (A + B);
    llong num = N / (A + B);
    llong ans;
    if(A < res) ans = A;
    else ans = res;
    ans += A * num;
    cout << ans << endl; 
}