# 正解だが長いコード
a = input()
b = input()
c = input()
d = input()
e = input()
amari = [int(a),int(b),int(c),int(d),int(e)]
count = 0
for i in range(1,10) :
    if a[0] != 0 :
        if i == int(a[-1]) :
            last = int(a)
            break
    if b[0] != 0 :
        if i == int(b[-1]) :
            last = int(b)
            break
    if c[0] != 0 :
        if i == int(c[-1]) :
            last = int(c)
            break
    if d[0] != 0 :
        if i == int(d[-1]) :
            last = int(d)
            break
    if e[0] != 0 :
        if i == int(e[-1]) :
            last = int(e)
            break
    last = int(a)
amari.remove(last)
for j in range(4) :
    if amari[j] % 10 != 0 :
        amari[j] += 10 - amari[j] % 10
for k in amari :
    count += k
count += last 
print(count)
# 約２８分でAC

# 短くて一気に計算するコード
t = [int(input()) for _ in range(5)] # 5つの入力をいっきにリストで受け取る
total_time = 0
max_loss = 0 # 節約できる最大の時間
for x in t:
    if x % 10 == 0: # 10の倍数に切り上げた時間を計算する
        kiriage = x
    else: # (x % 10 が 0 ならそのまま、それ以外なら 10 - 余り を足す)
        kiriage = x + (10 - x % 10)
    total_time += kiriage
    max_loss = max(max_loss, kiriage - x) # ロスが一番大きいものを更新していく
print(total_time - max_loss) # 全部の切り上げ合計時間から一番大きかったロスを引く
