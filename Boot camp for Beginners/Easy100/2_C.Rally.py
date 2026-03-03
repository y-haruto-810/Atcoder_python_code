n = int(input())
x = list(map(int,input().split()))
count = 0
total = 0
for i in x :
    count += i
if 0 <= (count % len(x)) / len(x) <= 0.5 :
    center = count // len(x)
else :
    center = count // len(x) + 1
for j in x :
    total += (j-center)**2
print(total)
