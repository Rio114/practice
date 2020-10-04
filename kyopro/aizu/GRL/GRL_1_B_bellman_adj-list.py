
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
        adj_list[edge[0]].append([edge[1], edge[2]]) # edge : [target, distance]
        
    return adj_list

def bellman(N, start, adj_list):
    state = []
    distance = []
    for i in range(N):
        state.append(-1)
        distance.append(INF)

    state[start] = 0
    distance[start] = 0
    
    while True:
        min_cost = INF
        u = -1
        for i in range(N):
            if state[i] != 1 and distance[i] < min_cost:
                min_cost = distance[i]
                u = i
        
        if u == -1:
            break
        
        state[u] = 1
        for t, d in adj_list[u]:
            if state[t] != 1:
                if distance[t] > distance[u] + d :
                    distance[t] = distance[u] + d
                    state[t] = 0

    return distance

def main():
    N, M, start, edges = read_data()
    adj_list = gen_w_adj_list(edges, N)
    distance = bellman(N, start, adj_list)
    for d in distance:
        print(int(d) if d != INF else 'INF')
    
if __name__ == "__main__":
    main()
