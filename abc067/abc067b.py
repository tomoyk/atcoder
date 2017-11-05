#!/usr/bin/env python

N,K=list( int(i) for i in input().split() )
l=list( int(i) for i in input().split() )

l.sort()
l.reverse()

N=0
for i in range(0,K):
    N+=l[i]

print(N)
    
