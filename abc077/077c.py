#!/usr/bin/env python

N=int(input())
A=sorted(list( int(i) for i in input().split()))
B=sorted(list( int(i) for i in input().split()))
C=sorted(list( int(i) for i in input().split()))

'''
print(A)
print(B)
print(C)
'''

count=0

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