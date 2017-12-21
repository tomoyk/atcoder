#!/usr/bin/env python

n=int(input())
S=[0] * n

charas=[{}] * n

# 入力の選択
for i in range(0, n):
    # 文字の選択とカウント
    for k in input():
        try:
            print("countUp:", "charas["+str(i)+"]["+k+"]")
            charas[i][k] += 1
            # charas[i].update({k:charas[i][k]+1})
        except KeyError:
            print("set", "charas["+str(i)+"]["+k+"]")
            charas[i][k] = 1
            # charas[i].update({k:charas[i][k]+1})

print(charas)

