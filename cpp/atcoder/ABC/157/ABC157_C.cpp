#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    vector<int> s(m);
    vector<int> c(m);
    vector<int> out(3);
    for(int i=0; i<m; i++){
        cin >> s.at(i) >> c.at(i);
    }

    for(int i=0; i<3; i++){
        out.at(i) = 0;
    }
    
    for (int j=0; j<m; j++){
        int order = s.at(j)-1;
        int cand = c.at(j);
        if(out.at(order) > 0 && out.at(order) != cand){
            n = 0;
            break;
        }else if(order ==2 && out.at(order) > 0 && out.at(order) != cand){
            n = 0;
            break;
        }else if (out.at(order) < cand){
            out.at(order) = cand;
        }
    }
    
    if(n == 0){
        cout << -1 << endl;
    }else if (n==3){
        if(out.at(0) == 0){
            cout << -1 << endl;
        }else{
            cout << out.at(0) << out.at(1) << out.at(2) << endl;
        }
    }else if(n==2){
        if (out.at(0) > 0 ){
            cout << -1 << endl;
        }else if (out.at(1) == 0){
            cout << -1 << endl;
        }else{
            cout << out.at(1) << out.at(2) << endl;
        }
    }else if(n==1){
        if (out.at(0) > 0 || out.at(1) > 0){
            cout << -1 << endl;
        }else{
            cout << out.at(2) << endl;
        }
    }
}