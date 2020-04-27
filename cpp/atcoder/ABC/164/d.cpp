#include<iostream>
#include<string>
using namespace std;
static const int DIV = 2019;

int main(){
    string s;
    cin >> s;
    int len = s.size();

    int cnt = 0;
    for(int i=0; i<len-4; i++){
        for(int j=i+4; j<=len; j++){
            int order = j-i;
            int res=0;
            int order_adj = 1;
            for(int k=order; k>0; k--){
                string subs = s.substr(i+k-1, 1);
                // cout << subs << endl;
                int num = atoi(subs.c_str()) * order_adj;
                res = (res + num) % DIV;
                order_adj = (order_adj * 10) % DIV;
            }
            
            if(!(res % DIV)) {
                // cout << i << " " << j << " ";
                // string subs = s.substr(i, j-i);
                // cout << subs << endl;
                cnt++;
            }
        }
    }
    cout << cnt << endl;

}