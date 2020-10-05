from heapq import heappop, heappush

INF = 1e+10

def read_data():
    N, M = map(int, input().split())
    edges = []
    for m in range(M):
        s, t, w = map(int, input().split())
        edges.append([s, t, w])
    
    return N, M, edges

def gen_w_adj_list(edges, N):
    adj_list = []
    for i in range(N):
        adj_list.append([])
    
    for edge in edges:
        adj_list[edge[0]].append([edge[1], edge[2]]) # edge : [target, distance]
        adj_list[edge[1]].append([edge[0], edge[2]]) # edge : [target, distance]
        
    return adj_list

def prim(N, start, adj_list):

    states = []
    dists = []
    parents = []
    for i in range(N):
        states.append(-1)
        dists.append(INF)
        parents.append(-1)

    states[start] = 0
    dists[start] = 0

    pq = [(0, start)]

    while True:
        try:
            u = heappop(pq)
        except:
            break

        states[u[1]] = 1

        for t, d in adj_list[u[1]]:
            if states[t] != 1 and dists[t] > d:
                dists[t] = d
                parents[t] = u[1]
                states[t] = 0
                heappush(pq, (d, t))

    return dists

def main():
    N, M, edges = read_data()
    adj_list = gen_w_adj_list(edges, N)
    start = 0
    dists = prim(N, start, adj_list)
    print(dists)
    dist_sum = 0
    for i in dists:
        dist_sum += int(i)
    print(dist_sum)
    
if __name__ == "__main__":
    main()
