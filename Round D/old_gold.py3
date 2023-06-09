# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round D - Problem D. Old Gold
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cada3b
#
# Time:  O(NlogN), pass in PyPy3 but Python3
# Space: O(N)
#

from collections import defaultdict

def old_gold():
    S = input().strip()
    lookup = defaultdict(lambda: -1)
    prev_prev_eq = -1
    prev_gt, next_gt = [[-1]*len(S) for _ in range(2)]
    can_be_the_first = True
    prefix = [0]*(len(S)+1)
    for i, c in enumerate(S):
        dp = 0
        if c == '=':
            prev_prev_eq = lookup['=']
        elif c == '>':
            for j in range(lookup['>']+1, i+1):
                next_gt[j] = i
        elif c in "o.":
            dp = (dp+can_be_the_first)%MOD
            left = max(lookup['o'], i-2*(i-lookup['<'])+1)
            if lookup['='] >= left:
                j = i-2*(i-lookup['='])
                if j >= max(left, prev_prev_eq+1, prev_gt[lookup['=']]+1):
                    dp = (dp+(prefix[j+1]-prefix[j]))%MOD
                left = lookup['=']+1
            j = i-1
            while j >= left:  # Time: O(logN)
                dp = (dp+(prefix[j+1]-prefix[max(prev_gt[j], left)]))%MOD
                j = i-2*(i-prev_gt[j])-1
                while j >= left and next_gt[j] != ((j+1)+i)//2:
                    j = i-2*(i-next_gt[j])-1
        prefix[i+1] = (prefix[i]+dp)%MOD
        lookup[c] = i
        prev_gt[i] = lookup['>']
        if c not in ">.":
            can_be_the_first = False
    return (prefix[-1]-prefix[max(lookup['=']+1, lookup['>']+1, lookup['o'])])%MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, old_gold()))
