n = int(input())
v = list(map(int,input().split()))
v.sort()
newgu = 0
for i in range(n-1) :
    newgu = (v[0] + v[1]) / 2
    del v[0]
    del v[0]
    v.append(newgu)
    v.sort()
print(*v)
# 約１１分でAC

# より無駄のないコード
n = int(input())
v = list(map(int, input().split()))
v.sort() # 最初の一回だけ並び替える
ans = v[0] # 一番小さい具材を最初のベースにする
for i in range(1, n):# 残りの具材を順番に足して2で割っていく！
    ans = (ans + v[i]) / 2
print(ans)
