#!/usr/bin/env python

x,y=list( int(i) for i in input().split() )

g1=[1,3,5,7,8,10,12]
g2=[4,6,9,11]

def getGroup(num):
    if(num==2):
        return 3;
    for i in g2:
        if(i==num):
            return 2;
    return 1;

if(getGroup(x)==getGroup(y)):
    print("Yes")
else:
    print("No")
