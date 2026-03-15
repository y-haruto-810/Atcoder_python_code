n = int(input())
h = list(map(int,input().split()))
now = h[0]
num = 0
maxnum = 0
for i in range(1,n) :
    if now >= h[i] :
        now = h[i]
        num += 1
        maxnum = max(maxnum,num)
    else :
        now = h[i]
        num = 0
print(maxnum)
# 約１１分でAC

# 前のものと今のものを比べるコード
n = int(input())
h = list(map(int, input().split()))
num = 0
maxnum = 0
for i in range(1, n): # i を 1 からスタートし、「1つ左(i-1)」と「今(i)」を比べる
    if h[i-1] >= h[i]:  # 左のマスの方が高い（または同じ）なら降りられる
        num += 1
        maxnum = max(maxnum, num)
    else: # 登ってしまうならリセット
        num = 0
print(maxnum)
