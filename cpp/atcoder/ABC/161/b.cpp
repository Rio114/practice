#include<iostream>
using namespace std;

#define MAX 100

int main(){
    int i, N, M, a, A[MAX];
    int cnt=0;
    int total=0;
    cin >> N >> M;
    for(i=0; i<N; i++){
        cin >> A[i];
        total += A[i];
    }
    float thres = total / 4.0 / M;

    for(i=0; i<N; i++){
        if(A[i] >= thres) cnt++;
    }

    if(cnt >= M) cout << "Yes" << endl;
    else cout << "No" << endl;

}