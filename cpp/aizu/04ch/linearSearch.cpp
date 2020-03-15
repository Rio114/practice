#include<stdio.h>
#include<vector>
#include<iostream>
using namespace std;

int search(vector<int> a, int n, int key){
    int i = 0;
    a.push_back(key);
    while(a[i] != key){
        i++;
    }
    return i != n;
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
