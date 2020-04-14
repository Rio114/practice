#include<string>
#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

struct Node{
    int key;
    Node *parent, *left, *right;
};

Node *root, *NIL;

void insert(int k){
    Node *y = NIL;
    Node *x = root;
    Node *z;

    z = (Node *)malloc(sizeof(Node));
    z->key = k;
    z->left = NIL;
    z->right = NIL;

    while(x != NIL){
        y = x;
        if(z->key < x->key){
            x = x->left;
        } else {
            x = x->right;
        }
    }
    z->parent = y;
    if( y == NIL){
        root = z;
    } else {
        if(z->key < y->key){
            y->left = z;
        } else {
            y->right = z;
        }
    }
}

void find(Node *x, int k){
    if (x->key == k) cout << "yes" << endl;
    else if (x->key > k && x->left != NIL) find(x->left, k);
    else if (x->key < k && x->right != NIL) find(x->right, k);
    else cout << "no" << endl;
}

void inorder(Node *u){
    if(u == NIL) return;
    inorder(u->left);
    printf(" %d", u->key);
    inorder(u->right);
}

void preorder(Node *u){
    if(u == NIL) return;
    printf(" %d", u->key);
    preorder(u->left);
    preorder(u->right);
}

int main(){
    int n, i, x;
    string com;
    scanf("%d", &n);
    for(i=0; i<n; i++){
        cin >> com;
        if(com == "insert"){
            scanf("%d", &x);
            insert(x);
        } else if (com == "print"){
            inorder(root);
            printf("\n");
            preorder(root);
            printf("\n");
        } else if (com == "find"){
            scanf("%d", &x);
            find(root, x);
        }
    }
}
