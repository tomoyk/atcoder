#!/usr/bin/env python

n=int(input())
a=[int(i) for i in input().split()]

def cal(p, rev):
    if(rev):
        lst=reversed(list(enumerate(a)))
    else:
        lst=list(enumerate(a))
    for k,v in lst:
        if(k%2==p):
            print(str(v)+" ", end="")

if(n%2==1):
    cal(0, True)
    cal(1, False)
    print()
else:
    cal(1, True)
    cal(0, False)
    print()
