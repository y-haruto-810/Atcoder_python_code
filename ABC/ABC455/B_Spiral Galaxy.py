# 解法が全く思いつかなかったコード
h,w = map(int,input().split())
num = 0
s_list = [[] for _ in range(h)]
for i in range(h) :
    s = input()
    for j in s :
        s_list[i].append()
        num += 1

# ６重ループで解いたコード
h, w = map(int, input().split())
grid = [] # グリッドの受け取り（文字列のリストとしてそのまま受け取るのが一番ラク）
for _ in range(h):
    grid.append(input())
ans = 0
for h1 in range(h): # 1. すべての長方形の組み合わせを試す（4重ループ）
    for h2 in range(h1, h): # h2はh1以上
        for w1 in range(w):
            for w2 in range(w1, w): # w2はw1以上
                # ここから選ばれた長方形が「点対称」か調べる
                is_symmetric = True
                for i in range(h1, h2 + 1): # 2. 長方形の中のすべてのマス (i, j) を調べる（2重ループ）
                    for j in range(w1, w2 + 1): # 問題文の親切なカンペをそのまま
                        opp_i = h1 + h2 - i
                        opp_j = w1 + w2 - j
                        if grid[i][j] != grid[opp_i][opp_j]: # もし反対側のマスと色が違ったら対称じゃないので失格
                            is_symmetric = False
                            break # 色が違うと分かった瞬間調べるのをやめる（高速化）  
                    if not is_symmetric:
                        break # 外側のループも抜ける
                if is_symmetric: # 最後まで色が違わなかったら対称な長方形
                    ans += 1
print(ans)
