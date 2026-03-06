a,b,c = map(int,input().split())
ah = a//2
bh = b//2
ch = c//2
count = 0
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1 :
    print(0)
elif a==b==c :
    print(-1)
else :
    for _ in range(10000000) :
        count += 1
        a = bh + ch 
        b = ah + ch 
        c = ah + bh
        ah = a//2
        bh = b//2
        ch = c//2
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1 :
            print(count)
            exit()
        elif  a==b==c :
            print(-1)
            exit()
            