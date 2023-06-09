# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round A - Problem A. Colliding Encoding
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad7cf
#
# Time:  O(N)
# Space: O(N)
#

def colliding_encoding():
    D = list(input().strip().split())
    N = int(input())
    S = [input() for _ in range(N)]
    lookup = set()
    for x in S:
        encode = "".join(D[ord(c)-ord('A')] for c in x)
        if encode in lookup:
            return "YES"
        lookup.add(encode)
    return "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, colliding_encoding()))
