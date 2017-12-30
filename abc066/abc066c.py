#!/usr/bin/env python

n=int(input())
a=[int(i) for i in input().split()]

def cal(p):
    if(p==1 or p==2):
        lst=reversed(list(enumerate(a)))
    else:
        lst=list(enumerate(a))
    for k,v in lst:
        if(k%2==(p%2)):
            print(str(v)+" ", end="")

if(n%2==1):
    cal(2)
    cal(1)
    print()
else:
    cal(1)
    cal(0)
    print()
