#include <bits/stdc++.h>
using namespace std;


int main(){
    int h, w;
    cin >> h >> w;
    int n_h, n_w;
    int64_t num;
    int64_t res_h = h % 2;
    if(h==1 || w==1){
        num = 0;
    }else if(res_h == 1){
        n_h = h / 2 + 1;
        int64_t res_w = w % 2;
        n_w = w / 2;
            num = (n_h + n_h - 1) * n_w;
        if (res_w == 1){
            num += n_h;
        }
    }else{
        n_h = h / 2;
        num = n_h * w;
    }
    cout << num << endl;
}