#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<list>
using namespace std;

static const int MAX = 100000;
static const int INF = (1<<29);

vector<int> g[MAX];
list<int> out;
bool V[MAX];
int N;
int indeg[MAX];

void bfs(int s){
    queue<int> q;
    q.push(s);
    V[s] = true;
    while(! q.)
}