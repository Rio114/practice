import queue

INF = 1e+10


class TreeDiameter():
    def __init__(self):
        self.__read_data()
        self.__assign_adj_list()

    def __read_data(self):
        self.N = int(input())
        self.Nodes = [list(map(int, input().split())) for _ in range(self.N-1)]

    def __assign_adj_list(self):
        self.adj_list = [[] for _ in range(self.N)]
        for node in self.Nodes:
            self.adj_list[node[0]].append([node[1], node[2]])
            self.adj_list[node[1]].append([node[0], node[2]])

    def __bfs_dist(self, s):
        dist = [INF for _ in range(self.N)]  # distance from s
        dist[s] = 0
        q = queue.Queue()
        q.put(s)
        while not q.empty():
            u = q.get()
            for v, w in self.adj_list[u]:
                if dist[v] == INF:
                    dist[v] = dist[u] + w
                    q.put(v)

        return dist

    def __find_max_dist(self, dist):
        max_dist = 0
        target = 0
        for i in range(self.N):
            if max_dist < dist[i]:
                max_dist = dist[i]
                target = i

        return target, max_dist

    def exec(self):
        target, _ = self.__find_max_dist(self.__bfs_dist(0))
        _, max_dist = self.__find_max_dist(self.__bfs_dist(target))
        print(max_dist)


def main():
    obj = TreeDiameter()
    obj.exec()


if __name__ == "__main__":
    main()
