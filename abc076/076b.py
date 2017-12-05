#!/usr/bin/env python

D=1
N=int(input())
K=int(input())

for i in range(0, N):
    if(D+K > D*2):
        D*=2
    else:
        D+=K

print(D)
