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

def game_sort_part_1():
    def find_nondecreasing(i):
        prev, curr = (result[i-1] if i else []), result[i]
        cnt = Counter(S[i])
        for c in prev:
            if cnt[c]:
                cnt[c] -= 1
                curr.append(c)
                continue
            c = next((c for c in reversed(ascii_uppercase) if cnt[c]), ascii_uppercase[0])
            for i in reversed(range(len(curr)+1)):
                if c > prev[i]:
                    c = next((c for c in ascii_uppercase if c > prev[i] and cnt[c]))
                    cnt[c] -= 1
                    curr.append(c)
                    break
                if curr:
                    c = max(c, curr[-1])
                    cnt[curr.pop()] += 1
            else:
                return False
            break
        for c in ascii_uppercase:
            curr.extend([c]*cnt[c])
        return True

    P = int(input())
    S = list(input().strip().split())
    result = [[] for _ in range(P)]
    return "POSSIBLE\n%s" % " ".join(map(lambda x: "".join(x), result)) if all(find_nondecreasing(i) for i in range(P)) else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, game_sort_part_1()))
