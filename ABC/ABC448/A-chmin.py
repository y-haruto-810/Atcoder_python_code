n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in a :
    if i < x :
        print(1)
        x = i
    else :
        print(0)
        