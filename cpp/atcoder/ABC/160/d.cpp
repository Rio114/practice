#include<iostream>
using namespace std;
#define MAX 2000

int main(){
    int N, x, y, D[MAX], i, j, d, d1, d2;
    cin >> N >> x >> y;
    for(i=1; i<=N; i++) D[i]=0;
    for(i=1; i<N; i++){
        for(j=i+1; j<=N; j++){
            d1 = j - i;
            d2 = abs(y-j) + abs(x-i) + 1;
            d = min(d1, d2);
            D[d]++;
        }
    }
    for(i=1; i<N; i++) cout << D[i] << endl;

}
