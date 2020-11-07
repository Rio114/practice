import queue


class topological():
    def __init__(self):
        self.__read_data()
        self.status = [-1 for _ in range(self.V)]
        self.indeg = [0 for _ in range(self.V)]
        self.__assign_indeg()
        self.__assign_adj_list()
        self.out = []

    def __read_data(self):
        self.V, self.E = list(map(int, input().split()))
        self.Nodes = [list(map(int, input().split())) for _ in range(self.E)]

    def __assign_indeg(self):
        for node in self.Nodes:
            self.indeg[node[1]] += 1

    def __assign_adj_list(self):
        self.adj_list = [[] for _ in range(self.V)]
        for node in self.Nodes:
            self.adj_list[node[0]].append(node[1])

    def __bfs(self, s):
        q = queue.Queue()
        q.put(s)
        self.status[s] = 1
        while not q.empty():
            u = q.get()
            self.out.append(u)
            for v in self.adj_list[u]:
                self.indeg[v] -= 1
                if self.indeg[v] == 0 and self.status[v] != 1:
                    self.status[v] = 1
                    q.put(v)

    def __sort(self):
        for i in range(self.V):
            if self.indeg[i] == 0 and self.status[i] != 1:
                self.__bfs(i)

    def exec(self):
        self.__sort()

    def show(self):
        for i in self.out:
            print(i)


def main():
    obj = topological()
    obj.exec()
    obj.show()


if __name__ == "__main__":
    main()
