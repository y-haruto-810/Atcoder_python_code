# 正解のコード
x = int(input())
for i in range(x,10**6+1) :
    flag = False
    for j in range(2,318) :
        if i == j :
            pass
        elif i % j == 0 :
            flag = True
    if flag == False :
        print(i)
        exit()
# 約２１分半でAC

# 関数を使った美しいコード
def is_prime(n): # 素数かどうかを判定する専用の関数を作る
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # nの平方根（0.5乗）まで調べればOK
        if n % i == 0:
            return False # 割り切れたら素数じゃない（False）
    return True # 全部割り切れなかったら素数（True）
x = int(input())
while True: # 上限（10**6など）を決めず、見つかるまで無限に探し続ける！
    if is_prime(x):
        print(x)
        exit()
    x += 1 # 見つからなかったら次の数字へ
    