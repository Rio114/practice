#include<iostream>
using namespace std;
#define MAX 100

int main(){
    int n, a[MAX];
    cin >> n;
    int p1=0, p2;
    int sum1=0, sum2=0;
    for(int i=0; i<n; i++) {
        cin >> a[i];
        p1 += a[i];
    }
    p1 /= n;
    p2 = p1+1;
    for(int i=0; i<n; i++){
        sum1 += (a[i] - p1) * (a[i] - p1);
        sum2 += (a[i] - p2) * (a[i] - p2);
    }
    int ans = min(sum1, sum2);
    cout << ans << endl;
}