#include<iostream>
using namespace std;

static const int MAX = 100;
static const int INF = (1<<21);
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int main(){
    int i, j, n, mat[MAX][MAX];
    int state[MAX];
    int minW[MAX];
    int parent[MAX];

    cin >> n;
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            cin >> mat[i][j];
            if(mat[i][j] == -1) mat[i][j] = INF;
        }
    }

    for(i=0; i<n; i++){
        state[i] = WHITE;
        minW[i] = INF;
    }
    
    int initial = 0;
    state[initial] = GRAY;
    minW[initial] = 0;
    parent[initial] = -1;
    
    int cur;
    while(1){
        int cost = INF;
        for(i=0; i<n; i++){
            if(state[i] != BLACK && minW[i] < cost){
                cost = minW[i];
                cur = i;
            }
        }

        if(cost == INF) break;

        state[cur] = BLACK;

        for(i=0; i<n; i++){
            if(state[i] != BLACK && mat[cur][i] < minW[i]){
                minW[i] = mat[cur][i];
                parent[i] = cur;
                state[i] = GRAY; 
            }
        }

    }

    int sum=0;
    for(i=0; i<n; i++){
        sum += minW[i];
    }

    cout << sum << endl;



}