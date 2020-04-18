#include<iostream>
#include<vector>
#include<set>
using namespace std;

static const int MAX = 100000;
vector<int> G[MAX];
int N;
bool Visited[MAX];
int Prenum[MAX], Parent[MAX], Lowest[MAX], Timer;

void dfs(int curr, int prev){
    Prenum[curr] = Lowest[curr] = Timer;
    Timer++;

    Visited[curr] = true;
    int next;
    for(int i=0; i<G[curr].size(); i++){
        next = G[curr].at(i);
        if(!Visited[next]){
            Parent[next] = curr;
            dfs(next, curr);
            Lowest[curr] = min(Lowest[curr], Lowest[next]);
        }else if(next != prev){
            Lowest[curr] = min(Lowest[curr], Prenum[next]);
        }
    }
}

void art_points(){
    for(int i=0; i<N; i++){
        Visited[i] = false;
    }
    Timer = 1;
    dfs(0, -1);

    set<int> ap;
    int np = 0;
    for(int i=1; i<N; i++){
        int p = Parent[i];
        if(p == 0) np++;
        else if (Prenum[p] <= Lowest[i]) ap.insert(p);
    }
    if(np > 1) ap.insert(0);
    for(set<int>::iterator it=ap.begin(); it!=ap.end(); it++){
        cout << *it << endl;
    }
}

int main(){
    int m;
    cin >> N >> m;

    for(int i=0; i<m; i++){
        int s, t;
        cin >> s >> t;
        G[s].push_back(t);
        G[t].push_back(s);
    }

    art_points();
}