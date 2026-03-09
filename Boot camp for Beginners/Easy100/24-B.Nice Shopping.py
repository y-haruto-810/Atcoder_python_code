# 正解のコード
A,B,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
min_kingaku = min(a) + min(b)
for i in range(m) :
    x,y,c = map(int,input().split())
    if min_kingaku > a[x-1] + b[y-1] - c :
        min_kingaku = a[x-1] + b[y-1] - c
print(min_kingaku)
# 約１０分でAC

# よりスマートなコード
A,B,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
min_kingaku = min(a) + min(b)
for i in range(m) :
    x,y,c = map(int,input().split())
    ticket_price = a[x-1] + b[y-1] - c
    min_kingaku = min(min_kingaku, ticket_price)
print(min_kingaku)
