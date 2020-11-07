
class war():
    def __init__(self):
        self.__read_data()
        self.reachables = [[None] * self.V for _ in range(self.V)]
        self.__assign_reashable()

    def __read_data(self):
        self.V, self.E = list(map(int, input().split()))
        self.Nodes = [list(map(int, input().split())) for _ in range(self.E)]

    def __assign_reashable(self):
        for i in range(self.V):
            for j in range(self.V):
                self.reachables[i][j] = (i == j)

        for node in self.Nodes:
            self.reachables[node[0]][node[1]] = True

    def __war(self):
        for m in range(self.V):
            for s in range(self.V):
                if not self.reachables[s][m]:
                    continue
                for t in range(self.V):
                    if not self.reachables[m][t]:
                        continue
                    self.reachables[s][t] = True

        for s in range(self.V - 1):
            for t in range(s+1, self.V):
                if self.reachables[s][t] and self.reachables[t][s]:
                    return 1

        return 0

    def exec(self):
        print(self.__war())


def main():
    obj = war()
    obj.exec()


if __name__ == "__main__":
    main()
