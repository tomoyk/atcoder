#!/usr/bin/env python

# 入力
N,M=[int(i) for i in input().split()]

# 友達を保持するリストを作成
Friends=[[0 for col in range(N)] for row in range(N)]

# 友達の記録
for i in range(0, M):
    A,B=[int(i) for i in input().split()]
    Friends[A-1][B-1] += 1
    Friends[B-1][A-1] += 1

# print(Friends)

# 友達の友達を探索
for keyA,valA in enumerate(Friends):
    totalFF = set([])
    # 友達を選択
    for keyB,valB in enumerate(valA):
        # print("ユーザ"+str(keyA)+"の友達"+str(keyB))
        # 自分自身を除く
        if(keyA==keyB):
            continue

        # 友達関係である場合
        if(valB >= 1):
            # 友達の友達を探索
            for keyC,valC in enumerate(Friends[keyB]):
                # print("友達の友達"+str(keyC)+"="+str(valC))
                # BとCは友達 and 人C!=人B and 人C!=人A and AとCが友達でない
                if(valC >= 1 and keyC!=keyB and keyC!=keyA and Friends[keyA][keyC] < 1):
                    # print("__Friend__")
                    totalFF.add(keyC)
    print(len(totalFF))
