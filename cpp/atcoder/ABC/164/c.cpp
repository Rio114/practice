#include<iostream>
#include<map>
#include<string>
using namespace std;

int main(){
    int n;
    cin >> n;
    string str;
    map<string, int> get;
    for(int i=0; i<n; i++){
        cin >> str;
        if(get.count(str)) get.insert(make_pair(str, 1));
        else get.at(str)++;
    }

    cout << get.size() << endl;
}