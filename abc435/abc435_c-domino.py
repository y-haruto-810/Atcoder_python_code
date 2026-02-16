n = int(input())
a = list(map(int, input().split()))
taoreru = 1
count = n
for num in range(1,n) :
    if a[0] == 1 :
        count = num
        break
    else :
        if a[num-1] == 1 :
            taoreru -= 1
            if taoreru == 0 :
                count = num
                break
        else :
            taoseru = a[num-1]
            if taoreru < taoseru :
                taoreru = taoseru
            taoreru -= 1
if count < n :
    print(count)
else :
    print(n)
