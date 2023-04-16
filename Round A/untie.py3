# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round A - Problem E. Untie
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad9c1
#
# Time:  O(N), N = len(C)
# Space: O(1)
#

def untie():
    C = list(input().strip())
    i = next((i for i in range(len(C)) if C[i] != C[i-1]), -1)
    if i == -1:
        return (len(C)+1)//2
    result = l = 0
    for j in range(i, i+len(C)):
        l += 1
        if j+1 == i+len(C) or C[(j+1)%len(C)] != C[j%len(C)]:
            result += l//2
            l = 0
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, untie()))
