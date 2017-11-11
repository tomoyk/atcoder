#!/usr/bin/env pyhton

import math

A,B,C=list( int(i) for i in input().split() )

t=0
before=0
j=1

while(True):
    y=A*t+B*math.sin(C*t*math.pi)

    if( y==100 ):
        print("Matched!!")
        break

    elif( y>=100 ):
        print("Overed!!", "y:", y,"t:",t)
        t=before
        j*=0.1
        t+=j
        continue
        
    t+=j
    before=t

