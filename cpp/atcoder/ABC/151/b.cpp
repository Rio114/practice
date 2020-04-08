#include<iostream>
using namespace std;

int main(){
    int i, n, k, m;
    cin >> n >> k >> m;
    int sum = 0, s;
    for(i=0; i<n-1; i++){
        cin >> s;
        sum += s;
    }
    int tgt = n * m - sum;
    if (tgt > k) cout << -1 << endl;
    else if (tgt < 0) cout << 0 << endl;
    else cout << tgt << endl;

}