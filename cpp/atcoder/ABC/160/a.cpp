// #include <bits/stdc++.h>
#include<iostream>
#include<string>
using namespace std;

int main(){
    string str;
    cin >> str;
    int i;
    if (str.substr(2,1) == str.substr(3,1) 
        && str.substr(4,1) == str.substr(5,1)){
            cout << "Yes" << endl;
        }else {
            cout << "No" << endl;
        }
}