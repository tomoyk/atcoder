#!/usr/bin/env python

N=int(input())
a=[int(i) for i in input().split()] 

a.sort()
aa=[int(i) for i in set(a)]

print("a", a)
print("aa", aa)

head=0
err=0
for i in aa:
    ar=[i] * i
    if(a[head:head+i] == ar):
        print("fit-i:",i)
        head+=i
    else:
        print("unfit-i:",i)
        try:
            for j in range(0, i):
                if(a[head+j]!=i):
                    head+=j
                    err+=i-j
                    break
        except(e):
            
    if(i>len(a)):
        break

print(head)
print(err)

'''
def func(n):
    for i in range(0, n):
       if(a[base+i]!=n):
           return i

key=0
base=0
while(True):
    num=aa[key] 
    ar=[num] * num

    if(a[base:base+num]==ar[0:num]):
        print("ok")
    else:
        print("unok")
        num=func(num)

    if(len(a)==base+num):
        print("correct", 0)
        break

    base+=num

    if(len(a)<=key):
        key+=1
    else:
        print("fail", len(a)-base)
        break
'''
