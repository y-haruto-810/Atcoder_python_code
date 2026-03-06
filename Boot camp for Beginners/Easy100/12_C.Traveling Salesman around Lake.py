# 正解のコード
k,n = map(int,input().split())
a = list(map(int,input().split()))
maxkyori = 0
for i in range(-1,n-1) :
    if i == -1 :
        kyori = k - a[i] + a[i+1]
    else :
        kyori = a[i+1] - a[i]
    if maxkyori < kyori :
        maxkyori = kyori
print(k-maxkyori)

# 簡単なコード
k, n = map(int, input().split())
a = list(map(int, input().split())) # 1. 12時をまたぐ隙間を最初からリストに追加する
#（a[-1] は最後の家、a[0] は最初の家）
kyori_list = [k - a[-1] + a[0]]
for i in range(n - 1): # 2. 残りの普通の隙間を全部リストに追加する
    kyori_list.append(a[i+1] - a[i])
print(k - max(kyori_list)) # 3. 1周から「リストの中の最大値」を引く！

# 直線にして計算するコード
k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(a[0] + k) # 魔法の1行：最初の家を「2周目の家」としてリストの最後に付け足す
maxkyori = 0
for i in range(n): # n回ループを回すだけでOK！（例外処理の if 文がいらない）
    kyori = a[i+1] - a[i]  # ただ隣同士を引き算するだけ
    if maxkyori < kyori:
        maxkyori = kyori
print(k - maxkyori)
