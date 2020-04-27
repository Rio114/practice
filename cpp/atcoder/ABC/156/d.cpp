#include<iostream>
#include<cmath>
#include<vector>
using namespace std;
typedef long long llong;
static const int DIV = 1000000007;
vector<int> C;

const int MAX = 510000;
const int MOD = 1000000007;

long long fac[MAX], finv[MAX], inv[MAX];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}


int gcd(int a, int b){
    if (b == 0) return a;
    else return gcd(b, a % b);
}

int modinv(int a, int m) {
    int b = m, u = 1, v = 0;
    while (b) {
        int t = a / b;
        a -= t * b; swap(a, b);
        u -= t * v; swap(u, v);
    }
    u %= m; 
    if (u < 0) u += m;
    return u;
}

int binpow(int x, int e) {
  //----  宣言と初期化
  int a = 1;        // 結果変数の初期化
  int p = x;          // 二乗値の初期化

  //----  反復処理
  while ( e > 0 ) {      // 不定反復
    if ( e%2 == 0 ) {    // 指数が偶数のとき
      p *= p; e /= 2;    // 二乗値の更新
    } else {             // 指数が奇数のとき
      a *= p; e--;       // 二乗値の乗算
    }
  }
  //----  結果返却
  return a;
}


int extGCD(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int d = extGCD(b, a%b, y, x);
    y -= a/b * x;
    return d;
}

void comb(int n){
    C.push_back(1);
    int k = n / 2;
    int c_i;
    for(int i=1; i<=k+1; i++){
        c_i = C.at(i-1) * (n-i+1) * modinv(DIV, i);
        C.push_back(c_i);
    }
}

int biPow(int a, int n){
    int k = 1;
    int b = a;
    while( k * 2 < n ){
        b *= b % DIV;
        k *= 2;
    }

    for(int i=0; i<n-k; i++) b *= a % DIV;

    return b % DIV;
}

int main() {
    int n, a, b;
    cin >> n;
    cin >> a >> b;

    cout << biPow(a, n) << endl;

    // cout << modinv(n, a) << endl;

    // comb(n);

    // for (int i=0; i<=n; i++){
    //     int out;
    //     if(i < n/2) out = C.at(i);
    //     else out = C.at(n-i);
    //     cout << n << " " << i << " " << out << endl;
    // }

    // int cnt=0;
    // for(int i=1; i<=n; i++){
    //     if(i != a && i != b){
    //         int out;
    //         if(i < n/2) out = C.at(i);
    //         else out = C.at(n-i);
    //         cnt += out;
    //     }
    // }
    // cnt %= DIV;
    // cout << cnt << endl;
}