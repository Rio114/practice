#include<iostream>
using namespace std;

int main(){
    int i, n;
    char c[100];
    cin >> n >> c;

    if(n % 2 != 0){
        cout << "No" << endl;
        return 0;
    }

    for(i=0; i<n/2; i++){
        if(c[i] != c[n/2 + i]){
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;
    return 0;
}