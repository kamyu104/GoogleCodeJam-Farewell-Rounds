# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round D - Problem D. Old Gold
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cada3b
#
# Time:  O(NlogN)
# Space: O(N)
#

def old_gold():
    S = input().strip()
    lookup = {c:-1 for c in "<=>o."}
    prev_eq, prev_gt, next_gt = [], [], []
    can_be_the_first = True
    prefix = [0]*(len(S)+1)
    for i, c in enumerate(S):
        prev_eq.append(lookup['='])
        prev_gt.append(lookup['>'])
        if c == '>':
            next_gt.extend([i]*(i-lookup['>']))
        dp = 0
        if c in "o.":
            dp = (dp+can_be_the_first)%MOD
            left = max(lookup['o'], i-2*(i-lookup['<'])+1)
            if lookup['='] >= left:
                j = i-2*(i-lookup['='])
                if j >= left and prev_eq[lookup['=']] < j and prev_gt[lookup['=']] < j:
                    dp = (dp+(prefix[j+1]-prefix[j]))%MOD
                left = lookup['=']
            j = i
            while j > left:  # Time: O(logN)
                last_gt = prev_gt[j]
                dp = (dp+(prefix[j]-prefix[max(last_gt, left)]))%MOD
                j = i-2*(i-last_gt)
                while j > left and next_gt[j] != last_gt:
                    last_gt = next_gt[j]
                    j = i-2*(i-last_gt)
        prefix[i+1] = (prefix[i]+dp)%MOD
        lookup[c] = i
        if c not in ">.":
            can_be_the_first = False
    return (prefix[-1]-prefix[max(lookup['o'], lookup['>'], lookup['='], 0)])%MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, old_gold()))
