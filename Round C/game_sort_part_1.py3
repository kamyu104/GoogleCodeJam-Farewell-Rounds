# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round C - Problem A. Game Sort: Part 1
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cacb87
#
# Time:  O(P * L), L = max(len(s) for s in S)
# Space: O(1)
#

from collections import Counter
from string import ascii_uppercase

def collecting_pancakes():
    def find_nondecreasing(i):
        curr, new_curr = (result[i-1] if i else []), result[i]
        cnt = Counter(S[i])
        for c in curr:
            if cnt[c]:
                cnt[c] -= 1
                new_curr.append(c)
                continue
            for i in reversed(range(len(new_curr)+1)):
                c = next((c for c in ascii_uppercase if c > curr[i] and cnt[c]), None)
                if c:
                    cnt[c] -= 1
                    new_curr.append(c)
                    break
                if new_curr:
                    cnt[new_curr.pop()] += 1
            else:
                return False
            break
        for c in ascii_uppercase:
            new_curr.extend([c]*cnt[c])
        return True

    P = int(input())
    S = list(input().strip().split())
    result = [[] for _ in range(P)]
    if not all(find_nondecreasing(i) for i in range(P)):
        return "IMPOSSIBLE"
    return "POSSIBLE\n%s" % " ".join(map(lambda x: "".join(x), result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, collecting_pancakes()))
