#include<iostream>
#include<queue>
using namespace std;

static const int N=100;
static const int WHITE=0;
static const int GRAY=1;
static const int BLACK=2;

int n, mat[N][N];
int dist[N], color[N];
queue<int> Q;

void bfs_init(){
    for(int i=0; i<n; i++) color[i] = WHITE;
}

void bfs(int u){
    Q.push(u);
    color[u] = GRAY;
    dist[u] = 0;
    while(!Q.empty()){
        Q.pop();
        u = Q.front();
        cout << u << endl;
        for(int i=0; i<n; i++){
            if(mat[u][i] == 1 && color[i] == WHITE){
                Q.push(u);
                color[u] = GRAY;
                dist[i] = dist[u] + 1;
            }
        }
        color[u] = BLACK;
    }
}

int main(){
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

    bfs_init();
    bfs(0);

    for(int i=0; i<n; i++){
        cout << i+1 << " " << dist[i] << endl;
    }

}