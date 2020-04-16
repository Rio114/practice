#include<iostream>
#include<queue>
using namespace std;
typedef long long llong;

static const int INF = (1<<30);
static const int VMAX = 100000;
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int N, M, S; 
vector<pair<int, int> > adj[VMAX];

void dijkstra(int initial){
    priority_queue<pair<int, int> > PQ;
    int state[VMAX];
    int minW[VMAX];

    for(int i=0; i<N; i++){
        state[i] = WHITE;
        minW[i] = INF;
    }
    
    PQ.push(make_pair(0, initial));
    state[initial] = GRAY;
    minW[initial] = 0;
    
    int cur;
    while(!PQ.empty()){
        pair<int, int> f = PQ.top(); PQ.pop();
        int cur = f.second;
        state[cur] = BLACK;
        if(minW[cur] < f.first * (-1)) continue;

        for(int j=0; j<adj[cur].size(); j++){
            int v = adj[cur].at(j).first;
            if(state[v] == BLACK) continue;
            if(minW[v] > minW[cur] + adj[cur].at(j).second) {
                minW[v] = minW[cur] + adj[cur].at(j).second;
            }
            PQ.push(make_pair(minW[v]*(-1), v));
            state[v] = GRAY;
        }
    }

    for(int i=0; i<N; i++){
        if(minW[i] == INF){
            cout << "INF" << endl;
        }else{
            cout << minW[i] << endl;
        }
    }
}

int main(){
    // cout << (1<<21) << endl;
    // cout << (1<<25) << endl;
    // int t = (1<<30);
    // cout << t << endl;

    cin >> N >> M >> S;

    int src, tgt, w;
    for(int i=0; i<M; i++){
        cin >> src >> tgt >> w;
        adj[src].push_back(make_pair(tgt, w));
    }

    dijkstra(S);

}