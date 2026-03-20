# 本来２scでは終わらないものの問題が１０scの制限のためACできたコード
h,w = map(int,input().split())
x = []
for i in range(h) :
    xw = list(map(int,input().split()))
    ruikei = [0]
    now = 0
    for j in xw :
        ruikei.append(j+now)
        now = j+now
    x.append(ruikei)
q = int(input())
for _ in range(q) :
    a,b,c,d = map(int,input().split())
    kei = 0
    for k in range(a-1,c) :
        kei += x[k][d] - x[k][b-1]
    print(kei)
# 約３０分でAC

# 完全な２次元累積和のコード
h, w = map(int, input().split())
Z = [[0] * (w + 1)] # 縦の0が w+1 個並んだリストを最初に用意してZとする
for i in range(h):
    xw = list(map(int, input().split()))
    ruikei = [0]
    now = 0
    for j in xw: # 横方向の累積和
        now = j + now
        ruikei.append(now)
    for j in range(w + 1): # 縦方向の累積和を追加
        ruikei[j] += Z[-1][j] # 今作った ruikei に、一つ上の行（Z[-1]）の数字をそれぞれ足す
    Z.append(ruikei) # 完成した行を Z に追加する
q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    kei = Z[c][d] - Z[a-1][d] - Z[c][b-1] + Z[a-1][b-1] # 4つの頂点を使った面積の切り貼り
    print(kei) # 巨大な面積 - 上の切り捨て - 左の切り捨て + えぐれすぎた左上の補修
    