#include<iostream>
#include<stack>
using namespace std;

static const int N=100;
static const int WHITE=0;
static const int GRAY=1;
static const int BLACK=2;

int n, mat[N][N]
int nt[N], color[N],
int next(int u){

}


void


void dfs(){
    for(int i=0; i<n; i++){
        color[i] = WHITE;
        nt[i] = 0;
    }
}

int main(){
    int i, j, n;
    cin >> n;
    int mat[n][n];
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            mat[i][j] = 0;
        }
    }

    int idx, num, v;
    for(i=0; i<n; i++){
        cin >> idx >> num;
        for(j=0; j<num; j++){
            cin >> v;
            mat[idx-1][v-1] = 1;
        }
    }


}