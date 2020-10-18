import sys
sys.setrecursionlimit(1000000)

class scc():
    def __init__(self):
        self.__read_data()
        self.__adj_inv_list()

    def __read_data(self):
        self.V, self.E = list(map(int, input().split()))
        self.Edges = [list(map(int, input().split())) for _ in range(self.E)]
        self.Q = int(input())
        self.Quests = [list(map(int, input().split())) for _ in range(self.Q)]

    def __adj_inv_list(self):
        self.adj = [[] for _ in range(self.V)]
        self.inv = [[] for _ in range(self.V)]
        for edge in self.Edges:
            self.adj[edge[0]].append(edge[1])
            self.inv[edge[1]].append(edge[0])

    def __dfs(self, curr):
        self.status[curr] = 1
        for next_v in self.adj[curr]:
            if self.status[next_v] != 1:
                self.__dfs(next_v)
        self.order.append(curr)

    def __rev_dfs(self, curr, root):
        self.status[curr] = 1
        self.parents[curr] = root
        for next_v in self.inv[curr]:
            if self.status[next_v] != 1:
                self.__rev_dfs(next_v, root)

    def show(self):
        print("order: ", self.order)
        print("parents: ", self.parents)

    def exec(self):
        self.order = []
        self.status = [-1] * self.V
        self.parents = [-1] * self.V
        for i in range(self.V):
            if self.status[i] != 1: 
                self.__dfs(i)

        self.status = [-1] * self.V
        self.parents = [None for i in range(self.V)]

        for i in reversed(self.order):
            if self.parents[i] == None:
                self.__rev_dfs(i, i)

    def find_scc(self):
        for q in self.Quests:
            v = self.parents[q[0]]
            u = self.parents[q[1]]
            # print(v, u)
            print(1 if v == u else 0)
            
def main():
    obj = scc()
    obj.exec()
    obj.find_scc()

if __name__ == "__main__":
    main()
