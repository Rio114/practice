#include<iostream>
#include<vector>

using namespace std;

class DisjointSet{
    public:
        vector<int> rank, parent;

        DisjointSet(){}
        DisjointSet(int size){
            rank.resize(size, 0);
            parent.resize(size, 0);
            for(int i=0; i<size; i++) makeSet(i);
        }

        void makeSet(int x){
            parent.at(x) = x;
            rank.at(x) = 0;
        }

        bool same(int x, int y){
            return findSet(x) == findSet(y);
        }

        void unite(int x, int y){
            link(findSet(x), findSet(y));
        }

        void link(int x, int y){
            if(rank.at(x) > rank.at(y)){
                parent.at(y) = x;
            }else {
                parent.at(x) = y;
                if(rank.at(x) == rank.at(y)){
                    rank.at(y)++;
                }

            }
        }

        int findSet(int x){
            if(x != parent.at(x)){
                parent.at(x) = findSet(parent.at(x));
            }
            return parent.at(x);
        }

};

int main(){
    int n, a, b, q;
    int t;

    cin >> n >> q;
    DisjointSet ds = DisjointSet(n);

    for(int i=0; i<q; i++){
        cin >> t >> a >> b;
        if (t == 0) ds.unite(a, b);
        else if(t == 1){
            if(ds.same(a, b)) cout << 1 << endl;
            else cout << 0 << endl;
        }
    }
}
