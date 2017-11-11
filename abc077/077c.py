#!/usr/bin/env python

import sys

N=int(input())
A=sorted(list( int(i) for i in input().split()))
B=sorted(list( int(i) for i in input().split()))
C=sorted(list( int(i) for i in input().split()))

'''
鏡もちの形状
print(A)
print(B)
print(C)
'''

count=0

width=int(len(A)/2+len(A)%2)
print(width)

def getHalf(num):
    if(num%2==0):
        return int(num/2)
    else:
        return int((num+1)/2)

while(True):
    if(width<=1):
        break

    if(A[i]<=B[getHalf(width)]):
        print("中から右を検索")
        width=width+getHalf(width)
    else:
        print("左から中を検索")
        width=getHalf(width)

sys.exit()

# 
# 全探索
#
for i in range(0, len(A)):
	for j in reversed(range(0, len(B))):
		if(A[i]>=B[j]):
			# print("break:",A[i],B[j])
			break
		for k in reversed(range(0, len(C))):
			# print("count:",count,"A:",A[i],"B:",B[j],"C:",C[k])
			if(B[j]>=C[k]):
				# print("break2:",A[i],B[j],C[k])
				break
			count+=1

print(count)
