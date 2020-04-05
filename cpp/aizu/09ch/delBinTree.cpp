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

Node *find(Node *x, int k){
    if (x->key == k) return x;
    else if (x->key > k && x->left != NIL) find(x->left, k);
    else if (x->key < k && x->right != NIL) find(x->right, k);
    else return NIL;
}

Node *treeMinimum(Node *x){
    while(x->left != NIL) x = x->left;
    return x;
}

Node *treeSuccessor(Node *x){
    if(x->right != NIL) return treeMinimum(x->right);
    Node *y = x->parent;
    while(y != NIL && x == y->right){
        x = y;
        y = y->right;
    }
}

void treeDelete(Node *z){
    Node *x, *y;
    if(z->left ==NIL || z->right == NIL) y=z;
    else y = treeSuccessor(z);

    if(y->left != NIL){
        x = y->left;
    } else {
        x = y->right;
    }

    if(x != NIL){
        x->parent = y->parent;
    }

    if(y->parent == NIL){
        root = x;
    } else {
        if(y == y->parent->left){
            y->parent->left = x;
        } else{
            y->parent->right = x;
        }
    }

    if(y != z){
        z->key = y->key;
    }

    free(y);
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
            Node *u;
            scanf("%d", &x);
            u = find(root, x);
            if (u != NIL) cout << "yes" << endl;
            else cout << "no" << endl;
        } else if (com == "delete"){
            scanf("%d", &x);
            treeDelete(find(root, x));
        }
    }
}
