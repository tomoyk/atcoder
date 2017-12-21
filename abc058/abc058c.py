#!/usr/bin/env python

n=int(input())
min_charas={}

# 入力の選択
for i in range(0, n):
    charas={}
    # 文字の選択とカウント
    for k in input():
        try:
            charas[k] += 1
        except KeyError:
            charas[k] = 1
    
    # 文字の最小数をカウント
    if(i==0):
        # 最初のみ最小文字数カウンタをそのまま代入
        min_charas = charas
    else:
        # 最低文字数カウンタより出現頻度が低い入力文字列を記録
        for j in min_charas:
            try:
                if(min_charas[j] > charas[j]):
                    min_charas[j] = charas[j]
            except KeyError:
                # print("Key", j)
                min_charas[j] = 0
                continue
    
    # print(charas)

# print(min_charas)

for i in sorted(min_charas):
    for j in range(0, min_charas[i]):
        print(i, end='')
print()
