#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)

const int N = 11;

int main(){
    string str;
    cin >> str;
    int n = str.size();

    int64_t sums_total=0;

    for (int64_t tmp = 0; tmp < (1 << n-1); tmp++) {
        bitset<N> s(tmp);
        vector<string> nums;
        int64_t sum=0;
        string num_str="";
        rep(i, n){
            if(s.test(i) || i==n-1){
                num_str += str.at(i);
                nums.push_back(num_str);
                num_str = "";
            }else {
                num_str += str.at(i);
            }
        }
        for(string num_str : nums){
            int64_t num = stol(num_str);
            sum += num;
        }
        sums_total += sum;
    }
    cout << sums_total << endl;
}
