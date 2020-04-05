#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)

int main(){
    int n;
    cin >> n;
    vector<tuple<string, int, int>> a; 
    vector<tuple<int, string, int>> b; 
    string s;
    int p;
    rep(i, n){
        cin >> s >> p;
        a.push_back(make_tuple(s, p*(-1), i));
    }
    
    sort(a.begin(), a.end());

    int num;

    rep(j, n){
        tie(s, p, num) = a.at(j);
        cout << num+1 << endl;
    }

}
