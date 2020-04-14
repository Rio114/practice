#include<iostream>
using namespace std;

#define MAX 500000
#define SENTINEL 2000000000
typedef long long llong;

int L[MAX/2+2], R[MAX/2+2];
int cnt;
llong inv;

void merge(int a[], int left, int mid, int right){
    int n1 = mid - left;
    int n2 = right - mid;
    for (int i=0; i<n1; i++) L[i] = a[left + i];
    for (int i=0; i<n2; i++) R[i] = a[mid + i];
    L[n1]=R[n2]=SENTINEL;
    int i=0, j=0;
    for(int k=left; k<right; k++){
        cnt++;
        if(L[i] <= R[j]){
            a[k] = L[i];
            i++;
        }else{
            a[k] = R[j];
            inv += n1 - i;
            j++;
        }
    }
}

void mergeSort(int A[], int n, int left, int right){
    if(left + 1 < right){
        int mid = (left + right) / 2;
        mergeSort(A, n, left, mid);
        mergeSort(A, n, mid, right);
        merge(A, left, mid, right);
    }
}

int main(){
    int A[MAX], n, i;
    cnt = 0;
    inv = 0;
    cin >> n;
    for (i=0; i<n; i++) cin >> A[i];
    
    mergeSort(A, n, 0, n);

    // for(i=0; i<n; i++){
    //     if(i) cout << " ";
    //     cout << A[i];
    // }

    // cout << endl;

    // cout << cnt << endl;
    cout << inv << endl;
}