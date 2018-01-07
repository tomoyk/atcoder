#!/usr/bin/env python

import sys

S=input()
T=input()

# S'の開始位置
for p in range(len(S)):

    def findStr(k):
        # 文字の照合
        for q in range(len(T)):
            # print("Finding", p, q)
            try:
                # 文字が等しくなく かつ ?でない
                if(S[k+q]!=T[q] and S[k+q]!="?"):
                    # print(S[k+q], "!=", T[q])
                    return False
            except IndexError:
                return False

        # 一致した場合
        # print("p=",p,"q=",q)
        return p
    
    result=findStr(p)
    if(result!=False):
        # 一致した文字列を切り出し
        text=S[p:p+len(T)]
        # 置き換え
        newTxt=S.replace(text, T)
        # 残った?をaに置き換え
        fixTxt=newTxt.replace("?", "a")
        print(fixTxt)
        sys.exit()

print("UNRESTORABLE")

