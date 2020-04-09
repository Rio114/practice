#include<iostream>
using namespace std;
#define MAX 100

int main(){
    int i, n;
    cin >> n;
    char s[MAX], t[MAX], u[MAX*2];
    for(i=0; i<n; i++) cin >> s[i];
    for(i=0; i<n; i++) cin >> t[i];

    for(i=0; i<n; i++) cout << s[i] << t[i];
    cout << endl;
}