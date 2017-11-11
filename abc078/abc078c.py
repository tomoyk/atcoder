#!/usr/bin/env python

N,M=list( int(i) for i in input().split() )

def cal(Num, Sec):
    print("Num, Sec:",Num,Sec)
    return Sec/(2**Num)

Sum=0
for i in range(M):
    Sum+=cal(i+1, 1900)

print(Sum)
