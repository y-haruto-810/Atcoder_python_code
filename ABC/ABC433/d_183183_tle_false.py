n,m = map(int, input().split())
a_list = list(map(int, input().split()))
sum = 0
for i in range(n) :
    for j in range(n) :
        num = int(str(a_list[i]) + str(a_list[j]))
        if num % m == 0 :
            sum += 1
print(sum)
