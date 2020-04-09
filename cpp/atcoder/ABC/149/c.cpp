#include<iostream>
#include<cmath>
#include<list>
using namespace std;

#define MAX 1000

bool isPrime(int n){
    int i, r, res;
    if(n==1) return false;
    else if(n==2) return true;
    r = sqrt(n);
    bool flg;
    for(i=3; i<n; i+=2){
        res = n % i;
        if(res == 0) return false;
    }
    return true;

}

int main(){
    int i, n;
    cin >> n;
    bool p = isPrime(n);
    while(!p){
        n++;
        p = isPrime(n);
    }
    cout << n << endl;
}