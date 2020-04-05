#include<iostream>
using namespace std;
#define MAX 500000

int parent(int i) {return i/2;}
int left(int i) {return 2*i;}
int right(int i) {return 2*i+1;}

int A[MAX+1], H;

void maxHeapify(int i){
    int largest;
    int l = left(i);
    int r = right(i);
    if(l <= H && A[l] > A[i]) largest = l;
    else largest = i;

    if(r <= H && A[r] > A[largest]) largest = r;

    if(largest != i){
        swap(A[i], A[largest]);
        maxHeapify(largest);
    }
}

void buildMaxHeap(){
    int i;
    for(i=H/2; i>0; i--) maxHeapify(i);
}

int main(){
    int i;
    cin >> H;
    for(i=1; i<=H; i++) cin >> A[i];
    buildMaxHeap();
    for(i=1; i<=H; i++) cout << " " << A[i];
    cout << endl;
    

}