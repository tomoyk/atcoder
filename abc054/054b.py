#!/usr/bin/env python

import sys

N,M=list( int(i) for i in input().split() )
A=[] # large
B=[] # small

for i in range(0, N):
    A.append(input())

for i in range(0, M):
    B.append(input())

'''
print(A)
print(B)
'''

def check(start_x, start_y):
    for i in range(0, M):
        for j in range(0, M):
            # print("checking:","A:", start_x+i, start_y+j, "B:", i, j)
            if( A[start_x+i][start_y+j] != B[i][j] ):
                return False
    return True

for i in range(0, N-M+1):
    for j in range(0, N-M+1):
        # print("calling:", i, j)
        # check(i, j)
        if( check(i, j) ):
            # print("match", i, j)
            print("Yes")
            sys.exit()

print("No")
