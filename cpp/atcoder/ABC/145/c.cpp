#include<iostream>
using namespace std;
#include<cmath>

int main(){
    int i, j, n;
    cin >> n;
    int x[n], y[n];
    for(i=0; i<n; i++){
        cin >> x[i] >> y[i];
    }
    
    int d[n][n];
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            d[i][j] = pow(pow((x[i] - x[j]), 2) + pow((y[i] - y[j]), 2), 0.5); 
        }
    }

    
}
