#include<iostream>
using namespace std;
#define MAX 200

int main(){
    int N, x, y, D[MAX], i, j, d;
    cin >> N >> x >> y;
    for(i=1; i<=N; i++) D[i]=0;
    for(i=1; i<N; i++){
        for(j=i+1; j<=N; j++){
            if(i<=x && y<=j) d = j- y + x - i + 1;
            else d = j - i;
            D[d]++;
        }
    }
    for(i=1; i<=N; i++) cout << D[i] << endl;

}