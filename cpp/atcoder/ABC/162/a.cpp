#include<iostream>
using namespace std;

int main(){
    char n[3];
    cin >> n;
    if(n[0]=='7' || n[1]=='7' || n[2]=='7' ){
        cout << "Yes" << endl;
    }else cout << "No" << endl;
}