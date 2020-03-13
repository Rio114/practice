#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main(){
    int n, num_pattern, count;
    cin >> n;
    vector<int> arr(n);
    for (int i=0; i<n; i++){
        cin >> arr.at(i);
    }

    sort(arr.begin(), arr.end());
    decltype(arr)::iterator result = unique(arr.begin(), arr.end());
    arr.erase(result, arr.end());
    count = arr.size();
    cout << count << endl;
}