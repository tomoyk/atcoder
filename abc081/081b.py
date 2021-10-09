N = int(input())
An = map(int, input().split())

min_shift = 0

for i,A in enumerate(An):
    # print("==", A)
    if A % 2 == 1:
        if i == 0:
            min_shift = 0
            break
        continue

    if (A >> min_shift) % 2 == 0 and i !=0 :
        continue

    i = 0
    while (A >> i) % 2 == 0 and (A >> i) > 1:
        # print("A>>i=", A >> i)
        # print(f"i={i}")
        i+=1
    min_shift = i
    # print(i)

print(min_shift)
