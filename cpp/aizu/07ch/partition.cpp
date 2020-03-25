#include<stdio.h>
#define MAX 100000

int A[MAX], n;

int partition(int p, int r){
    int x = A[r];
    int i = p-1;
    for(int j=p; j<r; j++){
        if(A[j] <= x){
            i++;
            int t = A[j]; A[j]=A[i]; A[i]=t;
        }
    }
    int t = A[r]; A[r]=A[i+1]; A[i+1]=t;

    return i+1;
}

int main(){
    int i, q;

    scanf("%d", &n);
    for(i=0; i<n; i++) scanf("%d", &A[i]);

    q = partition(0, n-1);

    for(i=0; i<n; i++){
        if(i) printf(" ");
        if(i == q) printf("[");
        printf("%d", A[i]);
        if(i == q) printf("]");
    }
    printf("\n");
}