n = int(input())
a = list(map(int,input().split()))
count = 0
flag = True
while flag == True :
    for i in range(len(a)) :
        if a[i] % 2 == 0 :
            a[i] //= 2
        else :
            print(count)
            exit()
    count += 1
# 約４分でAC
