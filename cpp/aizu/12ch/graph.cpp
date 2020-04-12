#include<iostream>
using namespace std;

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
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            if(j != 0) cout << " ";
            cout << mat[i][j];
        }
        cout << endl;
    }

}