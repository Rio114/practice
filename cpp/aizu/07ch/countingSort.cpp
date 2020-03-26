#include<stdio.h>
#define N_MAX 2000000
#define A_MAX 10000

int A[N_MAX], B[N_MAX], C[A_MAX], n;

void countingSort(int k){
    int i;
    for (i=0; i<k+1; i++) C[i]=0;

    for (i=0; i<n; i++) C[A[i]]++;

    C[0]--;

    for (i=1; i<k+1; i++) C[i] = C[i] + C[i-1];

    for (i=n-1; i>=0; i--) {
        B[C[A[i]]] = A[i];
        C[A[i]]--;
    }
}

int main(){
    int i, a, k=0;
    scanf("%d", &n);
    for(i=0; i<n; i++){
        scanf("%d", &a);
        A[i] = a;
        if (k < a) k = a;
    } 
    
    countingSort(k);

    for(i=0; i<n-1; i++) printf("%d ", B[i]);
    printf("%d\n", B[n-1]);
}