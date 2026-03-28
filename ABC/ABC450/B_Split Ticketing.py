# 不正解のコードその１
n = int(input())
C_list = []
for _ in range(n-1) :
    C = list(map(int,input().split()))
    C_list.append(C)
num = 1
for a in range(1,n-1) : 
    for b in range(a+1,n) :
        for c in range(a+2,n+1) :
            if C_list[a-num][c-num] > C_list[a-num][b-num] + C_list[b-num][c-num] :
                print("Yes")
                exit()
            num += 1
print("No")

# 不正解のコードその２
n = int(input())
C_list = []
for _ in range(n-1) :
    C = list(map(int,input().split()))
    C_list.append(C)
for a in range(0,n-2) : 
    for b in range(0,n-3) :
        for c in range(0,n-4) :
            if C_list[a][c] > C_list[a][b] + C_list[a+1][c] :
                print("Yes")
                exit()
print("No")

# 正解のコード
N = int(input())
C_matrix = [[0] * N for _ in range(N)] # N x N の 0 で埋まった 2次元リストを作る
for i in range(N - 1):
    row = list(map(int, input().split()))
    for j_idx, cost in enumerate(row): # enumerateを使ってj_idxとcostを同時に取り出す
        j = i + 1 + j_idx # 出発駅は i 到着駅 j は、出発駅の次(i + 1) から、j_idx 分だけ進んだ駅
        C_matrix[i][j] = cost # 完璧な座標にコストを記録
for a in range(N - 2): # a < b < c になるようにループを組む
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            if C_matrix[a][c] > C_matrix[a][b] + C_matrix[b][c]: # 完全に直感的な数式
                print("Yes")
                exit()
print("No")
