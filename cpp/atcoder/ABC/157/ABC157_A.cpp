#include <bits/stdc++.h>
using namespace std;

int main (){
    int n, m;
    cin >> n;
    m = n / 2;
    if (n%2 ==1){
        m++;
    }
    cout << m << endl;
}