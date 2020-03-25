#include<stdio.h>
#define MAX 100000
#define SENTINEL 2000000000

struct Card{
    char suit;
    int value;
};

struct Card L[MAX / 2 + 2], R[MAX / 2 + 2];

void merge(struct Card a[], int left, int mid, int right){
    int n1 = mid - left;
    int n2 = right - mid;
    for (int i=0; i<n1; i++) L[i] = a[left + i];
    for (int i=0; i<n2; i++) R[i] = a[mid + i];
    L[n1].value = R[n2].value = SENTINEL;
    int i=0, j=0;
    for(int k=left; k<right; k++){
        if(L[i].value <= R[j].value){
            a[k] = L[i++];
        }else{
            a[k] = R[j++];
        }
    }
}

void mergeSort(struct Card A[], int n, int left, int right){
    if(left + 1 < right){
        int mid = (left + right) / 2;
        mergeSort(A, n, left, mid);
        mergeSort(A, n, mid, right);
        merge(A, left, mid, right);
    }
}

int partition(struct Card A[], int n, int q, int r){
    
}