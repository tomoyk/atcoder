#!/usr/bin/env python

C0=input().split()
C1=input().split()
C2=input().split()
C3=input().split()

'''
C[0]=input().split()
C[1]=input().split()
C[2]=input().split()
C[3]=input().split()
'''

for i in reversed(range(0, 4)):
    for j in reversed(range(0, 4)):
        print(eval("C"+str(i)+"["+str(j)+"]"), end='')
        if(j!=0):
            print(" ", end='')
    print()
