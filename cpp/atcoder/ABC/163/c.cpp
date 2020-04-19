#include<iostream>
using namespace std;

static const int MAX = 200001;

int main(){
    int n, a[MAX];
    cin >> n;
    for(int i=1; i<=n; i++){
        a[i] = 0;
    }

    for(int i=2; i<=n; i++){
        int b;
        cin >> b;
        a[b]++;
    }

    for(int i=1; i<=n; i++){
        cout << a[i] << endl;
    }

}