#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    map<int, int> b;
    vector<tuple<int, int>> c; 
    rep(i, n){
        cin >> a.at(i);
        b[a.at(i)] += 1; 
    }

    for(pair<int, int> p : b){
        int num = p.first;
        int cnt = p.second;
        c.push_back(make_tuple(cnt, num));
    }

    sort(c.begin(), c.end());
    reverse(c.begin(), c.end());

    int max_cnt, max_num;
    tie(max_cnt, max_num) = c.at(0);
    cout << max_num << " " <<  max_cnt << endl;

    
}