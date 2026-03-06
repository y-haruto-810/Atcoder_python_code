# 正解のコード
s = int(input())
a_set = set()
a_set.add(s)
n = s
for i in range(2,1000001) :
    if n % 2 == 0 :
        n = n // 2 
    else :
        n = 3 * n + 1
    if n in a_set :
        print(i)
        exit()
    else :
        a_set.add(n)
# 約１１分でAC

# 関数を使用したコード
def f(n): # 問題文の f(n) をそのまま関数にする！
    if n % 2 == 0:
        return n // 2  # 偶数なら半分にして「返す」
    else:
        return 3 * n + 1 # 奇数なら3倍して1足して「返す」
s = int(input())
a_set = {s} # 波括弧 {} で直接セットを作るプロの技！
n = s
for i in range(2, 1000001):
    n = f(n) # ここでさっき作った関数を呼び出す！めちゃくちゃスッキリ！
    if n in a_set:
        print(i)
        exit()
    else:
        a_set.add(n)
        