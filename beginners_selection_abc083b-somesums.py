n,a,b = map(int, input().split())
sum = 0
for i in range(1,n+1) :
    if 1 <= i <= 9 :
        if a <= i <= b :
            sum += i
    if 10 <= i <= 10000 :
        num = 0
        i_str = str(i)
        i_list = [int(j) for j in list(i_str)]
        for k in i_list :
            num += k
        if a <= num <= b :
                sum += i
print(sum)
