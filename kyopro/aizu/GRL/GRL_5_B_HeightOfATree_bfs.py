
INF = 1e+10


class TreeHeight():
    def __init__(self):
        self.__read_data()
        self.__assign_adj_list()
        self.__assing_dist_mat()
        self.preorder = []
        self.postorder = []

    def __read_data(self):
        self.N = int(input())
        self.Nodes = [list(map(int, input().split())) for _ in range(self.N-1)]

    def __assign_adj_list(self):
        self.adj_list = [[] for _ in range(self.N)]
        for node in self.Nodes:
            self.adj_list[node[0]].append([node[1], node[2]])
            self.adj_list[node[1]].append([node[0], node[2]])

    def __assing_dist_mat(self):
        self.dist_mat = [[INF for i in range(self.N)] for j in range(self.N)]
        for i in range(self.N):
            self.dist_mat[i][i] = 0

    def __dfs(self, curr, prev):
        self.preorder.append((curr, prev))
        for v, w in self.adj_list[curr]:
            if v != prev:
                self.__dfs(v, curr)
        self.postorder.append(curr)

    # def __find_max_dist(self):
    #     for dists in self.dist_mat:
    #         print(max(dists))

    def exec(self):
        self.__dfs(0, None)
        print(self.preorder)
        print(self.postorder)

        # for s in range(self.N):
        #     self.__bfs_dist(s)
        # self.__find_max_dist()


def main():
    obj = TreeHeight()
    obj.exec()


if __name__ == "__main__":
    main()
