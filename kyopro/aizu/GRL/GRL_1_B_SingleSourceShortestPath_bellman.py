
INF = 1e+9


def read_data():
    N, M, start = map(int, input().split())
    edges = []
    for m in range(M):
        s, t, w = map(int, input().split())
        edges.append([s, t, w])

    return N, M, start, edges


def gen_w_adj_list(edges, N):
    adj_list = []
    for i in range(N):
        adj_list.append([])

    for edge in edges:
        # edge : [target, distance]
        adj_list[edge[0]].append([edge[1], edge[2]])

    return adj_list


def bellman(N, start, edges):

    state = []
    dist = []
    for i in range(N):
        state.append(-1)
        dist.append(INF)

    state[start] = 0
    dist[start] = 0
    cnt = 0

    while True:
        update = False
        cnt += 1
        if cnt > N:
            return False

        for s, t, d in edges:
            if dist[s] != INF and dist[t] > dist[s] + d:
                dist[t] = dist[s] + d
                update = True
        if update is False:
            break

    return dist


def main():
    N, M, start, edges = read_data()
    distance = bellman(N, start, edges)
    if distance:
        for d in distance:
            print(int(d) if d != INF else 'INF')
    else:
        print("NEGATIVE CYCLE")


if __name__ == "__main__":
    main()
