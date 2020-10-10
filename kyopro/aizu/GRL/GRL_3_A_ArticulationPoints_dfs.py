
import heapq

def read_data():
    V, E = list(map(int, input().split()))
    Edges = [list(map(int, input().split())) for _ in range(0, E)]

    return V, E, Edges

def gen_adj_list(edges, V):
    adj_list = [[] for _ in range(V)]

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
        
    return adj_list


class ArticulationPoints():
    def __init__(self, adj_list, V, start=0):
        INF = 1e+10
        self.adj = adj_list
        self.V = V
        self.states = [-1 for _ in range(V)]
        self.prenum = [-1 for _ in range(V)]
        self.parents = [-1 for _ in range(V)]
        self.lowest = [INF for _ in range(V)]
        self.start = start
        self.timer = 0

    def __dfs(self, current, prev):
        self.prenum[current] = self.timer
        self.lowest[current] = self.timer
        self.timer += 1

        self.states[current] = 1

        for next_v in self.adj[current]:
            if self.states[next_v] != 1:
                self.parents[next_v] = current

                self.__dfs(next_v, current)
                self.lowest[current] = min(self.lowest[current], self.lowest[next_v])
            elif next_v != prev:
                self.lowest[current] = min(self.lowest[current], self.prenum[next_v])

    def show(self):
        print("prenum: ", self.prenum)
        print("lowest: ", self.lowest)
        print("parents: ", self.parents)

    def find_ap(self):
        start = 0
        self.__dfs(start, -1)

        ap = []
        np = 0

        for i in range(self.V):
            p = self.parents[i]
            if p == 0:
                np += 1
            elif self.prenum[p] <= self.lowest[i] and p > -1:
                ap.append(p)
        if np > 1:
            ap.append(0)
        ap = list(set(ap))
        ap.sort()
        for out in ap:
            print(out)

def main():
    V, E, Edges = read_data()
    adj_list = gen_adj_list(Edges, V)
    AP = ArticulationPoints(adj_list, V)
    AP.find_ap()
    # AP.show()
    
if __name__ == "__main__":
    main()
