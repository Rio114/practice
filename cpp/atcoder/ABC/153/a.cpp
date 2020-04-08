#include<iostream>
using namespace std;

int main(){
    int h, a;
    cin >> h >> a;
    int n = h / a;
    int res = h % a;
    if (res > 0) cout << n + 1 << endl;
    else cout << n << endl;
}