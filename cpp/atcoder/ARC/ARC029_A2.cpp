#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)

vector<tuple<int, int>> sums(vector<int> &a, int n){
    vector<tuple<int, int>> sums_temp;
    if (n == 0){
        sums_temp.push_back(make_tuple(0, 0));
        sums_temp.push_back(make_tuple(0, 0));
        return sums_temp;
    }

    vector<tuple<int, int>> sums_old = sums(a, n-1);

    for (tuple<int, int> tup : sums_old){
        int sum_a, sum_b;
        tie(sum_a, sum_b) = tup;
        sums_temp.push_back(make_tuple(sum_a+a.at(n-1), sum_b));
        sums_temp.push_back(make_tuple(sum_a, sum_b+a.at(n-1)));
    }
    return sums_temp;
}

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

    vector<tuple<int, int>> time_pairs = sums(t, n);

    for (tuple<int, int> tup : time_pairs){
        int sum_a, sum_b;
        tie(sum_a, sum_b) = tup;
        int diff = myabs(sum_a, sum_b);
        if (diff_min >= diff){
            diff_min = diff;
            sum = max(sum_a, sum_b);
        }

    }

    cout << sum << endl;
}