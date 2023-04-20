# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round D - Problem A. Indispensable Overpass
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cadc76
#
# Time:  O(W + E + C)
# Space: O(W + E)
#

def indispensable_overpass():
    def dist(P):
        N = len(P)+1
        D = [0]*N
        for i in reversed(range(N-1)):
            D[i] = D[P[i]]+1
        cnt = [1]*N
        for i in range(N-1):
            cnt[P[i]] += cnt[i]
        dp = [0]*N
        dp[-1] = sum(D)
        for i in reversed(range(N-1)):
            dp[i] = dp[P[i]]-cnt[i]+(N-cnt[i])
        return dp, sum(dp)//2

    W, E, C = list(map(int, input().strip().split()))
    X = list(map(lambda x: int(x)-1, input().strip().split()))
    F = list(map(lambda x: int(x)-1, input().strip().split()))
    A_B = [list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(C)]
    dp1, d1 = dist(X)
    dp2, d2 = dist(F)
    total = (W+E)*((W+E)-1)//2
    result = [(dp1[A]*E + dp2[B]*W + W*E + (d1+d2))/total for A, B in A_B]
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, indispensable_overpass()))
