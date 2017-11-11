#!/usr/bin/env python

S=input()

center=int(len(S)/2-1)

while(True):
    s1=S[0:center]
    s2=S[center:center+center]
    # print("debug","s1:",s1,"s2:",s2)
    if(s1==s2):
        print(len(s1)*2)
        break
    center-=1
