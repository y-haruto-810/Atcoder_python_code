# 間違いのコード
h,w,n = map(int,input().split())
masu = [0] * (h*w+1) 
for _ in range(n) :
    a,b,c,d = map(int,input().split())
    masu[(a-1)*w+b-1] += 1
    masu[(c-1)*w+d] -= 1
    print(masu[(a-1)*w+b-1],masu[(c-1)*w+d])
mae = 0
ruikei = []
for i in masu[:h*w] :
    ruikei.append(mae+i)
    mae += i
num = 0
for j in range(h*w) :
    num += 1
    if num % w == 0 :
        print(ruikei[j])
    else :
        print(ruikei[j],end=" ")

# 様々な修正をして本来２scでは終わらないものの問題が１０scの制限のためACできたコード
h,w,n = map(int,input().split())
masu = []
for _ in range(h) :
    masu.append([0] * (w+1))
for _ in range(n) :
    a,b,c,d = map(int,input().split())
    for l in range(a-1,c) :
        masu[l][b-1] += 1
        masu[l][d] -= 1
mae = 0
for i in range(h) :
    mae = 0
    for j in masu[i][:w] :
        print(j + mae,end=" ")
        mae = j + mae
    print()

# 4つのカドにメモを置く完全版の2次元いもす法コード
import sys
input = sys.stdin.readline # 10万回の質問が来るので爆速入力は必須
h, w, n = map(int, input().split()) # 1. 魔法の空箱（H+1行、W+1列）を用意する
Z = [[0] * (w + 1) for _ in range(h + 1)] # 外側に-1を置くため、1回り大きく作るのがエラーを防ぐ鉄則
for _ in range(n): # 2. 各質問に対して、4つのカドにメモを置く（ループなしの O(1) ）
    a, b, c, d = map(int, input().split())
    Z[a - 1][b - 1] += 1 # 左上スタート
    Z[a - 1][d] -= 1     # 右上のストップ
    Z[c][b - 1] -= 1     # 左下のストップ
    Z[c][d] += 1         # 右下の補修（引きすぎ防止）
for i in range(h): # 3. マップ全体に累積和をかける（早見表の完成）
    for j in range(1, w): # まずは横方向にドバーッと足す
        Z[i][j] += Z[i][j - 1]
for j in range(w): # 次に縦方向にドバーッと足す
    for i in range(1, h):
        Z[i][j] += Z[i - 1][j]
for i in range(h): # 4. 答えを出力する（はみ出して作ったダミーの壁は出力しない）
    print(*(Z[i][:w])) # Pythonの小技】リストの前に * をつけると、空白区切りで綺麗に出力してくれる
