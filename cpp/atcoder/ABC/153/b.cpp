#include<iostream>
using namespace std;

int main(){
    int i, h, n;
    int a, sum=0;
    cin >> h >> n;
    for (i=0; i<n; i++){
        cin >> a;
        sum +=a;
    }
    if(h <= sum) cout << "Yes" << endl;
    else cout << "No" << endl;
}