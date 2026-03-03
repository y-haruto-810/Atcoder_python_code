n = int(input())
a = list(map(int,input().split()))
masu = [0,0,0,0]
p = 0
for i in a :
    if i == 1 :
        masu[0] = 1
        masu.insert(0,0)
        if masu[4] == 1 :
            p += 1
        del masu[4]
    elif i == 2 :
        masu[0] = 1
        masu.insert(0,0)
        masu.insert(0,0)
        if masu[5] == 1 :
            p += 1
        del masu[5]
        if masu[4] == 1 :
            p += 1
        del masu[4]
    elif i == 3 :
        masu[0] = 1
        masu.insert(0,0)
        masu.insert(0,0)
        masu.insert(0,0)
        if masu[6] == 1 :
            p += 1
        del masu[6]
        if masu[5] == 1 :
            p += 1
        del masu[5]
        if masu[4] == 1 :
            p += 1
        del masu[4]
    else :
        masu[0] = 1
        for j in masu :
            if j == 1 :
                p += 1
        masu = [0,0,0,0]
print(p)
