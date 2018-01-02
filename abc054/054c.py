#!/usr/bin/env python

N,M=[ int(i) for i in input().split() ]
Relation=[[0 for col in range(N)] for row in range(N)]
for i in range(0, M):
    A,B = [int(i) for i in input().split()]
    Relation[A-1][B-1] += 1
    Relation[B-1][A-1] += 1

# print(Relation)

for i in range(0, N):

