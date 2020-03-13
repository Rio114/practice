#include <bits/stdc++.h>
#include <vector>
using namespace std;

int myabs(int a, int b){
    int diff;
    if (a > b){
        diff = a - b;
    }else{
        diff = b - a;
    }
    return diff;
}

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> diff(n);

    int sum = 0;
    for (int i=0; i<n; i++){
        cin >> a.at(i);
        sum += a.at(i);
    }
    int mean = sum / n;
    for (int i=0; i<n; i++){
        diff.at(i) = myabs(a.at(i), mean);
        cout << diff.at(i) << endl;
    }
}