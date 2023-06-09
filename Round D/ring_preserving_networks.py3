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
    def design():
        A_B = [(i, (i+1)%C) for i in range(C)]
        gen = ((j, i) for i in range(2, C) for j in range(int(i == C-1), i-1))
        A_B.extend(next(gen) for _ in range(L-len(A_B)))
        return "\n".join(map(lambda x: " ".join(map(lambda i: str(i+1), x)), A_B))

    def ring():
        adj = [[] for _ in range(C)]
        for u, v in U_V:
            adj[u].append(v)
            adj[v].append(u)
        u = min(range(C), key=lambda x: len(adj[x]))
        result = [-1]*C
        result[0], result[1], result[-1] = u, adj[u][0], adj[u][1]
        lookup = [False]*C
        lookup[result[0]] = lookup[result[1]] = lookup[result[-1]] = True
        left, right = 1, C-1
        for _ in range(C-3):
            if len(adj[result[left]]) < len(adj[result[right]]):
                result[left+1] = next(v for v in adj[result[left]] if not lookup[v])
                lookup[result[left+1]] = True
                left += 1
            else:
                result[right-1] = next(v for v in adj[result[right]] if not lookup[v])
                lookup[result[right-1]] = True
                right -= 1
        return " ".join(map(lambda i: str(i+1), result))

    C, L = list(map(int, input().strip().split()))
    print(design(), flush=True)
    U_V = [list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(L)]
    print(ring(), flush=True)

for case in range(int(input())):
    ring_preserving_networks()
