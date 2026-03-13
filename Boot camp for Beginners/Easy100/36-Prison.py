n,m = map(int,input().split())
max_l = 0
min_r = 10**5
for _ in range(m) :
    l,r = map(int,input().split())
    max_l = max(max_l,l) 
    min_r = min(min_r,r) 
if min_r < max_l :
    print(0)
else :
    print(min_r-max_l+1)
# 約１４分でAC
