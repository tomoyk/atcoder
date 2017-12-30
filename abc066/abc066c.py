#!/usr/bin/env python

n=int(input())
a=[int(i) for i in input().split()]
b=[]

for i in a:
    b.append(i)
    b.reverse()

for k,v in enumerate(b):
    print(v, end="")
    if(k!=len(b)-1):
        print(" ", end="")
    else:
        print()
