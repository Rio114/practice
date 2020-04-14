#include<iostream>
#include<stack>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    stack<int> depth;
    stack<pair<int, int> > s;
    int sum = 0;
    char ch;

    for(int i=0; cin >> ch; i++){
        if(ch == '\\')depth.push(i);
        else if(ch == '/' && depth.size()>0){
            int j = depth.top(); depth.pop();
            int a = i - j;
            sum += a;
            while(s.size()>0 && s.top().first > j){
                a += s.top().second; s.pop();
            }
            s.push(make_pair(j, a));
        }
    }

    vector<int> ans;
    while (s.size()>0){ans.push_back(s.top().second); s.pop();}
    reverse(ans.begin(), ans.end());
    cout << sum << endl;
    cout << ans.size();
    for(int i=0; i<ans.size(); i++){
        cout << " ";
        cout << ans.at(i);
    }
    cout << endl;
}