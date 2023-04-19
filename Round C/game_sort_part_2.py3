# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round C - Problem E. Game Sort: Part 2
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cad339
#
# Time:  O(N)
# Space: O(N), more space but faster
#

def game_sort_part_2():
    def P_N():
        i = next((i for i in range(len(S)-1) if S[i] > S[i+1]), -1)
        return list(S) if i != -1 else []

    def P_2():
        left = [(S[0], 1)]
        for i in range(1, len(S)):
            if S[i] < left[-1][0]:
                left.append((S[i], 1))
            elif S[i] == left[-1][0]:
                left.append((left[-1][0], left[-1][1]+1))
            else:
                left.append(left[-1])
        right = [(S[-1], 1)]
        for i in reversed(range(len(S)-1)):
            if S[i] > right[-1][0]:
                right.append((S[i], 1))
            elif  S[i] == right[-1][0]:
                right.append((right[-1][0], right[-1][1]+1))
            else:
                right.append(right[-1])
        right.reverse()
        for i in range(len(S)-1):
            if left[i][0] > right[i+1][0] or (left[i][0] == right[i+1][0] and (left[i][1] > right[i+1][1] or left[i][1] != i+1)):
                return [S[:i+1], S[i+1:]]
        return []

    def P_3():
        if S[0] >= S[-1]:
            return [S[:1], S[1:-1], S[-1:]]
        i = min(range(len(S)-1), key=lambda x: S[x])
        if i != 0:
            return [S[:i], S[i:i+1], S[i+1:]]
        i = next((i for i in range(2, len(S)-1) if S[i] == S[0]), -1)
        if i != -1:
            return [S[:i], S[i:i+1], S[i+1:]]
        i = max(reversed(range(1, len(S))), key=lambda x: S[x])
        if i != len(S)-1:
            return [S[:i], S[i:i+1], S[i+1:]]
        total, l = 1, 0
        for i in reversed(range(len(S)-1)):
            if S[i] == S[-1]:
                l += 1
                continue
            if l > total:
                return [S[:i+1], S[i+1:(i+l)+1], S[(i+l)+1:]]
            total += l
            l = 0
        return []

    def P_others():
        i = next((i for i in range(len(S)-1) if S[i] > S[i+1]), -1)
        mid = []
        if i != -1:
            mid = [S[i], S[i+1]]
            j = i+2
        else:
            i = next((i for i in range(len(S)-2) if S[i] == S[i+2]), -1)
            if i != -1:
                mid = [S[i]*2, S[i]]
                j = i+3
        result = []
        if i != -1:
            left = min(i, (P-len(mid))-int(j != len(S)))
            right = min(len(S)-j, (P-len(mid))-left)
            for k in range(left):
                result.append(S[k] if k != left-1 else S[k:i])
            for x in mid:
                result.append(x)
            for k in range(j, j+right):
                result.append(S[k] if k != (j+right)-1 else S[k:])
        return result

    P, S = list(input().strip().split())
    P = int(P)
    result = P_N() if P == len(S) else P_2() if P == 2 else P_3() if P == 3 else P_others()
    return  "POSSIBLE\n%s" % " ".join(result) if result else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, game_sort_part_2()))
