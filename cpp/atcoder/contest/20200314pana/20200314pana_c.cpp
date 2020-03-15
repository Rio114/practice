#include<cmath>
#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    double diff = sqrtl(a) + sqrtl(b) - sqrtl(c);

    cout << diff << endl;

    if(diff < 0){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    
}


