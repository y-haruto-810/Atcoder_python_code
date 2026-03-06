# 正解のコード
n = int(input())
if n == 1 :
    print(1)
elif 2<=n<=3 :
    print(2)
elif 4<=n<=7 :
    print(4)
elif 8<=n<=15 :
    print(8)
elif 16<=n<=31 :
    print(16)
elif 32<=n<=63 :
    print(32)
elif 64<=n<=100 :
    print(64)
# 約６分でAC

# nが巨大でも対応できるコード
n = int(input())
ans = 1
while ans * 2 <= n: # ans に 2を掛けても n を超えない間は、2を掛け続ける
    ans *= 2
print(ans)
