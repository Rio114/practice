#include<iostream>
using namespace std;
typedef long long llong;

int main(){
    llong n, k;
    cin >> n >> k;
    llong ans = n % k;
    llong ans2 = k - ans;
    ans = min(ans, ans2);
    cout << ans << endl;
}