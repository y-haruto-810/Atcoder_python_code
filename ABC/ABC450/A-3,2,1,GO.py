# 正解のコード
n = int(input())
for i in range(n,1,-1) :
    print(i,end=",")
print(1)

# ２行で終わるコード
n = int(input()) # rangeで N から 1 までの数字を作り
print(*range(n, 0, -1), sep=",") # * で中身を展開して、sep="," で間をカンマで埋めて出力する
