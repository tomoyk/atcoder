#!/usr/bin/env python

a,b,x=list( int(i) for i in input().split() )
count=0

# 最初に割り切れる数を特定
for i in range(a,b+1):
    if(i%x==0):
        break

print(b/x,x/a)
