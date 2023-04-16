# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round A - Problem C. Rainbow Sort
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cada38
#
# Time:  O(N)
# Space: O(N)
#

def rainbow_sort():
    N = int(input().strip())
    S = list(map(int, input().strip().split()))
    result = []
    lookup = set()
    for i, x in enumerate(S):
        if x not in lookup:
            result.append(x)
        elif x != S[i-1]:
            return "IMPOSSIBLE"
        lookup.add(x)
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, rainbow_sort()))
