#include<iostream>
#include<string>
using namespace std;

int main(){
    string str;
    int i, n=3, a=0, b=0; 
    cin >> str;
    for (i=0; i<n; i++){
        if (str.substr(i, 1) == "A") a++;
        else if (str.substr(i, 1) == "B") b++;
    }
    if(a*b != 0) cout << "Yes" << endl;
    else cout << "No" << endl;

}