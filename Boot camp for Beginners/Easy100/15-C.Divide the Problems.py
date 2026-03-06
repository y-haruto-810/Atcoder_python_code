n = int(input())
d = list(map(int,input().split()))
d.sort()
if d[n//2-1] == d[n//2] :
    print(0)
else :
    print(d[n//2] - d[n//2-1])
# 約６分でAC

# さらに短いコード
n = int(input())
d = list(map(int,input().split()))
d.sort()
print(d[n//2] - d[n//2-1])
