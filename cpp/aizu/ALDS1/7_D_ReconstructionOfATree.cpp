#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

int pos, n;
vector<int> preOrder, inOrder, postOrder;

void rec(int l, int r){
    if(l >=r ) return;
    int root = preOrder.at(pos);
    pos++;
    int m = distance(inOrder.begin(), find(inOrder.begin(), inOrder.end(), root));
    // cout << root << " " << l << " " << m << " " << r << endl;
    rec(l, m);
    rec(m+1, r);
    postOrder.push_back(root);
}

void solve(){
    pos = 0;
    rec(0, preOrder.size());
    for(int i = 0; i<n; i++){
        if(i) cout << " ";
        cout << postOrder.at(i);
    }
    cout << endl;
}

int main(){
    int i, t;
    cin >> n;
    for (i=0; i<n; i++){
        cin >> t;
        preOrder.push_back(t);
    } 
    for (i=0; i<n; i++){
        cin >> t;
        inOrder.push_back(t);
    } 
    solve();
}