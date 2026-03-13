# exitを忘れてその後も処理が続いてしまったコード
n,k,q = map(int,input().split())
point = [k]*n
seikai = [0]*n
if 10**5+1 <= k :
    for _ in range(n) :
        print("Yes")
for _ in range(q) :
    a = int(input())
    seikai[a-1] += 1
for i in range(n) :
    point[i] = point[i] - q + seikai[i]
for j in range(n) :
    if point[j] > 0 :
        print("Yes")
    else :
        print("No")

# 正解のコード
n,k,q = map(int,input().split())
point = [k]*n
seikai = [0]*n
if 10**5+1 <= k :
    for _ in range(n) :
        print("Yes")
    exit()
for _ in range(q) :
    a = int(input())
    seikai[a-1] += 1
for i in range(n) :
    point[i] = point[i] - q + seikai[i]
for j in range(n) :
    if point[j] > 0 :
        print("Yes")
    else :
        print("No")
        