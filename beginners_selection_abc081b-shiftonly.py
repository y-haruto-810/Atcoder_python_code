n = int(input())
a = list(map(int, input().split()))
sousa = 0
kisuu_flag = False
while kisuu_flag == False :
    for num in a :
        if num % 2 != 0 :
            kisuu_flag = True
    if kisuu_flag == False :
        a = [i//2 for i in a]
        sousa += 1
print(sousa)
