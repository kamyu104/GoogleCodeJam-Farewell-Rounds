# Copyright (c) 2023 kamyu. All rights reserved.
#
# Google Code Jam Farewell Round A - Problem D. ASCII Art
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad9c2
#
# Time:  O(1)
# Space: O(1)
#

def ascii_art():
    N = int(input().strip())
    i = int((-1+(1+8*((N-1)//26))**0.5)/2)   # find max i s.t. (N-1)-26*(i+1)*i//2 >= 0 => find max i s.t. (N-1)//26-(i+1)*i//2 >= 0
    return chr(ord('A')+((N-1)-26*(i+1)*i//2)//(i+1))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, ascii_art()))
