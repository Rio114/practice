#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)

const int N = 5;

int main(){
    string str;
    cin >> str;
    int n = str.size();

    string num_str="";
    int sum=0;

    for (int tmp = 0; tmp < (1 << n-1); tmp++) {
        bitset<N> s(tmp);
        vector<string> nums;
        num_str = "";
        sum = 0;
        
        sum += stoi(str.substr(0, 1));
        num_str += str.at(0);

        rep(i, n-1){
            if(s.test(i)){
                num_str += "+";
                sum += stoi(str.substr(i+1, 1));
                num_str += str.at(i+1);
            }else{
                num_str += "-";
                sum -= stoi(str.substr(i+1, 1));
                num_str += str.at(i+1);
            }
        }
        if (sum==7){
            break;
        }

    }
    
    if(sum==7){
        cout << num_str << "=7" << endl;
    }

}
