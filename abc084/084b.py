import re

A,B=[int(i) for i in input().split()]
S=input()

regex = '[0-9]{'+str(A)+'}-[0-9]{'+str(B)+'}'
if( re.compile(regex).match(S) ):
    print("Yes")
else:
    print("No")
    
