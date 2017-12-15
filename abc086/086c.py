#!/usr/bin/env python

N,K=[int(i) for i in input().split()]
A=[int(i) for i in input().split()]

# bollの種類
bollTypes=...

bollNumbersCounter=[0] * bollTypes

A.sort()

for boll in A:
    bollNumbersCounter[boll]+=1

print(A)

for i in range(0, max(A)+1):
    print("bollNumbersCounter["+str(i)+"]="+str(bollNumbersCounter[i]))
