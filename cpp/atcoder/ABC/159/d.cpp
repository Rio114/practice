#include<iostream>
using namespace std;
typedef long long llong;

static const int NMAX = 200001;

int main(){
    llong n, a[NMAX], num[NMAX], sum=0;
    cin >> n;
    for(int i=1; i<=n; i++) num[i] = 0;
    
    for(int i=0; i<n; i++){
        cin >> a[i];
        num[a[i]]++;
    } 

    for(int j=1; j<=n; j++){
        sum += num[j] * (num[j] - 1) / 2;
    }

    for(int i=0; i<n; i++){
        llong ans = sum - (num[a[i]] - 1);
        cout << ans  << endl;
    }

}