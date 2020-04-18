#include<iostream>
#include<algorithm>
using namespace std;

typedef long long llong;
static const llong INF = (1LL << 31);

int main(){
    // cout << INF << endl;
    int N, M;
    cin >> N >> M;

    llong mat[N][N];
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            mat[i][j] = ( (i==j) ? 0 : INF);
            // if(i == j) mat[i][j] = 0;
            // else mat[i][j] = INF;
        }
    }

    for(int j=0; j<M; j++){
        int s, t, w;
        cin >> s >> t >> w;
        mat[s][t] = w;
    }

    for(int k=0; k<N; k++){
        for(int i=0; i<N; i++){
            if(mat[i][k] == INF) continue;
            for(int j=0; j<N; j++){
                if(mat[k][j] == INF) continue;
                mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j]);
            }
        }
    }

    for(int i=0; i<N; i++){
        if(mat[i][i] < 0) {
            cout << "NEGATIVE CYCLE" << endl;
            return 0;
        }
    }

    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(j != 0) cout << " ";
            if(mat[i][j] == INF) cout << "INF";
            else cout << mat[i][j];
        }
        cout << endl;
    }


}