x,y,z = map(int, input().split())
flag = False
if x == y * z :
        print("Yes")
        flag = True
else :
    while x / y > 2 :
        x += 1
        y += 1
        if x == y * z :
            print("Yes")
            flag = True
            break
if flag == False :
    print("No")
