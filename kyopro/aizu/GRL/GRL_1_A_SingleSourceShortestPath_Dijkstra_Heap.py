from heapq import heappop, heappush

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


def dik(N, start, adj_list):
    state = []
    dist = []
    for i in range(N):
        state.append(-1)
        dist.append(INF)

    state[start] = 0
    dist[start] = 0
    pq = [(0, start)]

    while True:
        try:
            u = heappop(pq)
        except ValueError:
            break

        state[u[1]] = 1
        for t, d in adj_list[u[1]]:
            if state[t] != 1:
                if dist[t] > dist[u[1]] + d:
                    dist[t] = dist[u[1]] + d
                    state[t] = 0
                    heappush(pq, [dist[t], t])

    return dist


def main():
    N, M, start, edges = read_data()
    adj_list = gen_w_adj_list(edges, N)
    distance = dik(N, start, adj_list)
    for d in distance:
        print(int(d) if d != INF else 'INF')


if __name__ == "__main__":
    main()
