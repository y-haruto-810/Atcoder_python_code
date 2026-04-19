# WAになるコード
n = int(input())
l = list(map(int,input().split()))
num = 0
now = 0.5
for i in range(n-1) :
    if l[i] < l[i+1] :
        if now > 0 :
            now += l[i] 
            if now < 0 :
                num += 1
        else :
            now += l[i]
            if now > 0 :
                num += 1
print(num)

# DFS（再帰関数）を用いたコード
import sys
sys.setrecursionlimit(10**6) # Pythonで再帰関数を使う時のおまじない（限界突破）
n = int(input())
l = list(map(int, input().split()))
def dfs(step, now): # dfs(現在のステップ数, 現在の座標) -> その先で0を跨げる「最大回数」を返す関数
    if step == n: # もしN回移動し終わったら、もう跨げないので 0 を返す
        return 0
    # パターン1：プラスの方向に進んでみる
    next_pos_plus = now + l[step]
    # 0を跨いだか判定（符号がひっくり返っていたら跨いだ証拠）
    cross_plus = 1 if (now > 0 and next_pos_plus < 0) or (now < 0 and next_pos_plus > 0) else 0
    # 「今回跨いだ回数」＋「この先で跨げる最大回数（関数を再帰呼び出し）」
    res_plus = cross_plus + dfs(step + 1, next_pos_plus)
    # パターン2：マイナスの方向に進んでみる
    next_pos_minus = now - l[step]
    # 0を跨いだか判定
    cross_minus = 1 if (now > 0 and next_pos_minus < 0) or (now < 0 and next_pos_minus > 0) else 0
    res_minus = cross_minus + dfs(step + 1, next_pos_minus) # 「今回跨いだ回数」＋「この先で跨げる最大回数」
    return max(res_plus, res_minus) # プラスに進んだ未来と、マイナスに進んだ未来、どっちが多かったか勝負して大きい方を返す
print(dfs(0, 0.5)) # 0歩目、座標0.5からスタートした時の最大回数を計算して表示
