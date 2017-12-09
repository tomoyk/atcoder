#!/usr/bin/env python

import sys

N=int(input())
A=sorted(list( int(i) for i in input().split() ))
B=sorted(list( int(i) for i in input().split() ))
C=sorted(list( int(i) for i in input().split() ))

print(A)
print(B)
print(C)

#
# Finding Min
#
def findMin():
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            if(A[i]>=B[j]):
                break

            for k in range(0, len(C)):
                print("A:",A[i],"B:",B[j],"C:",C[k])
                if(B[j]>=C[k]):
                    continue

                print("i",i,"j",j,"k",k)
                return

print("FindMin() ---")
findMin()

#
# Finding Max
#
def findMax():
    for i in reversed(range(0, len(A))):
        for j in reversed(range(0, len(B))):
            if(A[i]>=B[j]):
                break

            for k in reversed(range(0, len(C))):
                print("A:",A[i],"B:",B[j],"C:",C[k])
                if(B[j]<C[k]):
                    continue
                elif(B[j]>=C[k]):
                    print("i",i,"j",j,"k",k+1)
                    return

    print("i",i,"j",j,"k",k)
    return 

print("FindMax() ---")
findMax()
