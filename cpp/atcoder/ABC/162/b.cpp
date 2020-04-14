#include<iostream>
using namespace std;
typedef long long llong;

int main(){
    llong i, n, sum=0;
    cin >> n;
    for(i=1; i<=n; i++){
        if(i % 3 != 0 && i % 5 !=0) sum += i;
    }

    cout << sum << endl;
}