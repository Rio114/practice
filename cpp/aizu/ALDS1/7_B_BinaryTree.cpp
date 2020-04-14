#include<iostream>
// #include<algorithm>
using namespace std;
#define MAX 25
#define NIL -1

struct Node{int p;
            int l;
            int r;
            };

Node T[MAX];
int D[MAX], H[MAX], S[MAX], n;

void printNode(int u){
    cout << "node " << u << ": ";
    cout << "parent = " << T[u].p << ", ";
    cout << "sibling = " << S[u] << ", ";
    
    cout << "degree = ";
    int deg = 0;
    if (T[u].l != NIL) deg++;
    if (T[u].r != NIL) deg++;
    cout << deg << ", ";
    
    cout << "depth = " << D[u] << ", ";
    cout << "height = " <<  H[u] << ", ";
    
    if (T[u].p == NIL) cout << "root" << endl;
    else if(H[u] == 0) cout << "leaf" << endl; 
    else cout << "internal node" << endl; 
}

void setDepth(int u, int d){
    if(u == NIL) return;
    D[u] = d; 
    setDepth(T[u].l, d+1);
    setDepth(T[u].r, d+1);
}

void setParent(){
    for(int u = 0; u < n; u++){        
        T[T[u].l].p = u;
        T[T[u].r].p = u;
    }
}

void setSibling(){
    for(int u = 0; u < n; u++){        
        if(T[u].p == NIL) S[u] = NIL;
        else if(T[T[u].p].l != u && T[T[u].p].l != NIL) S[u] = T[T[u].p].l;
        else if(T[T[u].p].r != u && T[T[u].p].r != NIL) S[u] = T[T[u].p].r;
    }

}

int setHight(int u){
    int h1 = 0, h2 = 0;
    if(T[u].l != NIL){
        if(H[T[u].l] == NIL) h1 = setHight(T[u].l) + 1;
        else h1 = H[T[u].l];
    }
    if(T[u].r != NIL)
        if(H[T[u].r] == NIL) h2 = setHight(T[u].r) + 1;
        else h2 = H[T[u].r];
    H[u] = max(h1, h2);
    return H[u];
}

int getRoot(){
    for(int i = 0; i < n; i++){
        if(T[i].p == NIL) return i;
    }
    return NIL;
}

int main(){
    int i;
    cin >> n;
    for(i = 0; i < n; i++) T[i].p =T[i].l = T[i].r = D[i] = H[i] = S[i] = NIL;
    for(i = 0; i < n; i++) {
        int m;
        cin >> m;
        cin >> T[m].l >> T[m].r;
    }
    setParent();
    int r = getRoot();
    // cout << "setting hight..." << endl;
    setHight(r);
    // cout << "setting depth..." << endl;
    setDepth(r, 0);
    // cout << "setting sibling..." << endl;
    setSibling();

    for(i = 0; i < n; i++) printNode(i);
}
