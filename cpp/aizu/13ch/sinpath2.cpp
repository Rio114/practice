#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;

static const int INF = (1<<20);
static const int MAX = 10000;
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int n, i, j;
vector<pair<int, int> > adj[MAX];

void dijkstra(){
    priority_queue<pair<int, int> > PQ;
    int state[MAX];
    int minW[MAX];

    for(i=0; i<n; i++){
        state[i] = WHITE;
        minW[i] = INF;
    }
    
    int initial = 0;
    PQ.push(make_pair(0, initial));
    state[initial] = GRAY;
    minW[initial] = 0;
    
    int cur;
    while(!PQ.empty()){
        pair<int, int> f = PQ.top(); PQ.pop();
        int cur = f.second;
        state[cur] = BLACK;
        if(minW[cur] < f.first * (-1)) continue;

        for(j=0; j<adj[cur].size(); j++){
            int v = adj[cur].at(j).first;
            if(state[v] == BLACK) continue;
            if(minW[v] > minW[cur] + adj[cur].at(j).second) {
                minW[v] = minW[cur] + adj[cur].at(j).second;
            }
            PQ.push(make_pair(minW[v]*(-1), v));
            state[v] = GRAY;
        }

    }

    for(i=0; i<n; i++){
        cout << i << " " << (minW[i] == INF ? -1 : minW[i] ) << endl;
    }

}


int main(){
    cin >> n;
    int idx, num, v, w;
    for(i=0; i<n; i++){
        cin >> idx >> num;
        for(j=0; j<num; j++){
            cin >> v >> w;
            adj[idx].push_back(make_pair(v, w));
        }
    }

    dijkstra();
}