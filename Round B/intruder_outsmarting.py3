# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round B - Problem B. Intruder Outsmarting
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad13d
#
# Time:  O(W * log(min(D, N)))
# Space: O(1)
#

# Reference: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
def extended_gcd(a, b, c):  # Time: O(log(min(a, b)))
    x, nx = 1, 0
    y, ny = 0, 1
    while b:
        q = a//b
        a,  b =  b, a-q*b
        x, nx = nx, x-q*nx
        y, ny = ny, y-q*ny
    if c%a:
        return 0, 0, 0
    return a, x*(c//a), y*(c//a)

def intruder_outsmarting():
    def dist(xi, xj):
        g, x1, _ = extended_gcd(D, N, xj-xi)  # (xi+Dx)%N = xj%N => Dx+Ny = xj-xi
        _, x2, _ = extended_gcd(-D, N, xj-xi)  # (xi-Dx)%N = xj%N => -Dx+Ny = xj-xi
        return min(x1%(N//g), x2%(N//g)) if g else -1

    W, N, D = list(map(int, input().strip().split()))
    X = list(map(int, input().strip().split()))
    result = 0
    for i in range(W//2):
        d = dist(X[i], X[~i])
        if d == -1:
            return "IMPOSSIBLE"
        result += d
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, intruder_outsmarting()))
