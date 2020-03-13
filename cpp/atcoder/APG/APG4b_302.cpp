#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)

int main(){
    int n;
    cin >> n;
    vector<tuple<int, int>> a;
    int b, c;
    rep(i, n){

        cin >> b >> c;
        a.push_back(make_tuple(c, b));
    }
    
    sort(a.begin(), a.end());

    rep(i, n){
        tie(c, b) = a.at(i);
        cout << b << " " << c << endl;
    }


}
