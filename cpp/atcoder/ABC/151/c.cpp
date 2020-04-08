#include<iostream>
#include<string>
using namespace std;
#define MAX 100000

int main(){
    int WA[MAX];
    bool AC[MAX];
    int i, n, m, p;
    int wsum = 0, asum = 0;
    string str;

    cin >> n >> m;
    for(i=0; i<m; i++){
        WA[i] = 0;
        AC[i] = false;
    }

    for(i=0; i<m; i++){
        cin >> p >> str;
        if(AC[p] == false){
            if(str == "AC"){
                asum++;
                wsum += WA[p];
                AC[p] = true;
            }else if(str == "WA"){
                WA[p]++;
            }
        }
    }
    cout << asum << " " << wsum << endl;

}