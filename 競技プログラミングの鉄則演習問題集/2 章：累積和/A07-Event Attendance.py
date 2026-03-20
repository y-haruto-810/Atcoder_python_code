# TLEになったコード
d = int(input())
n = int(input())
people = [0] * d
for i in range(n) :
    l,r = map(int,input().split())
    for j in range(l-1,r) :
        people[j] += 1
for k in range(d) :
    print(people[k])

# 正解のコード
d = int(input())
n = int(input())
zougen = [0] * (d+1)
for _ in range(n) :
    l,r = map(int,input().split())
    zougen[l-1] += 1
    zougen[r] -= 1
zenjitu = 0
for i in zougen[:d] :
    print(zenjitu+i)
    zenjitu = zenjitu+i
    