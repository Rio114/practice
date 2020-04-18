#include<iostream>
using namespace std;

static const int MAX = 4000;

int main(){
    int n;
    char s[MAX];
    // scanf("%d", &n);
    // scanf("%s", s);

    cin >> n;
    cin >> s;

    int cnt = 0;
    int i, j, k;
    for(i=0; i<n; i++){
        for(j=i+1; j<n; j++){
            for(k=j+1; k<n; k++){
                if(s[i]!=s[j] && s[j]!=s[k] && s[k]!=s[i] && j-i!=k-j) cnt++;
            }
        }
    }

    // printf("%d\n", cnt);
    cout << cnt << endl;
}
