# 正解のコード
n = int(input())
x = n * (100/108) 
x_check = n * (100/108) // 1
x_tasu = (n+1) * (100/108) // 1
n_set = set()
for i in range(50000) :
    n_set.add(i * 1.08 // 1)
if n not in n_set :
    print(":(")
else :
    if x == int(x) :
        print(int(x))
    else :
        print(int(x_tasu))

# もっと良い全探索のコード
n = int(input())

for x in range(1, 50001): # 税抜価格 X の候補を、1 から 50000 まで全部試す！
    if int(x * 1.08) == n: # 問題文の通り「X * 1.08 の切り捨て」を計算
        print(x)
        exit()  # 見つかったら出力して即終了！

print(":(") # ループを50000まで全部回しても見つからなかったら、存在しないということ
