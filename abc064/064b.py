#!/ust/bin/env python

a=[]
N=int(input())
for i in input().split():
    a.append(int(i))

a.sort()
print(a[-1]-a[0])
