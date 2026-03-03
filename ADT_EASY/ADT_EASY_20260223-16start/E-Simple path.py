# 間違いのコード
n,x,y = map(int,input().split())
guraf = []
for i in range(n-1) :
    u,v = map(int,input().split())
    guraf.append([u,v])
nownum = x
count = 200000
nowcount = 0

for j in range(n-1) :
    if guraf[j][0] == x and guraf[j][1] == y :
        print(x,y)
    elif nownum == y :
        if nowcount < count :
            count = nowcount
        else :
            nowcount = 0
    elif nownum == guraf[j][0] :
        nownum = guraf[j][1]
        nowcount += 1
    elif nownum == guraf[j][1] :
        nownum = guraf[j][0]
        nowcount += 1
    
# 正解のコード
from collections import deque

n, x, y = map(int, input().split())

# 1. グラフを作る（隣接リスト）
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 2. パンくずリスト（親の頂点番号をメモする配列）の準備
# まだ行ってない場所は -1 にしておく
parent = [-1] * (n + 1)

# 探索するための「順番待ちリスト（キュー）」を用意
queue = deque([x])
# スタート地点は自分自身を親にしておく（目印）
parent[x] = x 

# 3. 探索スタート！
while queue:
    # 順番待ちの先頭を取り出す
    now = queue.popleft()
    
    # ゴールに着いたら探索終了！
    if now == y:
        break
        
    # 今いる場所から行ける頂点をすべてチェック
    for next_node in graph[now]:
        # もしそこが「まだ行ったことのない場所(-1)」なら
        if parent[next_node] == -1:
            # 「now から来ました」とパンくずを残す
            parent[next_node] = now
            # 次の探索候補として順番待ちリストに入れる
            queue.append(next_node)

# 4. ゴールからパンくずを辿ってルートを復元する
path = []
now = y
while now != x:
    path.append(now)        # 今の場所をルートに追加
    now = parent[now]       # 親（来た道）へ戻る
path.append(x)              # 最後にスタート地点を追加

# ゴールからスタートへ遡ったので、ひっくり返して出力
path.reverse()
print(*path)
