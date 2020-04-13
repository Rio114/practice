#include<iostream>
using namespace std;

static const int INF = (1<<21);

int main(){
    int i, j, n;
    cin >> n;
    int mat[n][n];
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            mat[i][j] = INF;
        }
    }

    int idx, num, v, w;
    for(i=0; i<n; i++){
        cin >> idx >> num;
        for(j=0; j<num; j++){
            cin >> v >> w;
            mat[idx][v] = w;
        }
    }


}