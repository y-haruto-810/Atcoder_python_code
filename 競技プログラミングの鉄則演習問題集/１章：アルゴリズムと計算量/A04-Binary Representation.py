# 正解のコード
n = int(input())
n = bin(n)
n = n[2:]
n = (10 - len(n)) * "0" + n
print(n)
# 約３分１５秒でAC

# f文字列を使った短いコード
n = int(input())
print(f"{n:010b}") # 「nを、0埋め(0)の、10桁(10)の、2進数(b)にして」という魔法
