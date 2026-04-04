# 毎回topとminを更新しているため答えが見つかりづらくTLEになるコード
n,x = map(int,input().split())
a = list(map(int,input().split()))
now = (n+1)//2 
flag = True
while flag :
    if a[now-1] == x :
        print(now)
        exit()
    elif a[now-1] > x :
        top = now
        min = 0
        now = (min+top+1)//2
    else :
        top = n
        min = now
        now = (min+top+1)//2

# ちゃんとした二分探索のコード
n,x = map(int,input().split())
a = list(map(int,input().split()))
now = (n+1)//2 
right = n
left = 0
while left <= right :
    if a[now-1] == x :
        print(now)
        exit()
    elif a[now-1] > x :
        right = now-1
        now = (left+right+1)//2
    else :
        left = now+1
        now = (left+right+1)//2

# bisectモジュールを使ったコード
import bisect
n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = bisect.bisect_left(a, x) # bisect_left はxを挿入するなら左から何番目かを二分探索で一瞬で出してくれる
print(ans + 1) # 1番目スタートにするために+1するだけ
