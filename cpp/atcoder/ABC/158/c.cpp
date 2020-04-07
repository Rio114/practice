#include<iostream>
using namespace std;

int main(){
    int A, B;
    cin >> A >> B;
    int paa, pab, pba, pbb;
    
    paa = A * 25 / 2.0;
    pab = (A+1) * 25 / 2.0;
    pba = B * 10;
    pbb = (B+1) * 10;

    cout << (paa-1) * 0.08 << " " << (pba-1) * 0.1 << endl;

    int ans = max(paa, pba);

    int check_a, check_b;
    check_a = ans * 0.08;
    check_b = ans * 0.10;

    if ( ans < min(pab, pbb)) cout << ans << endl;
    else cout << -1 << endl;
    
}