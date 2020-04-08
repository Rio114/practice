#include<iostream>
using namespace std;

int main(){
    int i, a, n;
    cin >> n;
    int pmin = n;
    int cnt = 0;
    for(i=0; i<n; i++){
        cin >> a;
        pmin = min(a, pmin);
        if(pmin == a) cnt++;
    }
    cout << cnt << endl;
}