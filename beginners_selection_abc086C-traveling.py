n = int(input())
pt,px,py = 0,0,0

for _ in range(n) :
    t,x,y = map(int,input().split())
    if (t-pt)-(abs(x-px)+abs(y-py)) < 0 :
        print("No")
        exit()
    elif (t-pt)-(abs(x-px)+abs(y-py)) == 0 :
        pt,px,py = t,x,y
    else :
        if ((t-pt)-(abs(x-px)+abs(y-py))) % 2 == 0 :
            pt,px,py = t,x,y
        else :
            print("No")
            exit()
print("Yes")
