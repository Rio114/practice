#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<stack>
#include<iostream>
#include<tuple>
using namespace std;

int main(){
    char land[20000];
    stack<int> depth;
    stack<tuple<int, int>> s;
    int a = 0, a_total=0;
    vector<int> area;
    scanf("%s", land);
    int n = strlen(land);

    for(int i=0; i<n; i++){
        if(land[i] == '\\'){
            depth.push(i);
        }else if(land[i] == '/'){
            if(!depth.empty()){
                int j = depth.top(); depth.pop();
                int dist = i - j - 1;
                int diff_a = (dist + dist + 2) / 2;
                s.push(make_tuple(j, diff_a));
                a += diff_a; 
                a_total += diff_a;
                if(depth.empty()){
                    area.push_back(a);
                    a = 0;
                }
            }
        }
        if (i==n-1 && a > 0){
            area.push_back(a);
        }
    }
    int area_total = 0;
    int n_area = area.size();
    cout << a_total << endl;
    cout << n_area << " ";
    for(int i=0; i<n_area; i++){
        int b = area.at(i);
        area_total += b;
        cout << b;
        if(i<n-1) cout << " ";
    }
    cout << endl;
    cout  << area_total << endl;
}