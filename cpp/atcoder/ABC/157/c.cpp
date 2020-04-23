#include<iostream>
#include<cmath>
using namespace std;

#define NMAX 3

int main(){
    int n, m;
    int num[NMAX + 1];
    int memo[NMAX + 1];
    cin >> n >> m;

    for(int i=0; i<=n; i++){
        num[i] = 0;
        memo[i] = -1;
    }

    for(int i=0; i<m; i++){
        int s, c;
        cin >> s >> c;
        num[s] = c;
        if(memo[s] == -1) memo[s] = num[s];
        else if(memo[s] != num[s]){
            cout << -1 << endl;
            return 0;
        }

    }

    int ans=0;
    if(n != 1 && memo[1] == 0){
        cout << -1 << endl;
        return 0;
    }else if (n == 1 && memo[1] != -1){
        cout << num[1] << endl;
        return 0;       
    }else if(n == 1 && memo[1] == -1){
        cout << 0 << endl;
        return 0;       
    }

    if(memo[1] == -1) ans += pow(10, n-1);
    else ans += num[1] * pow(10, n-1);

    for(int i=2; i<=n; i++){
        ans += num[i] * pow(10, n-i);
    }

    cout << ans << endl;
   
}