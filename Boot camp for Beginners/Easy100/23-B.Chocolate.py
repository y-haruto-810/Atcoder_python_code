# 正解のコード
n = int(input())
d,x = map(int,input().split())
choko = x
for i in range(n) :
    a = int(input())
    num = 0
    while d >= num * a + 1 :
        choko += 1
        num += 1
print(choko)
# 約１１分半でAC

# while分なしのコード
n = int(input())
d, x = map(int, input().split())
choko = x
for _ in range(n):
    a = int(input())
    choko += (d - 1) // a + 1 # whileループを回さず割り算（//）で一発計算!
print(choko)
