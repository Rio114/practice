#include<iostream>
using namespace std;
#include<bitset>
#define MAX 10

int main() {
    int n, a, b;
    cin >> n >> a >> b;

    for (int tmp = 0; tmp < (1 << n); tmp++) {
        bitset<MAX> s(tmp);
        cout << s << endl;
    }
}