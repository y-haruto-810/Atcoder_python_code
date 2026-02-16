n = int(input())
a = list(map(int, input().split()))
count = 0
for l in range(1,n+1) :
    for r in range(l,n+1) :
        num = 0
        for i in a[l-1:r] :
            num += i
        flag = False
        for j in a[l-1:r] :
            if num % j == 0 :
                flag = True
        if flag == False :
            count += 1
print(count)
