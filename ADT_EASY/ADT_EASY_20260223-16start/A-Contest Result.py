n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
num = 0
for i in b :
    num += a[i-1]
print(num)
