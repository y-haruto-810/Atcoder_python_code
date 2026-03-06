# 正解のコード
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
alice = 0
bob = 0
for i in range(n) :
    if i % 2 == 0 :
        alice += a[i]
    else :
        bob += a[i]
print(alice-bob)
# 約５分半でAC

# スライスを使った解き方
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
# a[::2] は「最初から最後まで、2つ飛ばしで取る（＝Aliceのカード）」
# a[1::2] は「1番目から最後まで、2つ飛ばしで取る（＝Bobのカード）」
print(sum(a[::2]) - sum(a[1::2]))
