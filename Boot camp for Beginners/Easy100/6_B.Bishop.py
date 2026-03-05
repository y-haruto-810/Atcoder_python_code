h,w = map(int,input().split())
total = h * w
if h == 1 or w == 1 :
    print(1)
elif total % 2 == 0 :
    print(total//2)
else :
    print((total//2)+1)
    