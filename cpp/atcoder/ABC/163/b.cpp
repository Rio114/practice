#include<iostream>
using namespace std;

static const int MAX = 10000;

int main(){
    int n, m, a;
    int asum = 0;
    cin >> n >> m;
    for(int i=0; i<m; i++){
        cin >> a;
        asum += a;
    }
    if(asum > n) cout << -1 << endl;
    else cout << n - asum << endl;
}