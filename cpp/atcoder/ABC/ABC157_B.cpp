#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main (){
    vector<int> a(9);
    vector<int> c(9);
    for (int i=0; i<9; i++){
        cin >> a.at(i);
        c.at(i) = 0;

    }

    int n;
    cin >> n;
    vector<int> b(n);
    for(int i=0; i<n; i++){
        cin >> b.at(i);

        for (int j=0; j<9; j++){
            if (b.at(i) == a.at(j)){
                c.at(j)++;
            }
        }
    }

    string out;
    if (c.at(0) == 1 && c.at(1) == 1 && c.at(2) == 1){
        out = "Yes";
    }else if (c.at(3) == 1 && c.at(4) == 1 && c.at(5) == 1){
        out = "Yes";
    }else if (c.at(6) == 1 && c.at(7) == 1 && c.at(8) == 1){
        out = "Yes";
    }else if (c.at(0) == 1 && c.at(3) == 1 && c.at(6) == 1){
        out = "Yes";
    }else if (c.at(1) == 1 && c.at(4) == 1 && c.at(7) == 1){
        out = "Yes";
    }else if (c.at(2) == 1 && c.at(5) == 1 && c.at(8) == 1){
        out = "Yes";
    }else if (c.at(0) == 1 && c.at(4) == 1 && c.at(8) == 1){
        out = "Yes";
    }else if (c.at(2) == 1 && c.at(4) == 1 && c.at(6) == 1){
        out = "Yes";
    }else{
        out = "No";
    }

    cout << out << endl;
}