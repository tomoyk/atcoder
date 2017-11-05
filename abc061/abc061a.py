#!/usr/bin/env python

A,B,C=list( int(i) for i in input().split() )

if(A<=C and C<=B):
    print("Yes")
else:
    print("No")
