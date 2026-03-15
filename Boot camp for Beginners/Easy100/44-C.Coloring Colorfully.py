# 正解のコード
s = input()
kuro = s.count("0")
siro = s.count("1")
num1 = 0
num2 = 0
mae = "1" 
for i in s :
    if i == mae :
        num1 += 1
        if i == "0" :
            mae = "1"
        else :
            mae = "0"
    else :
        mae = i
mae = "0"
for i in s :
    if i == mae :
        num2 += 1
        if i == "0" :
            mae = "1"
        else :
            mae = "0"
    else :
        mae = i
print(min(num1,num2))
# 約１６分半でAC

# 短縮したコード
s = input()
num1 = 0  # 010101... と比較して違う文字の数
num2 = 0  # 101010... と比較して違う文字の数
for i in range(len(s)): # range(len(s)) でインデックスを取得しながらループ
    if i % 2 == 0:  # 偶数番目のとき
        if s[i] != "0": num1 += 1
        if s[i] != "1": num2 += 1
    else:           # 奇数番目のとき
        if s[i] != "1": num1 += 1
        if s[i] != "0": num2 += 1
print(min(num1, num2))

# 奇数偶数を分けて足し算をして数えるコード
def main():
    S = [int(i) for i in list(input())]
    odd = []
    even = []
    for idx in range(len(S)):
        if idx%2:
            odd.append(S[idx])
        else:
            even.append(S[idx])
    # if all even are to be black 
    even_black = sum(even) + (len(odd)-sum(odd))
    # if all odd are to be black
    odd_black = sum(odd) + (len(even)-sum(even))
    print(min(even_black, odd_black))
main()
