n,m = map(int,input().split())
c = list(map(int,input().split()))
cosyou = [0] * m
ryou = 0
for i in range(n) :
    a,b = map(int,input().split())
    cosyou[a-1] += b
for j in range(m) :
    ryou += min(cosyou[j],c[j])
print(ryou)
