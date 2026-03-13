# 正解のコード
a,b = map(int,input().split())
s = input()
if s[a] != "-" :
        print("No")
        exit()
s = s[:a] + s[a+1:]
for i in s :
    if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" :
        pass
    else :
        print("No")
        exit()
print("Yes")
# 約１４分でAC

# isdisitを使った短いコード
a, b = map(int, input().split())
s = input()
if s[a] != "-": # 条件1: a番目がハイフンじゃないならダメ
    print("No")
    exit()
rest_s = s[:a] + s[a+1:] # 条件2: ハイフンを抜いた残りの文字列を作る
if rest_s.isdigit(): # rest_s が「すべて数字」ならYes、違うものが混ざってたらNo
    print("Yes")
else:
    print("No")
