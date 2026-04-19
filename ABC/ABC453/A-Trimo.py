# 正解のコード
n = int(input())
s = input()
num = 0
for i in s :
    if i == "o" :
        num += 1
    else :
        print(s[num:])
        exit()

# lstripを使ったコード
n = int(input())
s = input()
print(s.lstrip('o')) # 左側（先頭）の 'o' をすべて取り除いて表示するだけ
