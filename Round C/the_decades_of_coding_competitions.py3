# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round C - Problem D. The Decades of Coding Competitions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cad9c6
#
# Time:  O(K * (N + M + Q)), pass in PyPy3 but Python3
# Space: O(K * N)
#

from collections import defaultdict

class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0]*n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        return True

def the_decades_of_coding_competitions():
    N, M, Q = list(map(int, input().strip().split()))
    U_V_K = [list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(M)]
    P_C = [list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(Q)]
    uf = UnionFind(N)
    uf_exclude = defaultdict(lambda: UnionFind(N))
    K_set = set(K for _, _, K in U_V_K)
    for U, V, K in U_V_K:
        uf.union_set(U, V)
        for k in K_set:
            if k != K:
                uf_exclude[k].union_set(U, V)
    group = defaultdict(set)
    for U, V, K in U_V_K:
        group[uf.find_set(U)].add(K)
    return sum(len(group[uf.find_set(P)])%2 == 1 or
               any(uf_exclude[k].find_set(P) == uf_exclude[k].find_set(C) for k in group[uf.find_set(P)])
               for P, C in P_C if uf.find_set(P) == uf.find_set(C))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, the_decades_of_coding_competitions()))
