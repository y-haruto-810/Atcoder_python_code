# ちょっとヒントを見て正解したコード
n,q = map(int,input().split())
a = list(map(int,input().split()))
ruiseki = []
for i in range(n) :
    if i == 0 :
        ruiseki.append(a[i])
    else :
        ruiseki.append(ruiseki[i-1] + a[i])
for j in range(q) :
    l,r = map(int,input().split())
    if l-2 < 0 :
        print(ruiseki[r-1])
    else :
        print(ruiseki[r-1] - ruiseki[l-2])
        
# 先頭に０を置いて条件分岐をせずにわかりやすいコード
n, q = map(int, input().split())
a = list(map(int, input().split()))
ruiseki = [0] # 最初から「0日目の合計は0人」というダミーを入れておく
for i in range(n): # 累積和を作る（aの中身をどんどん足していく）
    ruiseki.append(ruiseki[-1] + a[i]) # ruisekiの末尾の数字に今日のa[i]を足して追加する
for j in range(q):
    l, r = map(int, input().split()) # ダミーの0を入れたのでインデックスが問題文(1スタート)と一致する
    print(ruiseki[r] - ruiseki[l-1])
