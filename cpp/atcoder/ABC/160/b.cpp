#include<iostream>
using namespace std;

int main(){
    int x;
    cin >> x;
    int num_500, res_500;
    num_500 = x / 500;
    res_500 = x % 500;
    int num_5;
    num_5 = res_500 / 5;

    int ans = num_500 * 1000 + num_5 * 5;

    cout << ans << endl;
    
}