# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round B - Problem B. Intruder Outsmarting
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad13d
#
# Time:  O(W * log(min(D, N)))
# Space: O(1)
#

# reference: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
def extended_gcd(a, b, c):  # Time: O(log(min(a, b)))
    g, ng = a, b
    x, nx = 1, 0
    y, ny = 0, 1
    while ng:
        q = g//ng
        g, ng = ng, g-q*ng
        x, nx = nx, x-q*nx
        y, ny = ny, y-q*ny
    if c%g:
        return 0, 0, 0  # no valid solution
    x *= c//g
    y *= c//g
    assert(a*x+b*y == c)
    return g, x, y  # return (gcd, x, y) s.t. ax + by = c

def intruder_outsmarting():
    def dist(xi, xj):
        # find min x s.t.
        # - (xi+Dx)%N = xj%N => Dx+Ny = xj-xi
        # - (xi-Dx)%N = xj%N => -Dx+Ny = xj-xi => D(-x)+Ny = xj-xi
        g, x, _ = extended_gcd(D, N, xj-xi)
        return min(x%(N//g), -x%(N//g)) if g else float("inf")

    W, N, D = list(map(int, input().strip().split()))
    X = list(map(int, input().strip().split()))
    result = sum(dist(X[i], X[~i]) for i in range(W//2))
    return result if result != float("inf") else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, intruder_outsmarting()))
