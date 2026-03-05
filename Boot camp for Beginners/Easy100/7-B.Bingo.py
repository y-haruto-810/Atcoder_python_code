# 正解のコード
a11,a12,a13 = map(int,input().split())
a21,a22,a23 = map(int,input().split())
a31,a32,a33 = map(int,input().split())
a = [a11,a12,a13,a21,a22,a23,a31,a32,a33]
n = int(input())
for _ in range(n) :
    b = int(input())
    if b in a :
        for i in range(9) :
            if b == a[i] :
                a[i] = 0
if a[0] == 0 and a[1] == 0 and a[2] == 0 or a[3] == 0 and a[4] == 0 and a[5] == 0 or a[6] == 0 and a[7] == 0 and a[8] == 0 \
    or a[0] == 0 and a[3] == 0 and a[6] == 0 or a[1] == 0 and a[4] == 0 and a[7] == 0 or a[2] == 0 and a[5] == 0 and a[8] == 0 \
    or a[0] == 0 and a[4] == 0 and a[8] == 0 or a[2] == 0 and a[4] == 0 and a[6] == 0 :
    print("Yes")
else :
    print("No")
# 約１３分でAC

# ２次元配列を使ったより高レベルな問題にも対応できるコード

a = [list(map(int, input().split())) for _ in range(3)]
# 1. 盤面を 3x3 の2次元配列として一気に受け取る（これが超便利！）
n = int(input())
for _ in range(n):
    b = int(input())
    # 盤面全体を探して、あったら 0 にする
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = 0

bingo = False

# 2. タテとヨコの判定（ループでスッキリ！）
for i in range(3):
    # ヨコが全部0か？（a[i][0], a[i][1], a[i][2]）
    if a[i][0] == 0 and a[i][1] == 0 and a[i][2] == 0:
        bingo = True
    # タテが全部0か？（a[0][i], a[1][i], a[2][i]）
    if a[0][i] == 0 and a[1][i] == 0 and a[2][i] == 0:
        bingo = True

# 3. ナナメの判定（ここは2パターンだけなので手書き）
if a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
    bingo = True
if a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")
