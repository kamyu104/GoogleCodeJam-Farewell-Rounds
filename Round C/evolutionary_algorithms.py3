# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round C - Problem C. Evolutionary Algorithms
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cad08b
#
# Time:  O(NlogN), pass in PyPy3 but Python3
# Space: O(N)
#

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

def evolutionary_algorithms():
    def iter_dfs():
        cnt = [0]*N
        bit = BIT(len(s_to_idx))
        stk = [(1, 0)]
        while stk:
            step, u = stk.pop()
            if step == 1:
                cnt[u] = -bit.query(s_to_idx[S[u]]-1)
                stk.append((2, u))
                for v in reversed(adj[u]):
                    stk.append((1, v))
            elif step == 2:
                cnt[u] += bit.query(s_to_idx[S[u]]-1)
                bit.add(s_to_idx[K*S[u]], 1)
        return cnt, bit
        
    N, K = list(map(int, input().strip().split()))
    S = list(map(int, input().strip().split()))
    P = list(map(lambda x: int(x)-1, input().strip().split()))
    adj = [[] for _ in range(N)]
    for i, j in enumerate(P, 1):
        adj[j].append(i)
    s_to_idx = {x:i for i, x in enumerate(sorted(set(S)|set(K*s for s in S)))}
    cnt, bit = iter_dfs()
    return sum(cnt[i]*1*(bit.query(s_to_idx[s]-1)-cnt[i]) for i, s in enumerate(S))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, evolutionary_algorithms()))
