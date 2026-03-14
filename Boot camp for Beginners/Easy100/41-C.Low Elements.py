n = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(n) :
    if i == 0 : # ここはなくてもできる
        nowmin = p[0] 
        count += 1
    else :
        if p[i] <= nowmin :
            count += 1
            nowmin = p[i]
print(count)
# 約１０分でAC
