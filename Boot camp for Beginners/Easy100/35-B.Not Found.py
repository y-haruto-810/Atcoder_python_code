s = input()
s_set = set()
alfabet = "abcdefghijklmnopqrstuvwxyz"
nai = []
for i in s :
    if i not in s_set :
        s_set.add(i)
for j in alfabet :
    if j not in s_set :
        print(j)
        exit()
print(None)
# 約１３分半でAC

# 短くミスのしにくいコード
import string # 魔法のモジュールを読み込む
s_set = set(input()) # 一発でsetにする
for j in string.ascii_lowercase:
    if j not in s_set:
        print(j)
        exit() # string.ascii_lowercase には "abcdefg..." が最初から入っている
print("None")
