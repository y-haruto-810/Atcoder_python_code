# チェックが足りずに間違いのコード
w = input()
num = 0
w = list(w)
w.sort()
nowstr = w[0]
for i in w :
    if i == nowstr :
        num += 1
    else :
        if num % 2 == 0 :
            num = 1
            nowstr = i
        else :
            print("No")
            exit()
print("Yes")

# ループが終わった後に一番最後の文字のカウントをチェックする正解のコード
w = input()
w = list(w)
w.sort()
nowstr = w[0]
num = 0
for i in w :
    if i == nowstr :
        num += 1
    else :
        if num % 2 == 0 :
            num = 1
            nowstr = i
        else :
            print("No")
            exit()
if num % 2 != 0 : # ループが終わった後一番最後の文字のカウントを忘れずにチェック
    print("No")
    exit()
print("Yes")

# setとcountを使ったコード
w = input()
for i in set(w): # set(w) で使われている文字の種類だけを取り出す
    if w.count(i) % 2 != 0: # countで元の文字列にその文字が何個あるか数えてくれる
        print("No")
        exit()
print("Yes")

# collectionsとCounterを使ったコード
from collections import Counter
w = input()
count_w = Counter(w) # これだけで{'a':4,'b':2,'c':2}という辞書を作ってくれる
for num in count_w.values(): # 個数(values)だけを取り出してループ
    if num % 2 != 0:
        print("No")
        exit()
print("Yes")
