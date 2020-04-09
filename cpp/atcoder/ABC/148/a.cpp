#include<iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    if(a * b == 2) cout << 3 << endl;
    else if(a * b == 3) cout << 2 << endl;
    else if(a * b == 6) cout << 1 << endl;
}