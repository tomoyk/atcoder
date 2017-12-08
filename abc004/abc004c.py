#!/usr/bin/env python

N=int(input())
Card=[1,2,3,4,5,6]

# Magic
N=N%30

for i in range(0, N):
    p = (i%5)
    # print("p", p)
    Card[p], Card[p+1] = Card[p+1], Card[p]

# print(Card)

for i in range(0, len(Card)):
    print(Card[i], end='')

print()
