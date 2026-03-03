n,q = map(int,input().split())
x = list(map(int,input().split()))
box = [0]*n
jun = []
for i in x :
    if i >= 1 :
        box[i-1] += 1
        jun.append(i)
    else :
        num = 0
        for j in box :
            if j == min(box) :
                box[num] += 1
                jun.append(num+1)
                break
            else :
                num += 1
for k in jun :
    print(k,end=" ")
    