# 正解のコード
s = input()
max_len = 0
now_len = 0
for i in s :
    if i == "A" or i == "C" or i == "G" or i == "T" :
        now_len += 1 
        if max_len < now_len :
            max_len = now_len
    else :
        now_len = 0
print(max_len)
# 約７分でAC

# よりスリムな書き方
s = input()
max_len = 0
now_len = 0
for i in s :
    if i in "ACGT" :
        now_len += 1 
        if max_len < now_len :
            max_len = now_len
    else :
        now_len = 0
print(max_len)
