#include<iostream>
#include<stack>
using namespace std;

static const int N=100;
static const int WHITE=0;
static const int GRAY=1;
static const int BLACK=2;

int n, mat[N][N];
int d[N], f[N], color[N];
int t;

void dfs_init(){
    for(int i=0; i<n; i++) color[i] = WHITE;
    t = 0;
}

void dfs(int u){
    color[u] = GRAY;
    t++;
    d[u] += t;
    for(int i=0; i<n; i++){
        if(mat[u][i] == 1 && color[i] == WHITE){
            dfs(i);
        }
   }
   t++;
   f[u] += t;
   color[u] = BLACK;
}

int main(){
    // int n=0, t=1;
    // cout << n << " " << t << endl;
    // n = t++;
    // cout << n << " " << t << endl;

    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            mat[i][j] = 0;
        }
    }

    int idx, num, v;
    for(int i=0; i<n; i++){
        cin >> idx >> num;
        for(int j=0; j<num; j++){
            cin >> v;
            mat[idx-1][v-1] = 1;
        }
    }

    dfs_init();

    for(int i=0; i<n; i++) {
        if(color[i] == WHITE) dfs(i);
    }

    for(int i=0; i<n; i++){
        cout << i+1 << " " << d[i] << " " << f[i] << endl;
    }

}