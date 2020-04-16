#include<iostream>
#include<vector>
using namespace std;

int N;
vector<int> value;

void update(int i, int x){
    i += N - 1;
    value.at(i) += x; //add
    while(i > 0){
        i = (i - 1) / 2;
        value.at(i) = value.at(i*2+1) + value.at(i*2+2);
    }
}

int getSum(int a, int b, int k, int l, int r){
    if(b <= l || r <= a) return 0;
    if(a <= l && r <= b) return value.at(k);
    else {
        int c1 = getSum(a, b, 2*k+1, l, (l+r)/2);
        int c2 = getSum(a, b, 2*k+2, (l+r)/2, r);
        return c1 + c2;
    }
}


int main(){
    int n, q;
    cin >> n >> q;
    N = 1;
    while(N < n+1) N *= 2;

    for(int i=0; i<2*N-1; i++){
        value.push_back(0);
    }

    for(int i=0; i<q; i++){
        int c;
        cin >> c;
        if(c == 0){
            int j, x;
            cin >> j >> x;
            update(j, x);
        }else{
            int s, t;
            cin >> s >> t;
            cout << getSum(s, t+1, 0, 0, N) << endl;
        }
    }
}
