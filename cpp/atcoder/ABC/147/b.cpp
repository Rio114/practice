#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    string str, inv;
    cin >> str;
    inv = str;
    reverse(inv.begin(), inv.end());
    int i, cnt=0;
    for(i=0; i<str.size(); i++){
        // cout << str.at(i) << " " << inv.at(i) << endl;
        if(str.at(i) != inv.at(i)) cnt++;
    }
    cout << cnt / 2 << endl;

}