#include<iostream>
#include<string>
using namespace std;

int main(){
    string c;
    int ans;

    cin >> c;
    
    if(c == "SUN"){
        ans = 7;
    }else if(c == "MON"){
        ans = 6;
    }else if(c == "TUE"){
        ans = 5;
    }else if(c == "WED"){
        ans = 4;
    }else if(c == "THU"){
        ans = 3;
    }else if(c == "FRI"){
        ans = 2;
    }else if(c == "SAT"){
        ans = 1;
    }
    cout << ans << endl;


}


