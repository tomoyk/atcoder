#!/usr/bin/env pyhton

import math

A,B,C=list( int(i) for i in input().split() )

t=0
before=0
j=1

while(True):
    y=A*t+B*math.sin(C*t*math.pi)
    # print("y:",y)

    if( y==100 ): # FIT
        print("Matched!!")
        break

    elif( y>=100 ): # LARGE
        print("Overed!!", "y:", y,"t:",t,"before:",before,"j:",j)
        j*=0.1
        t=before
        t+=j
        continue

    elif( y<100 ): #SMALL
        print("UnOvered!!")
        before=t
        t+=j
        continue

