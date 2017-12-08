#!/usr/bin/env python

N=int(input())
Num=[0]*4
A=N//1000
B=N//100%10
C=N//10%10
D=N%10

'''
for i in range(0, len(Num)):
    print(Num[i])
'''

Num.sort()
mul=[-1,1]

def ope(sym):
    if(sym==-1):
        return "-" 
    elif(sym==1):
        return "+"

def cal():
    for j in mul:
        for k in mul:
            for m in mul:
                if( A + B*j + C*k + D*m == 7 ):
                    # print("j, k, m", j, k, m)
                    print(str(A)+ope(j)+str(B)+ope(k)+str(C)+ope(m)+str(D)+"=7")
                    return

cal()

