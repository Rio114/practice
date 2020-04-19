#include<iostream>
#include<bitset>
#include<vector>
using namespace std;
typedef long long llong;

#define NMAX 200001

int main(){
    int n, k;
    cin >> n >> k;
    vector<pair<int, int> > pairs;

    for (llong tmp=0; tmp<(1LL<<(n+1)); tmp++) {
        bitset<NMAX> s(tmp);
        int bsum = 0;
        int nsum = 0;
        for(int i=0; i<=n; i++){
            bsum += s.test(i);
            nsum += s.test(i) * i;
        }
        if(bsum >= k) {
            int flg = 1; 
            for(int j=0; j<pairs.size(); j++){
                if(pairs.at(j).first == bsum && pairs.at(j).second == nsum){
                    flg = 0;
                    break;
                }
            }
            if(flg == 1){
                pairs.push_back(make_pair(bsum, nsum));    
            }
        }
        // cout << bsum << " " << nsum << " " << pairs.size() << endl;
    }

    cout << pairs.size() << endl;

}