#!/usr/bin/env python

a,b,x=list( int(i) for i in input().split() )
count=0

if(a==b):
    if(a%x==0):
        print(1)
    else:
        print(0)
else:
    if(a%x==0):
        p=1
    else:
        p=0
    # print("a:", a, "b:", b, "x:", x, "p:", p)
    print(b//x-a//x+p)

