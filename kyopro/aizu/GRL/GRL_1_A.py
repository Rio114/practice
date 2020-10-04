import heapq
import numpy as np

def read_data():
    N, M, s = map(int, input().split())
    edges = []
    for m in range(M):
        s, t, w = map(int, input().split())
        edges.append([s, t, w])
    
    return N, M, s, edges

def gen_w_adj_list(edges, N):
    adj_list = []
    for i in range(N):
        adj_list.append([])
    
    for edge in edges:
        adj_list[edge[0]].append([edge[1], edge[2]]) # edge : [target, distance]
        
    return adj_list

def dik(N, start, adj_list, INF=1e+9):
    state = np.ones([N], dtype='int') * (-1)
    distance = np.ones([N], dtype='int') * INF
    parent = np.ones([N], dtype='int') * (-1)

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

    print(distance)

def main():
    N, M, start, edges = read_data()
    adj_list = gen_w_adj_list(edges, N)

    # print(adj_list)
    
    dik(N, start, adj_list, INF=1000000000)

if __name__ == "__main__":
    main()
