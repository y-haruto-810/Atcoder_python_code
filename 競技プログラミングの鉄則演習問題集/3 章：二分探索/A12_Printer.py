# TLEやWAになるコード
n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
num = 0
for i in range(1,k+1):
    for j in a :
        if i % j == 0 :
            num += 1
    if num >= k :
        print(i)
        exit()
# 二分探索で秒数を求めるコード
n,k = map(int,input().split())
a = list(map(int,input().split()))
num = 0
left = 1
right = 10**9
ans = 0
while left <= right :
    num = 0
    mid = (left + right) // 2
    for j in a :
        num += mid // j
    if num >= k :
        ans = mid
        right = mid - 1
    else :
        left = mid + 1
print(ans)
