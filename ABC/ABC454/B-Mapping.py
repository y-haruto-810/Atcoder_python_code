# 正解のコード
n,m = map(int,input().split())
f = list(map(int,input().split()))
n_set = set()
flag = False
for i in f :
    if i in n_set :
        flag = True
    n_set.add(i)
if flag :
    print("No")
else :
    print("Yes")
for j in range(1,m+1) :
    if j not in n_set :
        print("No")
        exit()
print("Yes")

# for文を使わないコード
n, m = map(int, input().split())
f = list(map(int, input().split()))
unique_f = set(f) # fをsetに変換して、重複を取り除いた種類だけにする
# 質問1: 全員異なる服を着ているか？
if len(f) == len(unique_f): # 元のリストの長さと重複を消した後のセットの長さが同じなら誰も被っていない
    print("Yes")
else:
    print("No")
# 質問2: 1〜Mの服がすべて着られているか？
if len(unique_f) == m: # 問題文の制約で服は「1〜M」しか登場しないので
    print("Yes")
else: # 着られている服の種類数（セットの長さ）が M と完全に一致すればOK
    print("No")
    