a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0
for i in range(a+1) :
    for j in range(b+1) :
        if 0 <= x - (500*i + 100*j) <= 50*c :
            count += 1
print(count)
# 約４分半でAC
