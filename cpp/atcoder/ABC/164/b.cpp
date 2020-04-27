#include<iostream>
using namespace std;

int main(){
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int n_t, n_a;
    n_t = c / b;
    if(c % b) n_t++;

    n_a = a / d;
    if(a % d) n_a++;

    if(n_t <= n_a) cout << "Yes" << endl;
    else cout << "No" << endl;

}