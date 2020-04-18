#include<iostream>
using namespace std;
typedef long long llong;

static const int MAX = 4001;

int main(){
    llong n;
    char s[MAX];
    cin >> n;
    cin >> s;

    llong cnt = 0, r = 0, g = 0, b = 0;
    int i, j, k;
    for(i=0; i<n; i++){
        if(s[i] == 'R') r++;
        else if(s[i] == 'G') g++;
        else if(s[i] == 'B') b++;
    }

    for(i=0; i<n-2; i++){
        for(j=i+1; j<n-1; j++){
            k = 2 * j - i;
            if(s[i] != s[j] && s[k] != s[j] && s[k] != s[i] && k < n) cnt++;
        }
    }

    llong ans = r*g*b - cnt;
    
    // for(i=0; i<n; i++){
    //     for(j=i+1; j<n; j++){
    //         for(k=j+1; k<n; k++){
    //             if(s[i]!=s[j] && s[j]!=s[k] && s[k]!=s[i] && j-i!=k-j) cnt++;
    //         }
    //     }
    // }

    cout << ans << endl;
}
