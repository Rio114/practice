#include<iostream>
using namespace std;
#include<string>

#define MAX 50

int main(){
    int i, n;
    char c[MAX];
    cin >> n >> c;
    i = 0;
    int cnt = 0;
    for(i=0; i<n-2; i++){
        if(c[i] == 'A' && c[i+1] == 'B' && c[i+2] == 'C'){
            cnt++;
        }
    }
    cout << cnt << endl;
}