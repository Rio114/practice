
#include <bits/stdc++.h>
#include <string>
#include <stdio.h>
using namespace std;

int digit_sum(int n){
    string n_str = to_string(n);
    int len = (int)(n_str.length());
    int sum=0;
    for (int i=0; i<len; i++){
        string digit_str = n_str.substr(i, 1);
        int digit = stoi(digit_str);
        sum += digit;
    }
    return sum;
}

int main(){
    int n, a, b;
    cin >> n >> a >> b;
    string str = to_string(n);
    int len = (int)(str.length());
    int sum=0;
    for (int i=1; i<n+1; i++){
        int di_sum = digit_sum(i);
        if (di_sum >= a && di_sum <= b){
            sum += i;
        }
    }
    cout << sum << endl;
}