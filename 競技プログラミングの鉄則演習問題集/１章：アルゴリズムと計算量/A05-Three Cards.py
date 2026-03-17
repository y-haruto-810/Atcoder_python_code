n,k = map(int,input().split())
num = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if 1 <= k - (i + j) <= n :
            num += 1
print(num)
# 約５分でAC
