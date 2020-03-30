#include<stdio.h>

#define MAX 100

struct Node {
    int p;
    int l;
    int r;
};

Node T[MAX];
int preOrder[MAX], inOrder[MAX], postOrder[MAX];
int idx;

void reconstruction(int left, int right, int root){
    // leftTree = inOrder[:root];
    // rightTree = inOrder[root+1:];

    // leftTreeRoot;
    // rightTreeRoot;

    // T[idx] = {root, leftTreeRoot, rightTreeRoot};
    // idx++;

    // reconstruction(leftTree, leftTreeRoot);
    // reconstruction(rightTree, rightTreeRoot);

}


int main(){
    int i, n, root;
    scanf("%d", &n);
    for (i=0; i<n; i++) scanf("%d", &preOrder[i]);
    for (i=0; i<n; i++) scanf("%d", &inOrder[i]);

    idx =0;
    root = preOrder[0];

}