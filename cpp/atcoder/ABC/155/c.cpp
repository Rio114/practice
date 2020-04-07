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
    int max_vote = 0;
    for(auto iter = begin(vote); iter != end(vote); ++iter){
        max_vote = max(iter->second, max_vote);
    }

    for(auto iter = begin(vote); iter != end(vote); ++iter){
        if(iter->second == max_vote){
            cout << iter->first << endl;
        }
    }
}