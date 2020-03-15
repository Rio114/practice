#include<stdio.h>
#include<vector>
#include<iostream>
using namespace std;

int search(vector<int> a, int n, int key){
    int left = 0; 
    int right = n; 

    while(left < right){
        int mid = (left + right ) /2;
        if(a.at(mid) == key){
            return mid;
        }else if (key < a.at(mid)){
            right = mid;
        }else{
            left = mid + 1;
        }
    }
    return 0;
}

int main(){
    int n, i, q, key, cnt = 0;
    cin >> n;
    vector<int> a;
    for(int i=0; i<n; i++){
        int b;
        std::cin >> b;
        a.push_back(b);
    }

    cin >> q;
    
    for(int i=0; i<q; i++){
        cin >> key;
        if( search(a, n, key) ) cnt++;
    }
    
    cout << cnt << endl;    
}
