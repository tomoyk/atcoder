N,A,B=[int(i) for i in input().split()]
sum=0

def getTotal(num):
    tmp=0
    for s in str(num):
        tmp+=int(s)
    return tmp

for i in range(1, N+1):
    total=getTotal(i)
    if(A<=total and total<=B):
        sum+=i

print(sum)
