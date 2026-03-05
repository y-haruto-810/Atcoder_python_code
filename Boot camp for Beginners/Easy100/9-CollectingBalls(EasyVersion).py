n = int(input())
k = int(input())
x = list(map(int,input().split()))
a = []
b = []
kyori = []
for i in x :
    a.append(2*i)
    b.append(2*abs(k-i))
for j in range(n) :
    kyori.append(min(a[j],b[j]))
print(sum(kyori))
# 約１２分半でAC

# その都度判断してtotalに入れていくコード
n = int(input())
k = int(input())
x = list(map(int, input().split()))

total = 0  # 合計距離を入れるバケツ
for i in x:
    # Aの距離とBの距離をその場で比べて、小さい方を直接バケツに足す！
    total += min(i * 2, (k - i) * 2)

print(total)

# その都度判断してtotalに入れていくコードの改良版
n = int(input())
k = int(input())
x = list(map(int, input().split()))
print(sum(min(i * 2, (k - i) * 2) for i in x))
