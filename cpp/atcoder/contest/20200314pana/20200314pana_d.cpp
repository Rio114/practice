#include <bits/stdc++.h>
using namespace std;

vector<string> tree(int n){
    if(n ==1 ){
        vector<string> out;
        out.push_back('a');
        return out;
    }

    vector<string> a = tree(n-1);
    vector<string> b;

    int num = tree.size();
    for(int i=0; i<num: i++){
        string str = tree.at(i);
        for (int j=0; j<n; j++){
            char add = 'a' + j;
            string str_new = str + add;
            b.push_back(str_new);
        }
    }
    return b;
}

int main(){
    int n;
    cin >> n;
    cout << 'a' << endl;

    vector<string> out;
    out = tree(n);
    int num = tree.size();

    



}