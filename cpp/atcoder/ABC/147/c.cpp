#include<iostream>
#include<bitset>
using namespace std;
#define MAX 15


int main(){
    int i, n;
    cin >> n;
    int hon=n;
    int a[n];
    int x[n][n], y[n][n];
    for(i=0; i<n; i++){
        cin >> a[i];
        for(int j=0; j<a[i]; j++){
            cin >> x[i][j] >> y[i][j];
        }
    }

    int cnt, max_cnt=0;
    for (int tmp=0; tmp<(1<<n); tmp++){
        bitset<MAX> hyp(tmp);
        cnt = 0;        
        bool flg=true;
        for(i=0; i<n; i++){
            if(hyp.test(i)){
                cnt++;
                for(int j=0; j<a[i]; j++){
                    if(hyp.test(x[i][j]) != y[i][j]) {
                        flg = false;
                    }
                }
            }
        }
        if(flg == true) max_cnt = max(max_cnt, cnt);
    }
    cout << max_cnt << endl;
}