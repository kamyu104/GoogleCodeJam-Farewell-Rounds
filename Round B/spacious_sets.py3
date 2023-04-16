# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round B - Problem C. Spacious Sets
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad2ce
#
# Time:  O(NlogN)
# Space: O(N)
#

from bisect import bisect_left, bisect_right

def collecting_pancakes():
    N, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    sorted_A = sorted(A)
    left = [0]*N
    for i in range(N):
        j = bisect_right(sorted_A, sorted_A[i]-K)-1
        left[i] = left[j]+1 if j >= 0 else 1
    right = [0]*N
    for i in reversed(range(N)):
        j = bisect_left(sorted_A, sorted_A[i]+K)
        right[i] = right[j]+1 if j < N else 1
    result = [0]*N
    for i in range(N):
        j = bisect_left(sorted_A, A[i])
        result[i] = left[j]+right[j]-1
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, collecting_pancakes()))
