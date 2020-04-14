#include<iostream>
#include<vector>
using namespace std;

/*
int GCD(int &x, int &y){
    int gcd = 1;
    int z = min(x, y);
    int w = max(x, y);
    for(int i=z; i>=1; i--){
        int res1 =  w % i;  
        int res2 =  z % i;  
        //cout << i << " " << res1 << " " << res2 << endl;
        if (!res1 && !res2){
            gcd = i;
            break;
        }
    }

    return gcd;
}
*/

int GCD(int &x, int &y){
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
    int x, y;
    cin >> x >> y;

    int gcd = GCD(x, y);

    cout << gcd << endl;

}

