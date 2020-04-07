#include<iostream>
using namespace std;
#include<string>
#include<map>

int main(){
    map<string, int> vote;
    string str;
    int n, i;
    cin >> n;
    for(i=0; i<n; i++){
        cin >> str;
        vote[str] += 1;
    }
    for(auto iter = begin(vote); iter != end(vote); ++iter){
        cout << iter->first << " " << iter->second << endl;

    }

}