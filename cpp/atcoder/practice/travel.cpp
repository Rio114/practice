#include <bits/stdc++.h>
using namespace std;

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
    string out;
    cin >> n;
    vector<int> t(n), x(n), y(n);
    for (int i=0; i<n; i++){
        cin >> t.at(i) >> x.at(i) >> y.at(i);
    }

    for (int i=0; i<n; i++){
        int diff_t, diff_x, diff_y, diff_d, res, div;
        if(i == 0){
            diff_t = myabs(t.at(0), 0);
            diff_x = myabs(x.at(0), 0);
            diff_y = myabs(y.at(0), 0);
        }else{
            diff_t = myabs(t.at(1), t.at(0));
            diff_x = myabs(x.at(1), x.at(0));
            diff_y = myabs(y.at(1), y.at(0));
        }
        diff_d = diff_x + diff_y;
        res = diff_t % diff_d;
        div = diff_t - diff_d;

        if (res % 2 == 0 && div >= 0){
            out = "Yes";
        }else{
            out = "No";
            break;
        }
    }
    cout << out << endl;
}
