#include<iostream>
#include<list>
#include<string>
using namespace std;

// static const int SMAX = 100000;

int main(){
    string s;
    list<char> l;
    int q;
    cin >> s >> q;

    for(int i=0; i<s.size(); i++){
        l.push_back(s.at(i));
    }

    for(int i=0; i<q; i++){
        int t;
        cin >> t;
        if(t == 1){
            l.reverse();
        }else if(t == 2){
            int f;
            char c;
            cin >> f >> c;
            if(f == 1){
                l.push_front(c);
            }else if(f == 2){
                l.push_back(c);
            }

        }     
    }

    for(list<char>::iterator it=l.begin(); it != l.end(); it++){
        cout << *it;
    }
    cout << endl;
    
}