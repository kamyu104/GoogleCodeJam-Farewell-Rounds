# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round D - Problem C. Hey Google, Drive!
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000caccfa
#
# Time:  O((R * C)^2 * F), pass in PyPy3 but Python3
# Space: O(R * C)
#

from string import ascii_lowercase, ascii_uppercase

def hey_google_drive():
    def bfs():
        lookup = [[False]*C for _ in range(R)]
        lookup[r][c] = True
        q = [(r, c)]
        idx = 0
        while idx < len(q):
            i, j = q[idx]
            if (i+1 < R and not lookup[i+1][j] and curr[i+1][j] == '.' and
                (not i+2 < R or curr[i+2][j] != '*')):
                lookup[i+1][j] = True
                q.append((i+1, j))
            if (j+1 < C and not lookup[i][j+1] and curr[i][j+1] == '.' and
                (not j+2 < C or curr[i][j+2] != '*')):
                lookup[i][j+1] = True
                q.append((i, j+1))
            if (0 <= i-1 and not lookup[i-1][j] and curr[i-1][j] == '.' and
                (not 0 <= i-2 or curr[i-2][j] != '*')):
                lookup[i-1][j] = True
                q.append((i-1, j))
            if (0 <= j-1 and not lookup[i][j-1] and curr[i][j-1] == '.' and
                (not 0 <= j-2 or curr[i][j-2] != '*')):
                lookup[i][j-1] = True
                q.append((i, j-1))
            idx += 1
        return lookup, q

    R, C = list(map(int, input().strip().split()))
    G = [list(input().strip()) for _ in range(R)]
    result = set()
    for r in range(R):
        for c in range(C):
            if not 'A' <= G[r][c] <= 'Z':
                continue
            curr = [[G[i][j] if G[i][j] in '#*' else '.' for j in range(C)] for i in range(R)]
            reachables, new_reachables = [], [(i, j) for i in range(R) for j in range(C) if curr[i][j] not in '#*']
            while len(reachables) != len(new_reachables):
                for i, j in reachables:
                    if not lookup[i][j]:
                        curr[i][j] = '*'
                reachables = new_reachables
                lookup, new_reachables = bfs()
            for i, j in reachables:
                if 'a' <= G[i][j] <= 'z':
                    result.add((G[i][j], G[r][c]))
    return " ".join(c1+c2 for c1 in ascii_lowercase for c2 in ascii_uppercase if (c1, c2) in result) if result else "NONE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, hey_google_drive()))
