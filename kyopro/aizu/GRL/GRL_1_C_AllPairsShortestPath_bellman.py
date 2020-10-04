
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
    N, M, edges = read_data()
    # adj_list = gen_w_adj_list(edges, N)
    dist_list = []
    negative_cycle_flg = False
    for start in range(N):
        dist = bellman(N, start, edges)
        if dist == False:
            negative_cycle_flg = True
            break
        dist_list.append(dist)

    if negative_cycle_flg:
        print("NEGATIVE CYCLE")
    else:
        for dist in dist_list:
            out = ''
            for d in dist:
                if d != INF:
                    out += str(int(d))
                    out += " "
                else:
                    out += "INF"
                    out += " "
            print(out[:-1])

if __name__ == "__main__":
    main()
