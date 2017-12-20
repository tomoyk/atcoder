#!/usr/bin/env python

N=int(input())
a=[int(i) for i in input().split()] 

a.sort()
numbers=[int(i) for i in set(a)]
numbers.sort()

print("a", a)
print("numbers", numbers)

def main():
    label=0 # numbersの添字
    i=0 # aの添字
    err=0 # 削除する要素の数
    while(True):
        # 範囲を超えるパターン
        if(len(numbers) < label):
        # if(i>len(a)):
            print("Exit")
            return err
        # 最初が一致
        if(a[i]==numbers[label]):
            # 要素数分を確保
            ar=[ numbers[label] ] * numbers[label]
            # ピッタリ一致
            if(a[ i:i+numbers[label] ] == ar):
                print("fit-i:",i)
                i += numbers[label]
                label += 1
            # 最初が一致かつ不完全一致
            else:
                print("unfit-i:",i)
                for j in range(0, i):
                    try:
                        # 値が不一致(要素)
                        if(a[i+j]!=i):
                            print("Unmatched: j=", j)
                            i+=j
                            err+=i-j
                            break
                    except IndexError:
                        err+=i-j
                        break
        # 最初が不一致(右に1つずらす)
        else:
            err+=1
            i+=1

print(main())

