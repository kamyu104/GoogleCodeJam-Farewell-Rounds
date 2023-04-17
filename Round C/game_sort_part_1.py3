# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round C - Problem A. Game Sort: Part 1
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cacb87
#
# Time:  O(P * L), L = max(len(s) for s in S)
# Space: O(L)
#

from collections import Counter
from string import ascii_uppercase

def collecting_pancakes():
    def find_candidate(curr, s, cnt):
        candidate = []
        for i in range(len(curr)):
            if not cnt[curr[i]]:
                c = next((c for c in ascii_uppercase if c > curr[i] and cnt[c]), None)
                if c is None:
                    break
                cnt[c] -= 1
                candidate.append(c)
                break
            cnt[curr[i]] -= 1
            candidate.append(curr[i])
        for c in ascii_uppercase:
            candidate.extend([c]*cnt[c])
            cnt[c] = 0
        return candidate

    def find_nondecreasing(curr, s):
        cnt = Counter(s)
        new_curr = find_candidate(curr, s, cnt)
        if not (curr <= new_curr):
            for i in reversed(range(len(curr), len(new_curr))):
                cnt[new_curr.pop()] += 1
            for i in reversed(range(len(new_curr))):
                cnt[new_curr.pop()] += 1
                c = next((c for c in ascii_uppercase if c > curr[i] and cnt[c]), None)
                if c is None:
                    continue
                cnt[c] -= 1
                new_curr.append(c)
                break
            for c in ascii_uppercase:
                new_curr.extend([c]*cnt[c])
        return new_curr if curr <= new_curr else []

    P = int(input())
    S = list(input().strip().split())
    result = []
    curr = []
    for s in S:
        curr = find_nondecreasing(curr, s)
        if not curr:
            return "IMPOSSIBLE"
        result.append("".join(curr))
    return "POSSIBLE\n%s" % " ".join(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, collecting_pancakes()))