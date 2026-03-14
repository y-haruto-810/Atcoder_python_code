h,w,q = map(int,input().split())
gyou = h
retu = w
for i in range(q) :
    num,rc = map(int,input().split())
    if num == 1 :
        gyou = gyou - rc
        print(retu*rc)
    elif num == 2 :    
        retu = retu - rc
        print(gyou*rc)
        