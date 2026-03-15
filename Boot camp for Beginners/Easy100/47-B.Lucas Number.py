n = int(input())
num = 1
maenum = 2
nownum = 1
while num != n :
    nextnum = maenum + nownum
    maenum = nownum
    nownum = nextnum
    num += 1
print(nownum)
# 約８分半でAC

# 同時代入して計算する方法
n = int(input())
num = 1
maenum = 2
nownum = 1
while num != n : # 右側の計算を全部終わらせてから、左側に同時に代入してくれる
    maenum, nownum = nownum, maenum + nownum
    num += 1
print(nownum)

# listに全部メモしていくコード
n = int(input())
L = [2, 1] # L0 = 2, L1 = 1 を最初からリストに入れておく
for i in range(2, n + 1): # L2 から Ln まで順番に計算してリストの末尾に追加していく
    next_num = L[i-1] + L[i-2]
    L.append(next_num)
print(L[n]) # n番目の数字を出力するだけ
