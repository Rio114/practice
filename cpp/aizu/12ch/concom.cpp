#include<iostream>
#include<vector>
using namespace std;

static const int MAX = 100000;
static const int WHITE = -1;

int n, color[MAX];
vector<int> g[MAX];

void dfs(int u, int c){
    color[u] = c;
    for(int i=0; i<g[u].size(); i++){
        if(color[g[u].at(i)] == WHITE){
            dfs(g[u].at(i), c);
        }
   }
}

void assign(){
    int c=1;
    for(int i=0; i<n; i++) color[i] = WHITE;
    for(int i=0; i<n; i++){
        if(color[i] == WHITE){
            dfs(i, c);
            c++;
        }
    }

}

int main(){
    int m, s, t, q;
    cin >> n >> m;
    for(int i=0; i<m; i++){
        cin >> s >> t;
        g[s].push_back(t);
        g[t].push_back(s);
    }
    
    assign();
    
    cin >> q;
    for(int i=0; i<q; i++){
        cin >> s >> t;
        if(color[s] == color[t]) cout << "yes" << endl;
        else cout << "no" << endl;
    }
}