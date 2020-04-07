#include<iostream>
#include<map>
using namespace std;

int main(){
    int i, n, a;
    map<int, int> memo;
    cin >> n;
    for(i=0; i<n; i++) {
        cin >> a;
        memo[a] += 1;
    }
    int flg = 0;
    for(auto iter = begin(memo); iter != end(memo); ++iter){
        if(iter->second > 1){
            flg = 1;
            break;
        }
    }

    if(flg == 0) cout << "YES" << endl;
    else cout << "NO" << endl;


}
