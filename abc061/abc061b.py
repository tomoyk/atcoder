#!/usr/bin/env python

N,M=list( int(i) for i in input().split() )
counter=[0]*N

for i in range(0, M):
    a,b=list( int(i) for i in input().split() )
    counter[a-1]+=1
    counter[b-1]+=1

for i in range(0, N):
    print(counter[i])
