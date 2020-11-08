import sys
sys.setrecursionlimit(1000000)


class TreeHeight():
    def __init__(self):
        self.__read_data()
        self.__assign_adj_list()
        self.max_dist = 0
        self.max_id = -1

    def __read_data(self):
        self.N = int(input())
        self.Nodes = [list(map(int, input().split())) for _ in range(self.N-1)]

    def __assign_adj_list(self):
        self.adj_list = [[] for _ in range(self.N)]
        for node in self.Nodes:
            self.adj_list[node[0]].append([node[1], node[2]])
            self.adj_list[node[1]].append([node[0], node[2]])

    def __dfs(self, curr, prev, dists):
        for v, w in self.adj_list[curr]:
            if v == prev:
                continue
            dists[v] = dists[curr] + w
            if self.max_dist <= dists[v]:
                self.max_dist = dists[v]
                self.max_id = v
            self.__dfs(v, curr, dists)

    def exec(self):
        dists0 = [0 for _ in range(self.N)]
        dists1 = [0 for _ in range(self.N)]
        dists2 = [0 for _ in range(self.N)]

        self.__dfs(0, None, dists0)
        self.__dfs(self.max_id, None, dists1)
        self.__dfs(self.max_id, None, dists2)

        for i in range(self.N):
            print(max(dists1[i], dists2[i]))


def main():
    obj = TreeHeight()
    obj.exec()


if __name__ == "__main__":
    main()
