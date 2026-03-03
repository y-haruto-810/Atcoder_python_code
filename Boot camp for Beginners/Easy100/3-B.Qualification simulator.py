n,a,b = map(int,input().split())
s = input()
total_count = 0
b_count = 0
for i in s :
    if i == "a" and total_count < a+b :
        print("Yes")
        total_count += 1
    elif i == "b" and total_count < a+b and b_count < b :
        print("Yes")
        total_count += 1
        b_count += 1
    else :
        print("No")
# 約１２分半でAC
