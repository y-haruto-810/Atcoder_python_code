n,m,c = map(int,input().split())
b = list(map(int,input().split()))
count = 0
for i in range(n) :
    a = list(map(int,input().split()))
    total = c
    for j in range(m) :
        total += (a[j] * b[j])
    if total > 0 :
        count += 1 
print(count)
# 約１８分でAC
