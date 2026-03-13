# 間違いのコード
h = int(input())
kaisu = 0 
monster = [h]
nextmonster = []
while monster != [] :
    for i in monster :
        kaisu += 1
        if i != 1 :
            nextmonster.append(i // 2)
            nextmonster.append(i // 2)
    monster = nextmonster
    nextmonster = []
print(kaisu)

# 正解のコード
h = int(input())
kaisu = 0 
monster = h
num = 1
while monster != 0 :
    kaisu += num
    monster //= 2
    num *= 2 
print(kaisu)
# 約２４分でAC

# pythonのサボれるコード
h = int(input())
print(2 ** h.bit_length() - 1) # hの2進数での桁数乗-1を計算する
