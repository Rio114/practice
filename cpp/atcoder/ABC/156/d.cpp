#include<iostream>
#include<cmath>
using namespace std;
typedef long long llong;

llong


int main() {
    int n, a, b;
    cin >> n >> a >> b;
    llong cnt = 0;


    for(int i=1; i<=n; i++){
        if(i != a && i != b){
            cnt += pow(2, i);
        }
    }

    cout << cnt << endl;
}