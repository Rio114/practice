#include<iostream>
using namespace std;
#define MAX 100000
typedef long long llong;

int n, k;
llong T[MAX];

int check(llong P){
    int i = 0;
    for(int j=0; j<k; j++){
        llong s = 0;
        while(s+T[i] <= P){
            s += T[i];
            i++;
            if(i ==n) return n;
        }
    }
    return i;
}

int solve() {
    llong left = 0;
    llong right = MAX * 10000;
    llong mid;
    while(right - left > 1){
        mid = (left + right) / 2;
        int v = check(mid);
        if( v >=n) right = mid;
        else left = mid;
    }

    return right;
}

int main(){
    cin >> n >> k;
    for(int i =0; i<n; i++) cin >> T[i];
    llong ans = solve();
    cout <<  ans << endl;
}


// #include<iostream>
// #include<queue>
// #include<stdio.h>
// using namespace std;
// #define MAX 100000
// typedef long long llong;

// int n, k, w[MAX];

// int count(int p){
//     int i, nt=1, sum=0;
//     for(i=0; i<n; i++){
//         if(sum + w[i] <= p) sum += w[i];
//         else{
//             nt++;
//             sum=w[i];
//         }
//         cout << i << " " << nt << " " << sum << endl;
//     }
//     return nt;
// }

// int main(){
//     cin >> n >> k;
//     int pmin = 0;
//     for(int i=0; i<n; i++){
//         int a;
//         cin >> a;
//         pmin = max(pmin, a);
//         w[i] = a;
//     }

//     int left = pmin, right=MAX;
//     int mid, ans;

//     while(right - left > 1){
//         mid = (left + right) / 2;
//         int v = count(mid);
//         cout << v << " " << k << " " << left << " "<< mid <<  " "<< right << endl;
//         if (v <= k) right = mid;
//         else if (v > k) left = mid;
//         cout << v << " " << k << " " << left << " "<< mid <<  " "<< right << endl;
//     }

//     if (count(left)== k) ans = left;
//     else ans = right;
    
//     int v1 = count(left);
//     int v2 = count(right);
//     cout <<  left << " " << v1 << " " << right << " " << v2 << endl;

//     cout << ans << endl;
// }

