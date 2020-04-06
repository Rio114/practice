#include<iostream>
using namespace std;

#define MAX 200000

int main(){
    int i, K, N, A[MAX], D[MAX];
    cin >> K >> N;
    for(i=0; i<N; i++) cin >> A[i];
    for(i=0; i<N; i++) {
        if(i < N-1) D[i] = A[i+1] - A[i];
        else D[i] = (K - A[i]) + A[0];
    }
    int maxDist = 0;
    for(i=0; i<N; i++) maxDist = max(maxDist, D[i]);

    cout << K - maxDist << endl;

}