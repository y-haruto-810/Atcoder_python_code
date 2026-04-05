# 試行錯誤してACしたコード
import bisect
n = int(input())
a = list(map(int, input().split()))
a_sort = a.copy()
a_sort.sort()
junban = []
rank = [0]* n
b = [0] * n
for i in a:
    junban.append(bisect.bisect_left(a_sort,i))
mae = 0
num = 0
for j in range(n) :
    if a_sort[j] > mae :
        num += 1
        mae = a_sort[j]
    rank[j] = num
for k in range(n) :
    b[k] = rank[junban[k]]
print(*b)

# bisectを使った短いコード
import bisect
n = int(input())
a = list(map(int, input().split()))
rank_table = list(set(a))# ステップ1: 重複を消してソートした「完璧な順位表」を作る
rank_table.sort()# setで重複を消してからリストに戻し、ソートする
b = []
for num in a: # ステップ2 & 3: 元の配列の数字が、順位表の何番目かを探す
    idx = bisect.bisect_left(rank_table, num)# rank_tableはソート済みなので、bisectが完璧に機能する
    b.append(idx + 1) # 0番目スタートなので、+1 すると「〇位」になる
print(*b)


# 辞書を使った短いコード
n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(list(set(a))) # ① 重複を消してソートする（綺麗な順位表のベース）
rank_dict = {} # ② 【第8章の魔法】辞書(Map)を作って、「数字: 順位」を直接登録する
for i in range(len(a_sorted)):
    num = a_sorted[i]
    rank_dict[num] = i + 1  # 例： {46: 1, 80: 2, 89: 3} のようなメモ帳ができる
b = [] # ③ 元の配列を前から見て、辞書から順位を直接引いてくる
for num in a:
    b.append(rank_dict[num])
print(*b)
