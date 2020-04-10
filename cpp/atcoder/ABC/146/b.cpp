#include<iostream>
#include<string>
using namespace std;

int main(){
    int i, n;
    string s;
    cin >> n >> s;
    int m = s.size();
    int aloc='A', zloc='Z';
    // cout << aloc << " " << zloc << endl;
    int loc;
    for(i=0; i<m; i++){
        loc = s.at(i);
        // cout << loc << endl;
        if(loc + n > zloc) s.at(i) = aloc + n - zloc + loc-  1; 
        else s.at(i) += n;
    }
    cout << s << endl;
}