#!/usr/bin/env python

N=int(input())

if(int(N*0.1)%111==0 or N%1000%111==0):
    print("Yes")
else:
    print("No")
