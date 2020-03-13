#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)

const int N = 4;

int myabs(int a, int b){
    int diff;
    if (a > b){
        diff = a - b;
    }else{
        diff = b - a;
    }
    return diff;
}

int main(){
    int n;
    cin >> n;
    vector<int> t(n);

    int time=0;
    rep(i,n){
        cin >> t.at(i);
        time += t.at(i);
    }

    int diff_min = time;
    int sum = time;
    for (int tmp = 0; tmp < (1 <<N); tmp++) {
        bitset<N> s(tmp);  // 最大20個なので20ビットのビット列として扱う
 
        int sum_a = 0;
        int sum_b = 0;
        rep(i, n) {
            if (s.test(i)) {
                sum_a += t.at(i);
            }else{
                sum_b += t.at(i);
            }
        }
        int diff = myabs(sum_a, sum_b);
        if (diff_min >= diff){
            diff_min = diff;
            sum = max(sum_a, sum_b);
        }

    }

    cout << sum << endl;
}