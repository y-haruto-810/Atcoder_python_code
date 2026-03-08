# 正解のコード
n,x = map(int,input().split())
a = list(map(int,input().split()))
kodomo = 0
total = 0
a.sort()
for i in a :
    if i + total < x :
        kodomo += 1
        total += i
    elif i + total == x :
        print(kodomo+1)
        exit()
    else :
        print(kodomo)
        exit()
if x == sum(a) :
    print(n)
else :
    print(n-1)
# 約９分でAC

# より良いコード
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
kodomo = 0
for i in a:
    if x >= i:
        kodomo += 1
        x -= i  # 配った分だけ、持っているお菓子(x)を減らしていく！
    else:
        break # もう配れないならループ終了
if kodomo == n and x > 0: # 全員に配れたのに、まだお菓子(x)が余っていたら1人減らす
    kodomo -= 1
print(kodomo)
