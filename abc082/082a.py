#!/usr/bin/env python

a,b=[int(i) for i in input().split()]

val=(a+b)/2

if(val*10%10>=5):
    print(int(val)+1)
else:
    print(int(val))
