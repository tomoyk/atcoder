#!/usr/bin/env python

O=input()
E=input()

s=''

for i in range(0, len(E)):
    s+=O[i]+E[i]

if(len(O)!=len(E)):
    s+=O[len(O)-1]

print(s)
