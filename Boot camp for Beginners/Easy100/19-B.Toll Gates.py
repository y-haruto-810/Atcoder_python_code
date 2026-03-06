# 正解のコード
n,m,x = map(int,input().split())
a = list(map(int,input().split()))
cost = 0
left = 0 
right = 0
for i in a :
    if i < x :
        left += 1
    else :
        right += 1
print(min(left,right))
# 約８分半でAC

# ジェネレータ式のコード
n, m, x = map(int, input().split())
a = list(map(int, input().split()))
left = sum(i < x for i in a) # 「xより小さいか？」の判定(0or1)をそのまま足し算する！
right = sum(i > x for i in a)
print(min(left, right))
