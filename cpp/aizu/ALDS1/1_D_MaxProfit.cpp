#include<iostream>
using namespace std;

static const int RMAX = 1000000000;

int main(){
    int n, r, rprev, rmin=RMAX, pmax=-RMAX;
    cin >> n;
    cin >> r;
    for(int i=1; i<n; i++){
        rprev = r;
        cin >> r;
        rmin = min(rmin, rprev);
        pmax = max(pmax, r - rmin);
    }

    cout << pmax << endl;
}