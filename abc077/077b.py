#!/usr/bin/env ptyhon

import math

num=int(input())

for i in reversed(range(1, num+1)):
    rev=math.sqrt(i)
    # print(i,rev,int(rev))
    if( rev-int(rev) == 0 ):
        print(i)
        break
