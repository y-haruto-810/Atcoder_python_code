# 正解のコード
s = input()
s_set = set()
for i in s :
    if i in s_set :
        print("no")
        exit()
    else :
        s_set.add(i)
print("yes")
# 約２分半でAC

# よりスリムなコード
s = input() # 元の文字列の長さとsetにして重複を消した後の長さを比べるだけ
if len(s) == len(set(s)):
    print("yes") 
else:
    print("no")
    