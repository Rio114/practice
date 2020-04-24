#include<iostream>
#include<vector>
#include<queue>
using namespace std;
typedef long long llong;

static const int NMAX = 100001;
// static const int MMAX = 100000;
// static const int KMAX = 100000;
static const int NIL = -1;
// static const int WHITE = 0;
// static const int GRAY = 1;
// static const int BLACK = 2;

int N, Idx;
int Color[NMAX];
llong Cnt[NMAX], Adj[NMAX];
vector<llong> F[NMAX], B[NMAX];

void dfs(int u, int c){
    Color[u] = c;
    for(int i=0; i<F[u].size(); i++){
        if(Color[F[u].at(i)] == NIL){
            dfs(F[u].at(i), c);
        }
   }
}


// void bfs(int u, int c){
//     queue<int> Q;
//     Q.push(u);
//     Color[u] = c;
//     while(!Q.empty()){
//         u = Q.front(); Q.pop();
//         for(int i=0; i<F[u].size(); i++){
//             if(Color[F[u].at(i)] == NIL){
//                 Q.push(F[u].at(i));
//                 Color[F[u].at(i)] = c;
//             }
//         }
//     }
// }


void assign(){
    Idx=1;
    for(int i=1; i<=N; i++) Color[i] = NIL;
    for(int i=1; i<=N; i++){
        if(Color[i] == NIL){
            dfs(i, Idx);
            Idx++;
        }
    }
}

int main(){
    int m, k;
    cin >> N >> m >> k;
    for(int i=0; i<m; i++){
        int a, b;
        cin >> a >> b;
        F[a].push_back(b);
        F[b].push_back(a);
    }

    assign();
    
    for(int i=1; i<=N; i++) {
        Adj[i] = 0;
    }

    for(int i=0; i<k; i++){
        int c, d;
        cin >> c >> d;
        B[c].push_back(d);
        B[d].push_back(c);
        if(Color[c] != Color[d]){
            Adj[c] += 1;
            Adj[d] += 1;
        }
    }

    for(int i=1; i<=N; i++) Cnt[i] = 0;
    for(int i=1; i<=N; i++){
        Cnt[Color[i]]++;
    }

    for(int i=1; i<=N; i++){
        if(i != 1) cout << " ";
        llong ans = Cnt[Color[i]] - 1 - F[i].size() - B[i].size() + Adj[i];
        cout << ans;
    }
    cout << endl;

}
