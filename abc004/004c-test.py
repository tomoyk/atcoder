Card=[1,2,3,4,5,6]
i=0
Before=[1,2,3,4,5,6]

while True:
    p = (i%5)
    Card[p], Card[p+1] = Card[p+1], Card[p]
    if(Card == Before):
        print(i)
        break
    i+=1
