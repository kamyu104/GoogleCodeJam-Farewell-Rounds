# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round B - Problem E. Railroad Management
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000caccfb
#
# Time:  O(N)
# Space: O(N)
#

def railroad_management():
    N = int(input())
    D = list(map(lambda x: int(x)-1, input().strip().split()))
    C = list(map(int, input().strip().split()))
    R = [0]*N
    for i in range(N):
        R[D[i]] += C[i]
    result = sum(max(C[i]-R[i], 0) for i in range(N))
    lookup = [-1]*N
    for i in range(N):
        if lookup[i] != -1:
            continue
        j = i
        while lookup[j] == -1:
            lookup[j] = i
            j = D[j]
        if lookup[j] != i:
            continue
        mn = float("inf")
        k = j
        while True:
            mn = min(mn, max(C[D[k]]-(R[D[k]]-C[k]), 0)-max(C[D[k]]-R[D[k]], 0))
            k = D[k]
            if k == j:
                break
        result += mn
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, railroad_management()))
