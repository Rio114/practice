#include <bits/stdc++.h>
#include <string>
using namespace std;

int main(){
    string str, new_str;
    cin >> str;

    int length=1, pos;
    string out;
    while (length > 0){
        int dreamer, dream, erase, eraser, dreameraser, dreamerase;
        dreamer = str.find("dreamer"); //7
        dream = str.find("dream"); //5
        eraser = str.find("eraser"); //6
        erase = str.find("erase"); // 5
        dreamerase = str.find("dreamerase"); //10
        dreameraser = str.find("dreameraser"); //11
        
        pos =  dreamer * dream * erase * eraser * dreameraser * dreamerase;
        if (pos != 0){
            out = "NO";
            break;
        }

        if (dreameraser == 0){
            new_str = str.substr(11);
        }else if (dreamerase == 0){
            new_str = str.substr(10);
        }else if (dreamer == 0){
            new_str = str.substr(7);
        }else if (eraser == 0){
            new_str = str.substr(6);
        }else if (dream == 0){
            new_str = str.substr(5);
        }else if (erase == 0){
            new_str = str.substr(5);
        }

        str = new_str;
        length = new_str.length();
        if (length == 0){
            out = "YES";
            break;


        }
    }

    cout << out << endl;


}