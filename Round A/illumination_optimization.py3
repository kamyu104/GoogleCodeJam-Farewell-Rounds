# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round A - Problem B. Illumination Optimization
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad086
#
# Time:  O(N)
# Space: O(1)
#

def illumination_optimization():
    M, R, N = list(map(int, input().strip().split()))
    X = list(map(int, input().strip().split()))
    result = curr = 0
    for i in range(N):
        if i+1 < N and X[i+1]-R <= curr:
            continue 
        if X[i]-R > curr:
            break
        result += 1
        curr = X[i]+R
        if curr >= M:
            break
    return result if curr >= M else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, illumination_optimization()))
