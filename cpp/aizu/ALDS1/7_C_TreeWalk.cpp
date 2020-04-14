#include<iostream>
using namespace std;

#define NIL -1
#define MAX 25

struct Node{
    int p;
    int l;
    int r;
};

Node T[MAX];

void preWalk(int u){
    if(u == NIL) return;
    cout << " " << u;
    preWalk(T[u].l);
    preWalk(T[u].r);
}

void inWalk(int u){
    if(u == NIL) return;
    inWalk(T[u].l);
    cout << " " << u;
    inWalk(T[u].r);
}

void postWalk(int u){
    if(u == NIL) return;
    postWalk(T[u].l);
    postWalk(T[u].r);
    cout << " " << u;
}

int main(){
    int n, i, r;
    cin >> n;
    for(i=0; i<n; i++) T[i].p = NIL;
    for(i=0; i<n; i++){
        int v, l, r;
        cin >> v >> l >> r;
        T[v].l = l;
        T[v].r = r;
        if(l != NIL) T[l].p = v;
        if(r != NIL) T[r].p = v;
    }
    for(i=0; i<n; i++){
        if(T[i].p == NIL) r = i;  
    }

    cout << "Preorder" << endl;
    preWalk(r);
    cout << endl;
    cout << "Inorder" << endl;
    inWalk(r);
    cout << endl;
    cout << "Postorder" << endl;
    postWalk(r);
    cout << endl;

}
