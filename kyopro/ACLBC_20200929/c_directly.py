import queue
import numpy as np


def read_data():
  N, M = map(int, input().split())
  nodes = np.zeros([M,2], dtype='int')

  for i in range(M):
    b, c = map(int, input().split())
    nodes[i][0] = b-1
    nodes[i][1] = c-1

  return N, M, nodes	

def main():
  N, M, nodes = read_data()
  group = [-1] * N
  
  group_no = -1
  for node in nodes:
    a = node[0]
    b = node[1]
    if group[a] == -1:
      group_no += 1
      group[a] = group_no
      group[b] = group_no
    else:
      group[b] = group[a]
  
  group_arr = np.array(group)
  num_group = len(np.unique(group_arr[group_arr > -1]))
  num_iso = len(group_arr[group_arr == -1])
  print(num_group)
  print(num_iso)
  print(group_arr)
  print(num_group + num_iso - 1)

if __name__ == "__main__":
  main()