# 正解のコード
a,b = map(int,input().split())
num = 0
for (i) in range(a,b+1) :
    i = str(i)
    if i[0] == i[4] :
        if i[1] == i[3] :
            num += 1
print(num)
# 約４分でAC

# 文字列を逆にするスライスを使ったコード
a, b = map(int, input().split())
num = 0
for i in range(a, b + 1):
    s = str(i)
    if s == s[::-1]: # 元の文字列(s)と逆から読んだ文字列(s[::-1])が同じなら回文
        num += 1
print(num)
