import sys
sys.setrecursionlimit(1000000)


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


class Lowest():
    def __init__(self, adj_list, V, start=0):
        INF = 1e+10
        self.adj = adj_list
        self.V = V
        self.states = [-1 for _ in range(V)]
        self.prenum = [-1 for _ in range(V)]
        self.parents = [-1 for _ in range(V)]
        self.bridges = set()
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

                if self.lowest[next_v] > self.prenum[current]:
                    self.bridges.add(
                        (min(current, next_v), max(current, next_v)))
                self.lowest[current] = min(
                    self.lowest[current], self.lowest[next_v])
            elif next_v != prev:
                self.lowest[current] = min(
                    self.lowest[current], self.prenum[next_v])

    def show(self):
        print("prenum: ", self.prenum)
        print("lowest: ", self.lowest)
        print("parents: ", self.parents)

    def show_bridges(self):
        self.__dfs(0, -1)
        for b in sorted(self.bridges):
            print(b[0], b[1])


def main():
    V, E, Edges = read_data()
    adj_list = gen_adj_list(Edges, V)
    AP = Lowest(adj_list, V)
    AP.show_bridges()
    # AP.show()


if __name__ == "__main__":
    main()
