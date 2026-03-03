# 正解のコード
a,b = map(int,input().split())
if b == 1 :
    print(0)
elif a >= b :
    print(1)
else :
    c = a
    for i in range(1,100) :
        if c < b :
            c = c + a - 1
        else :
            print(i)
            exit()
            
# もっと良いコード
a, b = map(int, input().split())

c = 1      # 最初から持っている口の数は「1」
count = 0  # 買ったタップの数は最初「0」

while c < b: # 持っている口(c)が、欲しい数(b)より少ない間だけタップを買う！
    c = c + a - 1  # あなたの考えた最強の式！
    count += 1     # 買った数を1つ増やす
    
print(count)
