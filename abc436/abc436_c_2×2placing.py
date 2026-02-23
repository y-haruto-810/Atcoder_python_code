# 間違いのコードその１
n,m = map(int,input().split())
r_c_list = [list(map(int,input().split())) for i in range(2)]
mas = [[0]*n]*n
num = 0 
for j in range(m) :
    if mas[r_c_list[j][0]-1][r_c_list[j][1]-1] and mas[r_c_list[j][0]][r_c_list[j][1]-1] and mas[r_c_list[j][0]-1][r_c_list[j][1]] and mas[r_c_list[j][0]][r_c_list[j][1]] == 0 :
        num+=4
print(num)

# 間違いのコードその２
n,m = map(int,input().split())
block = [[0]*n for _ in range(n)]
num = 0
for i in range(1,m+1) :
    r,c = map(int,input().split())
    if block[r-1][c-1] == block[r-1][c] == block[r][c-1] == block[r][c] == 0 :
        block[r-1][c-1] = 1
        block[r-1][c] = 1
        block[r][c-1] = 1
        block[r][c] = 1
        num += 1
print(num)

# 正解のコード
n,m = map(int,input().split())
block = set()
num = 0
for i in range(1,m+1) :
    r,c = map(int,input().split())
    if ((r,c) not in block and (r,c+1) not in block and (r+1,c) not in block and (r+1,c+1) not in block) :
        block.add((r,c)) 
        block.add((r,c+1)) 
        block.add((r+1,c)) 
        block.add((r+1,c+1)) 
        num += 1
print(num)
