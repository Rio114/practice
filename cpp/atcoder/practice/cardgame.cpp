#include <bits/stdc++.h>
using namespace std;

const int N_max=100;

int* sort(int arr[N_max], int num){
    int former, later;
    for (int i=0; i<num-1; i++){
        for (int j=0; j<num-1; j++){
            former = arr[j];
            later = arr[j+1];
            if(former < later){
                arr[j] = later;
                arr[j+1] = former;
            }
        }
    }
    return arr;
}

int main(){
    int n, arr[N_max], buf;
    int alice=0, bob=0;
    int* sorted_arr;
    int diff;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> buf;
        arr[i] = buf;
    }

    sorted_arr = sort(arr, n);

    for (int j=0; j<n; j++){
        if (j % 2 == 0){
            alice += arr[j];
        }else{
            bob += arr[j];
        }
    }

    diff = alice - bob;
    cout << diff << endl;
}