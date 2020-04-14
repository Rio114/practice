#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

bool isPrime(int x){
    if(x == 2) return true;
    else if (x == 3) return true;
    int sq = sqrt(x);
    for(int i=2; i<=sq; i++){
        if(!(x % i)){
            return false;
        }
    }
    return true;
}


int main(){
    int n;
    vector<int> a;
    cin >> n;
    for(int i=0; i<n; i++){
        int b;
        cin >>  b;
        a.push_back(b);
    }

    int cnt = 0;

    for(int i=0; i<n; i++){
        int p = (int)isPrime(a.at(i));
        cnt += p;
        // cout << p;
    }
    // cout << endl;
    cout << cnt << endl;
    
}