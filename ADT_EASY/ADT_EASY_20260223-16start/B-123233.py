n = input()
count_1 = 0
count_2 = 0
count_3 = 0
for i in n :
    if int(i) == 1 :
        count_1 += 1
    elif int(i) == 2 :
        count_2 += 1
    elif int(i) == 3 :
        count_3 += 1
    else :
        print("No")
        exit()
if count_1 == 1 and count_2 == 2 and count_3 == 3 :
    print("Yes")
else :
    print("No")
