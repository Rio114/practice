#include<iostream>
using namespace std;

int gcd(int x, int y){
    int z = min(x, y);
    int w = max(x, y);
    while(z > 0){
        int res = w % z;
        w = z;
        z = res;
    }
    return w;
}

int main(){
    int a, b, c, g, sum=0;
    int k;
    cin >> k;
    for(a=1; a<=k; a++){
        for(b=1; b<=k; b++){
            for(c=1; c<=k; c++){
                sum += gcd(gcd(a, b), c);
            }
        }
    }
    cout << sum << endl;
}