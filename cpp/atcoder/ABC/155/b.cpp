#include<iostream>
using namespace std;
#define MAX 100


int main(){
    int i, n, a[MAX];
    cin >> n;
    for(i=0; i<n; i++) cin >> a[i];
    int flg = 1;
    for(i=0; i<n; i++){
        if(a[i] % 2 == 0){
            if(a[i] % 3 != 0 && a[i] % 5 != 0){
                flg = 0;
                break;
            }
        }
    }

    if(flg == 0) cout << "DENIED" << endl;
    else cout << "APPROVED" << endl;
}