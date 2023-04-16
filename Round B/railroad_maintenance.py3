# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round B - Problem D. Railroad Maintenance
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad77d
#
# Time:  O(N + L), pass in PyPy3 but Python3
# Space: O(N + L)
#

# Reference: https://en.wikipedia.org/wiki/Biconnected_component#Algorithms
def iter_get_articulation_points(graph):
    index_counter, index, lowlinks = [0], [-1]*len(graph), [0]*len(graph)
    cutpoints = []
    stk = [(1, (0, -1))]
    while stk:
        step, args = stk.pop()
        if step == 1:
            v, p = args
            index[v] = index_counter[0]
            lowlinks[v] = index_counter[0]
            index_counter[0] += 1
            children_count = [0]
            is_cut = [False]
            stk.append((4, (v, p, children_count, is_cut)))
            for w in reversed(graph[v]):
                if w == p:
                    continue
                stk.append((2, (w, v, children_count, is_cut)))
        elif step == 2:
            w, v, children_count, is_cut = args
            if index[w] == -1:
                children_count[0] += 1
                stk.append((3, (w, v, is_cut)))
                stk.append((1, (w, v)))
            else:
                lowlinks[v] = min(lowlinks[v], index[w])
        elif step == 3:
            w, v, is_cut = args
            if lowlinks[w] >= index[v]:  # (v, w) is a bridge
                is_cut[0] = True
            lowlinks[v] = min(lowlinks[v], lowlinks[w])
        elif step == 4:
            v, p, children_count, is_cut = args
            if (p != -1 and is_cut[0]) or (p == -1 and children_count[0] >= 2):
                cutpoints.append(v)
    return cutpoints

def railroad_maintenance():
    N, L = list(map(int, input().strip().split()))
    adj = [[] for _ in range(N+L)]
    for i in range(N, N+L):
        _  = int(input().strip())
        S = list(map(lambda x: int(x)-1, input().strip().split()))
        for j in S:
            adj[i].append(j)
            adj[j].append(i)
    return sum(i >= N for i in iter_get_articulation_points(adj))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, railroad_maintenance()))
