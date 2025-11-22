n,y = map(int, input().split())
flag = False

for a in range(0,n+1) :
    if flag == True :
        break
    for b in range(0,n+1-a) :
            if y == 10000*a + 5000*b + 1000*(n-a-b) :
                if 0 <= n-a-b :
                    print(a,b,n-a-b)
                    flag = True
                    break
if flag == False :
    print(-1, -1, -1)
