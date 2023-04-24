# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round D - Problem E. Ring-Preserving Networks
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cad08a
#
# Time:  O(L)
# Space: O(L)
#
# python interactive_runner.py python3 testing_tool.py -- python3 ring_preserving_networks.py3
#

def ring_preserving_networks():
    C, L = list(map(int, input().strip().split()))
    A_B = [(i, i+1) for i in range(1, C)]
    A_B.append((1, C))
    it = ((j, i) for i in range(1, C+1) for j in reversed(range(1, (i-2)+1)))
    for _ in range(L-len(A_B)):
        A_B.append(next(it))
    print("\n".join(map(lambda x: " ".join(map(str, x)), A_B)), flush=True)
    U_V = [list(map(int, input().strip().split())) for _ in range(L)]
    adj = [[] for _ in range(C+1)]
    for u, v in U_V:
        adj[u].append(v)
        adj[v].append(u)
    for u in range(1, C+1):
        adj[u].reverse()
    u = min(range(1, C+1), key=lambda x: len(adj[x]))
    result = [0]*C
    result[0], result[-1], result[1] = u, adj[u][-1], adj[u][-2]
    lookup = [False]*(C+1)
    lookup[result[0]] = lookup[result[-1]] = lookup[result[1]] = True
    left, right = 1, C-1
    while left <= right:
        if len(adj[result[left]]) < len(adj[result[right]]):
            while adj[result[left]]:
                u = adj[result[left]].pop()
                if lookup[u]:
                    continue
                lookup[u] = True
                result[left+1] = u
                break
            left += 1
        else:
            while adj[result[right]]:
                u = adj[result[right]].pop()
                if lookup[u]:
                    continue
                lookup[u] = True
                result[right-1] = u
                break
            right -= 1
    print(" ".join(map(str, result)), flush=True)

for case in range(int(input())):
    ring_preserving_networks()
