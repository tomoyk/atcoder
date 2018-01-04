#!/usr/bin/env python
import sys
A,B,C=[int(i) for i in input().split()]
Total=0

if(A==1):
    print("YES")
    sys.exit()

for i in range(1, 100000):
    if(Total%B==C):
        print("YES")
        sys.exit()
    Total+=A*i

print("NO")
