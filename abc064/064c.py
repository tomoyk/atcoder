#!/usr/bin/env python

base=0
counter=0
min_counter=0
scores=[3200, 2800, 2400, 2000, 1600, 1200, 800, 400, 1]
N=int(input())
a=[ int(i) for i in input().split() ]
a.sort()

for i in range(1, len(scores)):
    for j in range(0, N):
        if(scores[i-1]>a[j] and a[j]>=scores[i]):
            # print("scores[i]", scores[i], "a[j]", a[j])
            counter+=1
            break;

for i in range(0, len(a)):
    if(a[i]>=3200):
        min_counter+=1

if(len(set(a))==1 and a[0]>=3200):
    base+=1

print(base+counter, counter+min_counter)
