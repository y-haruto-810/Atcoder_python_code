# 問題名の通りにsetでしようとしたら行き詰まってしまったコード
q = int(input())
card = set()
for _ in range(q):
    num,x = map(int, input().split())
    if num == 1:
        card.add(x)
    elif num == 2:
        card.remove(x)
    else:
        どうしよう

#　bisectを使い二分探索でACしたコード
import bisect
q = int(input())
card = []
for _ in range(q):
    num,x = map(int, input().split())
    if num == 1:
        bisect.insort(card,x)
    elif num == 2:
        card.remove(x)
    else:
        iti = bisect.bisect_left(card,x)
        if len(card) <= iti:
            print(-1)
        else:
            print(card[iti])
