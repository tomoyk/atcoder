#!/usr/bin/env python

N=input()
sum=0

for i in range(0, len(N)):
    sum+=int(N[i])

if(int(N)%sum==0):
    print("Yes")
else:
    print("No")
