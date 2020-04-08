#include<iostream>
#include<list>
using namespace std;
#define MAX 8

int fact(int n){
    int f=1;
    for (int i=0; i<n; i++){
        f *= i+1;
    }
    return f;
}

int order(int a[], int n){
    int ord = 1, i, pos;
    list<int> lis;
    for(i=0; i<n; i++) lis.push_back(i+1);
    
    for(i=0; i<n-1; i++){
        pos = 1;
        for(auto it=lis.begin(); it!=lis.end(); it++){
            // cout << *it << " ";
            if(*it == a[i]){
                // cout << "pos" << pos <<endl;
                break;
            } 
            pos++;
        }
        lis.erase(next(lis.begin(), pos-1));
        ord += (pos-1) * fact(n-i-1);
        pos = 1;
    }

    return ord;
}


int main(){
    int i, n, p[MAX], q[MAX];
    cin >> n;
    for(i=0; i<n; i++) cin >> p[i];
    for(i=0; i<n; i++) cin >> q[i];

    int a, b;
    a = order(p, n);
    b = order(q, n);
    // cout << a << endl;
    // cout << b << endl;
    cout << abs(a-b) << endl;

}

