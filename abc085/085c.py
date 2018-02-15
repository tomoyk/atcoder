#!/usr/bin/env python
import sys

N,Y=[int(i) for i in input().split()]

Fukuzawa = Y // 10000
Higuchi = Y % 10000 // 5000
Noguchi = Y % 10000 % 5000 // 1000
total = Noguchi + Higuchi + Fukuzawa

if(total == N):
    print(str(Fukuzawa)+" "+str(Higuchi)+" "+str(Noguchi))
    sys.exit()
elif(total > N):
    print("-1 -1 -1")
    sys.exit()
#elif(Y//10000 + Y//5000 + Y//1000 > N):
#    print("-1 -1 -1")
#    sys.exit()

for i in range(Y//10000 + 1):
    for j in range(Y//5000 + 1):
        if(i+j>N):
            break
        for k in range(Y//1000 + 1):
            # print(i, j, k)
            if(i+j+k>N):
                break
            if(i*10000 + j*5000 + k*1000 > Y):
                break
            if(i*10000 + j*5000 + k*1000 == Y and i+j+k==N):
                print(i, j, k)
                sys.exit()

