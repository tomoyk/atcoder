#!/usr/bin/env python

s=input()
t=input()

if(len(s)>len(t)):
    min_len=len(t)
else:
    min_len=len(s)

ss=[]
for num in range(0, len(s)):
    ss.append(s[num])

tt=[]
for num in range(0, len(t)):
    tt.append(t[num])

ss.sort()
tt.sort()
tt.reverse()

if(ss>=tt):
    print("No")
else:
    print("Yes")

# print(ss)
# print(tt)
