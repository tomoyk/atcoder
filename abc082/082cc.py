#!/usr/bin/env python

N=int(input())
a=[int(i) for i in input().split()] 
a.sort()
numbers=[int(i) for i in set(a)]
numbers.sort()

# dictの初期化
numbers_count = {}
# for i in numbers:
for i in numbers:
    numbers_count[i] = 0 

# 数値別の集計
for i in a:
    numbers_count[i] += 1

# 取り除く数を算出
remove=0
for i in numbers:
    # 3が2つある
    if(i > numbers_count[i]):
        remove += numbers_count[i]
    # 3が4つある
    elif(i < numbers_count[i]):
        remove += numbers_count[i] - i

print(remove)
