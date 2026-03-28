# ACしたコード
n,m = map(int,input().split())
nowlist = [0]*m
nextlist = [0]*m
for i in range(n) :
    a,b = map(int,input().split())
    nowlist[a-1] += 1
    nextlist[b-1] += 1
for j in range(m) :
    print(nextlist[j] - nowlist[j])

# いもす法のコード
n, m = map(int, input().split())
change = [0] * m  # 差分だけを記録するリストを1つ作る
for _ in range(n):
    a, b = map(int, input().split())
    change[a-1] -= 1  # 今の部門から 1人いなくなる (-1)
    change[b-1] += 1  # 来期の部門に 1人やってくる (+1)
for ans in change:
    print(ans)
    