# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round C - Problem B. Immunization Operation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cacb88
#
# Time:  O(M + VlogV)
# Space: O(V)
#

from heapq import heappush, heappop

def immunization_operation():
    V, M = list(map(int, input().strip().split()))
    P = list(map(int, input().strip().split()))
    D = list(map(int, input().strip().split()))
    X = list(map(int, input().strip().split()))
    right, left = [], []
    for i in range(V):
        if P[i] < D[i]:
            right.append(i)
        else:
            left.append(i)
    right.sort(key=lambda x: D[x], reverse=True)
    left.sort(key=lambda x: P[x], reverse=True)
    max_heap = []
    curr = 0
    result = []
    for x in X:
        curr += x
        cnt = 0
        if x > 0:
            while right and D[right[-1]] <= curr:
                right.pop()
                cnt += 1
            while left and P[left[-1]] <= curr:
                heappush(max_heap, -D[left.pop()])
        else:
            while max_heap and -max_heap[0] >= curr:
                heappop(max_heap)
                cnt += 1
        result.append(cnt)
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, immunization_operation()))
