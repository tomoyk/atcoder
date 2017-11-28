#!/usr/bin/env python

N=int(input())
A=2
B=1
sum=1

for i in range(0, N-1):
    # print(sum)
    sum=A+B
    A=B
    B=sum

print(sum)
