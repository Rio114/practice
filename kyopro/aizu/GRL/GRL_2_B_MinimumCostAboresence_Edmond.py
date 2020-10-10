from heapq import heappush, heappop

def read_data():
    V, E, r = list(map(int, input().split()))
    Edge = [list(map(int, input().split())) for _ in range(0, E)]

    return V, E, r, Edge

def solve(V, Edge, r):
    if V <= 1:
        return 0
    q = [[] for _ in range(0, V)]
    for s, t, w in Edge:
        heappush(q[t], (w, s))
    M = [(0, -1) for _ in range(0, V)]
    for t in range(0, V):
        if t != r:
            w, s = heappop(q[t])
            M[t] = (w, s)
    
    used = [False for _ in range(0, V)]
    hist = []
    cycle = []
    for t in range(0, V):
        w, s = M[t]
        if s == -1 or used[t] == True:
            continue
        if used[t] == False:
            used[t] = True
            hist += [t]
            tt = s
            while used[tt] == False:
                used[tt] = True
                hist += [tt]
                w, s = M[tt]
                if s == -1:
                    hist = []
                    break
                tt = s
            if used[tt] == True and s != -1 and 0 < len(hist):
                try:
                    k = hist.index(tt)
                    cycle = hist[k:]
                except:
                    continue
                finally:
                    pass
                break
                
    if len(cycle) == 0:
        return sum(m[0] for m in M)

    parent = min(cycle)
    rn = [0 for _ in range(0, V)]
    k = 0
    for t in range(0, V):
        if k == parent:
            k += 1
        if t in cycle:
            rn[t] = parent
        else:
            rn[t] = k
            k += 1
            
    Vp = V - len(cycle) + 1
    Ep = []
    for s, t, w in Edge:
        if s in cycle:
            if t in cycle:
                continue
            else:
                Ep += [[parent, rn[t], w]]
        else:
            if t in cycle:
                Ep += [[rn[s], parent, w - M[t][0]]]
            else:
                Ep += [[rn[s], rn[t], w]]
    r = rn[r]
    return solve(Vp, Ep, r) + sum(M[t][0] for t in cycle)



def main():
    V, E, r, Edge = read_data()
    print(solve(V, Edge, r))
    
if __name__ == "__main__":
    main()
