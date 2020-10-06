from heapq import heappop, heappush, heapify

INF = 1e+10

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

def read_data():
    N, M = map(int, input().split())
    edges = []
    for m in range(M):
        s, t, w = map(int, input().split())
        edges.append([w, s, t])
    
    return N, M, edges

def kruskal(N, edges):
    total_cost = 0
    heapify(edges) # edges[(w, s, t)]
    uf = UnionFind(N)

    while True:
        try:
            w, s, t = heappop(edges)
        except:
            break

        if uf.same(s, t) == False:
            total_cost += w
            uf.union(s, t) 

    return total_cost

def main():
    N, M, edges = read_data()
    total_cost = kruskal(N, edges)
    print(total_cost)
    
if __name__ == "__main__":
    main()
