import queue
import numpy as np


def read_data():
  a = input().split(' ')
  N = int(a[0])
  M = int(a[1])

  nodes = np.zeros([M,2], dtype='int')

  for i in range(M):
    b = input().split(' ')
    nodes[i][0] = int(b[0])
    nodes[i][1] = int(b[1])

    return N, M, nodes	

def gen_adj_list(nodes, N):
  adj_list = []
  M = len(nodes)
  for i in range(N):
    adj_list.append([])

  for i in range(M):
    adj_list[nodes[i][0]-1].append(nodes[i][1]-1)
    adj_list[nodes[i][1]-1].append(nodes[i][0]-1)

  return adj_list

def bfs(state, que, adj_list, cnt, start_idx):
  que.put(start_idx)
  state[start_idx] = 1  
  cnt += 1
  while not que.empty():
    i = que.get()
    for j in adj_list[i]:
      if state[j] == 0:
        que.put(j)
        state[j] = 1

  return state, que, cnt

def main():
  N, M, nodes = read_data()
  adj_list = gen_adj_list(nodes, N)

  ## breath first search
  state = np.zeros([N], dtype='int')

  que = queue.Queue()
  cnt = 0

  while state.min() == 0:
    start_idx = np.arange(N)[state==0][0]
    state, que, cnt = bfs(state, que, adj_list, cnt, start_idx)


  out = cnt - 1
  print(out)

if __name__ == "__main__":
  main()