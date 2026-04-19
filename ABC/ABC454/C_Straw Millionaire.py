# TLEになるコード
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ab_list = []
a_set = set()
b_set = set()
item = set()
if 1 not in b_set :
        b_set.add(1)
for i in range(m) :
    a,b = map(int,input().split())
    a_set.add(a)
    b_set.add(b)
    ab_list.append((a,b))
item.add(1)
for _ in range(300000) :
    for j in ab_list :
        if j[0] in item :
            item.add(j[1])
    if item == b_set :
        print(len(item))
        exit()
print(len(item))

# ディクショナリを使ってしようとしたけどできなかったコード
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
item = set()
mae = set()
now = set()
ab_dict = dict()
for i in range(m) :
    a,b = map(int,input().split())
    if a not in ab_dict.keys() :
        ab_dict[a] = set(b)
    else :
        ab_dict[a].add(b)
mae.add(1)
for _ in range(300000) :
    for j in mae :
        if j in ab_dict :
            for k in ab_dict[j] :
                item.add(k)
                now.add(k)
    now -= item
    if len(now) == 0 :
        print(len(item))
        exit()
    mae = now 
    now = set()
print(len(item))

# dequeを使ったコード
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# 1. 隣接リストを作る（辞書よりも爆速で安全）
graph = [[] for _ in range(n + 1)] # [ [], [], [], ... ] という空のリストをN+1個用意する
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # アイテムa から アイテムb へ行けるよとメモ
# 2. 探索の準備
visited = set()   # ゲットしたアイテムを記録（あなたのコードの item）
visited.add(1)    # 最初はアイテム1を持っている
queue = deque([1]) # mae と now を合体させたような超便利ツール
# 3. 探索開始（待ち行列が空になるまで繰り返す）
while queue:
    current = queue.popleft() # 待ち行列の先頭から、調べるアイテムを1つ取り出す
    for next_item in graph[current]: # そのアイテムから交換できる先のアイテムをすべて見る
        if next_item not in visited: # もし、まだゲットしたことのないアイテムだったら
            visited.add(next_item)  # ゲットした記録に追加
            queue.append(next_item) # 次の探索候補として待ち行列の最後尾に並ばせる
print(len(visited)) # 最終的にゲットできたアイテムの種類数を出力
