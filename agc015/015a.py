#!/ust/bin/env python

N,A,B=[int(i) for i in input().split()]

def main():
    if(A>B):
        print(0)
        return
    elif(A==B):
        print(1)
        return

    ### A<B
    Max=(A+B)+(N-2)*B
    Min=(A+B)+(N-2)*A

    if(N==1):
        print(0)
    elif(N==2):
        print((B+B)-(A+A)+1)
    elif(Max-Min+1<=0):
        print(0)
    else:
        print(Max-Min+1)

main()
