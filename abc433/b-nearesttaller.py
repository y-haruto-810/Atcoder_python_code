n = int(input())
a_list = list(map(int, input().split()))
print(-1)
num = 1
for i in a_list[1:] :
    hito_num = 0
    flag = False
    for j in a_list[:num] :
        hito_num += 1
        if j > i :
            tall_num = hito_num
            flag = True
    if flag == True :
        print(tall_num)
    else :
        print(-1)
    num += 1
