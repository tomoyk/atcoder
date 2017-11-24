#!/usr/bin/env python

H,W=list( int(i) for i in input().split() )
a=[]
for i in range(0, H):
    a.append(input())

def line():
    for i in range(0, W+2):
        print("#", end="")
    print()

line()

for i in range(0, H):
    print("#"+a[i]+"#")

line()
