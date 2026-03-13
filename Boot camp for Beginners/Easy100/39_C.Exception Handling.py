# TLE（時間切れ）になったコード
n = int(input())
a = [input() for _ in range(n)]
a_copy = a.copy()
max_a = max(a_copy)
a_copy.remove(max_a)
if max_a == max(a_copy) :
    for _ in range(n) :
        print(max(a))
else :
    for i in range(n) :
        if a[i] == max(a) :
            print(max(a_copy))
        else :
            print(max(a))

# 実行時間が短くて済むコード
n = int(input())
a = [int(input()) for _ in range(n)] # ちゃんと int に変換して受け取る
max1 = max(a) # 最大値（1番大きい数）を1回だけ探して保存
a_copy = a.copy() # コピーから最大値を1つ消して、2番目に大きい数を探して保存
a_copy.remove(max1)
max2 = max(a_copy)
for i in range(n): # あとはループで判定するだけ
    if a[i] == max1:
        print(max2)
    else:
        print(max1)
        