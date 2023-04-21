# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round D - Problem B. Genetic Sequences
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cadc77
#
# Time:  O((N + M) * log(N + M) + Q * logM * logN), pass in PyPy3 but Python3
# Space: O((N + M) * log(N + M))
#

from random import seed, random
from copy import copy

class TreapNode(object):
    def __init__(self, key):
        self.key = key
        self.prior = random()
        self.left = None
        self.right = None

class PersistentTreap(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __insert(self, x, key):
        if not x:
            return TreapNode(key)
        y = copy(x)
        if key < y.key:
            y.left = self.__insert(y.left, key)
            if y.left.prior < y.prior:
                return self.__rotate_left(y)
        elif y.key < key:
            y.right = self.__insert(y.right, key)
            if y.right.prior < y.prior:
                return self.__rotate_right(y)
        return y

    def __delete(self, x, key):
        y = copy(x)
        if key < y.key:
            y.left = self.__delete(y.left, key)
        elif y.key < key:
            y.right = self.__delete(y.right, key)
        else:
            return self.__delete_node(y)
        return y

    def __delete_node(self, x):
        if x.left and x.right:
            if x.left.prior < x.right.prior:
                x.left = copy(x.left)
                y = self.__rotate_left(x)
                y.right = self.__delete_node(x)
            else:
                x.right = copy(x.right)
                y = self.__rotate_right(x)
                y.left = self.__delete_node(x)
            return y
        return x.right if x.right else x.left

    def __rotate_left(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def __rotate_right(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

def log2_floor(x):  # assumed x >= 1
    return x.bit_length()-1

def log2_ceil(x):  # assumed x >= 1
    return (x-1).bit_length()

# Suffix Array
# Reference:
# - https://cp-algorithms.com/string/suffix-array.html#on-log-n-approach
# - https://github.com/kth-competitive-programming/kactl/blob/main/content/strings/SuffixArray.h
def suffix_array(s):
    def sorted_shifts(s):  # Time: O(nlogn), Space: O(n)
        n = len(s)
        alphabet = 256
        p, c, cnt = [0]*n, [0]*n, [0]*max(alphabet, n)
        for i in range(n):
            cnt[s[i]] += 1
        for i in range(alphabet):
            cnt[i] += cnt[i-1]
        for i in range(n):
            cnt[s[i]] -= 1
            p[cnt[s[i]]] = i
        c[p[0]] = 0
        classes = 1
        for i in range(1, n):
            if s[p[i]] != s[p[i-1]]:
                classes += 1
            c[p[i]] = classes-1
        pn, cn = [0]*n, [0]*n
        for h in range(log2_ceil(n)):
            for i in range(n):
                pn[i] = p[i]-(1<<h)
                if pn[i] < 0:
                    pn[i] += n
            for i in range(classes):
                cnt[i] = 0
            for i in range(n):
                cnt[c[pn[i]]] += 1
            for i in range(1, classes):
                cnt[i] += cnt[i-1]
            for i in reversed(range(n)):
                cnt[c[pn[i]]] -= 1
                p[cnt[c[pn[i]]]] = pn[i]
            cn[p[0]] = 0
            classes = 1
            for i in range(1, n):
                curr = (c[p[i]], c[(p[i]+(1<<h))%n])
                prev = (c[p[i-1]], c[(p[i-1]+(1<<h))%n])
                if curr != prev:
                    classes += 1
                cn[p[i]] = classes-1
            c, cn = cn, c
        return p

    s += '$'
    return sorted_shifts(list(map(ord, s)))[1:]

# Kasai's Algorithm
# Reference:
# - https://cp-algorithms.com/string/suffix-array.html#longest-common-prefix-of-two-substrings-without-additional-memory
# - https://github.com/kth-competitive-programming/kactl/blob/main/content/strings/SuffixArray.h
def lcp_array(s, p):  # Time: O(n), Space:O(n)
    n = len(s)
    rank = [0]*n
    for i in range(n):
        rank[p[i]] = i
    k = 0
    lcp = [0]*(n-1)
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue
        j = p[rank[i]+1]
        while i+k < n and j+k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k:
            k -= 1
    return lcp, rank

# RMQ - Sparse Table
# Reference:
# - https://cp-algorithms.com/data_structures/sparse-table.html#precomputation
# - https://cp-algorithms.com/data_structures/sparse-table.html#range-sum-queries
# - https://github.com/kth-competitive-programming/kactl/blob/main/content/data-structures/RMQ.h
class SparseTable(object):
    def __init__(self, arr):  # Time: O(nlogn), Space: O(nlogn)
        n = len(arr)
        k = log2_floor(n)
        self.st = [[0]*n for _ in range(k+1)]
        self.st[0] = arr[:]
        for i in range(1, k+1):
            for j in range((n-(1<<i))+1):
                self.st[i][j] = min(self.st[i-1][j], self.st[i-1][j+(1<<(i-1))])

    def query(self, L, R):  # Time: O(1)
        i = log2_floor(R-L+1)
        return min(self.st[i][L], self.st[i][R-(1<<i)+1])

def binary_search_right(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return right

def genetic_sequences():
    def check(l):
        def find_neighbors(node, x):
            left = right = None
            while node:
                if x < node.key:
                    right = node.key
                    node = node.left
                else:
                    if x > node.key:
                        left = node.key
                    node = node.right
            return left, right

        i = rank[-S]
        left, right = find_neighbors(versioned_bst[P-l], i)
        return max((rmq_lcp.query(left, i-1) if left is not None else 0), (rmq_lcp.query(i, right-1) if right is not None else 0)) >= l

    A, B, Q = list(input().strip().split())
    Q = int(Q)
    P_S = [list(map(int, input().strip().split())) for _ in range(Q)]
    AB = A+B
    p = suffix_array(AB)
    lcp, rank = lcp_array(AB, p)
    rmq_lcp = SparseTable(lcp)
    pt = PersistentTreap()
    versioned_bst = []
    for i in range(len(A)):
        pt.insert(rank[i])
        versioned_bst.append(pt.root)
    result = [0]*Q
    for i, (P, S) in enumerate(P_S):
        result[i] = binary_search_right(1, min(P, S), check)
    return " ".join(map(str, result))

seed(0)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, genetic_sequences()))
