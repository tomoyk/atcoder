#!/usr/bin/env python

N=int(input())
a=[int(i) for i in input().split()] 

a.sort()
numbers=[int(i) for i in set(a)]
numbers.sort()

# print("a", a)
# print("numbers", numbers)

def main():
    label=0 # numbersの添字
    i=0 # aの添字
    err=0 # 削除する要素の数
    while(True):
        # 範囲を超えるパターン
        if(len(numbers) <= label or len(a) <= i):
            # print("Exit")
            return err
        # 最初が一致
        if(a[i]==numbers[label]):
            # 要素数分を確保
            ar=[ numbers[label] ] * numbers[label]
            # ピッタリ一致
            if(a[ i:i+numbers[label] ] == ar):
                # print("[ fit ] i="+str(i))
                # print("a["+str(i)+"]="+str(a[i]))
                i += numbers[label]
                label += 1
            # 最初が一致かつ不完全一致
            else:
                # print("[unfit] i="+str(i))
                for j in range(0, i):
                    try:
                        # 値が不一致(要素)
                        # print("a[i+j]="+str(a[i+j]))
                        # print("numbers[label]="+str(numbers[label]))
                        if(a[i+j]!=numbers[label]):
                            # print("Unmatched: j=", j)
                            i+=j
                            err+=j
                            break
                    except IndexError:
                        err+=j
                        # print("i, j=", i, j)
                        return err
        # 最初が不一致(右に1つずらす)
        else:
            err+=1
            i+=1

if(N==1):
    if(a[0]==1):
        print(0)
    else:
        print(1)
else:
    print(main())

