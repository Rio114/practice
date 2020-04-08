#include<iostream>
using namespace std;
#include<vector>
#include<algorithm>
typedef long long llong;

int main(){
    int n, k;
    cin >> n >> k;
    vector<int> h;
    int a;
    for(int i=0; i<n; i++){
        cin >> a;
        h.push_back(a);
    }

    if (k>=n){
        cout << 0 << endl;
        return 0;
    } 
    
    sort(h.begin(), h.end());
    reverse(h.begin(), h.end());
    llong cnt = 0;
    for(int i=k; i<n; i++){
        cnt += h.at(i);
    }
    cout << cnt << endl;
}