#include <bits/stdc++.h>
using namespace std;

#define MAX_N 1000000

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i; i<n; i++){
        char* c;
        cin >> c;
        a.at(i) = stoi(c);
    }
    
    for(int i; i<n; i++){
        cout << a.at(i);
    }
    cout << endl;
}