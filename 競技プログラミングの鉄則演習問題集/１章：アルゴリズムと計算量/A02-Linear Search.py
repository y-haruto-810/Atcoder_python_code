# 正解のコード
n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in a :
    if i == x : 
        print("Yes")
        exit()
print("No")
# 約２分でAC

# より短いコード
n, x = map(int, input().split())
a = list(map(int, input().split()))
print("Yes" if x in a else "No") # もしxがaの中(in)にあればYesそうでなければNo
