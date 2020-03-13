#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, y;
    cin >> n >> y;
    int flg = 0;
    int cnt_10, cnt_5, cnt_1;
    for(int i=0; i<n+1; i++){
        int y_10 = y - 10000*i;
        if (y_10 < 0){
            continue;
        }
        for(int j=0; j<n-i+1; j++){
            int y_5 = y_10 - 5000*j;
            if(y_5 < 0){
                continue;
            }
            int k = n - i - j;
            int y_1 = y_5 - 1000*k;
            if (y_1 == 0){
                flg = 1;
                cnt_10 = i;
                cnt_5 = j;
                cnt_1 = k;
                break;
            } 
        }
        if (flg==1){
            break;
        }
    }

    if(flg == 1){
        cout << cnt_10 << " " << cnt_5 << " " << cnt_1 << endl;
    }else{
        cout << -1 << " " << -1 << " " << -1 << endl;
    }
}