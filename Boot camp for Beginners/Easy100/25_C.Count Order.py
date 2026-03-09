# 間違いのコード
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
p.reverse()
q.reverse()
sa = 0
if p == q :
    print(0)
    exit()
for i in range(n) :
    if i == 7 :
        sa += (q[i]-p[i]) * 5040
    if i == 6 :
        sa += (q[i]-p[i]) * 720
    if i == 5 :
        sa += (q[i]-p[i]) * 120
    if i == 4 :
        sa += (q[i]-p[i]) * 24
    if i == 3 :
        sa += (q[i]-p[i]) * 6
    if i == 2 :
        sa += (q[i]-p[i]) * 2
    if i == 1 :
        sa += (q[i]-p[i]) * 1
    if i == 0 :
        sa += (q[i]-p[i]) * 0
print(sa)

# 間違いのコードを完成させたもの
import math
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
def get_order(arr): # 「配列が辞書順で何番目か」を計算する専用の関数
    available = list(range(1, n + 1)) # 最初はまだ使ってない数字リストを用意
    order = 0
    for i in range(n): # 左から順番に見ていく
        idx = available.index(arr[i]) # 残っている数字の中で何番目かを取得
        order += idx * math.factorial(n - 1 - i) # インデックス×(残りの桁数の階乗)を足す
        available.pop(idx) # 使った数字は「もう使えない」のでリストから削除
    return order
ans = abs(get_order(p) - get_order(q))
print(ans) # Pの順番とQの順番を計算して、その差の絶対値(abs)を出力

# intertoolsを使ったコード
import itertools
n = int(input())
p = tuple(map(int, input().split())) # itertoolsが作るデータは
q = tuple(map(int, input().split())) # タプルなのでPとQもタプルにする
base = range(1, n + 1) # 1からNまでの数字を作る (例: n=3 なら [1, 2, 3])
# base を渡すだけで、辞書順の全パターンを自動生成してくれる
# list() で囲むことで、検索しやすいリスト型に変換する
all_perms = list(itertools.permutations(base))
a = all_perms.index(p) # PとQが、全パターンの中でインデックス何番目かを検索
b = all_perms.index(q)
print(abs(a - b)) # 差の絶対値を出力して終了
