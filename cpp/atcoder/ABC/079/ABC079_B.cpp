#include <bits/stdc++.h>
using namespace std;

const int N_max=100;

uint64_t luca(int &n){
    vector<uint64_t> l(N_max+1);
    l.at(0) = 2;
    l.at(1) = 1;
    if (n > 1){
        for(int i=2; i<n+1; i++) {
            l.at(i) = l.at(i-1) + l.at(i-2);
        }
    }
    return l.at(n);
}
    

int main(){
    int n;
    cin >> n;
    uint64_t ans = luca(n);

    cout << ans << endl;

}