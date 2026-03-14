n,m = map(int,input().split())
for i in range(n) :
    ka = list(map(int,input().split()))
    tugisuki = []
    if i == 0 :
        allsuki = ka[1:] 
    else :
        for j in range(1,ka[0]+1) :
            if ka[j] in allsuki :
                tugisuki.append(ka[j])
        allsuki = tugisuki
print(len(allsuki))
# 約１３分でAC
