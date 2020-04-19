#include<queue>
#include<iostream>
using namespace std;
typedef long long llong;

int main(){
    llong n;
    cin >> n;

    queue<llong> Q;
    for(llong i=1; i<=9; i++){
        Q.push(i);
    }

    llong d;
    for(int j=1; j<n; j++){
        d = Q.front(); Q.pop();
        // cout << j << " " <<  d << endl;
        llong m;

        if(d - d / 10 * 10 != 0){
            m = d * 10 + (d - d / 10 * 10) - 1;
            Q.push(m);
        }

        m = d * 10 + (d - d / 10 * 10);
        Q.push(m);

        if(d - d / 10 * 10 != 9){
            m = d * 10 + (d - d / 10 * 10) + 1;
            Q.push(m);
        }
    }
    
    d = Q.front(); Q.pop();
    cout << d << endl;
}