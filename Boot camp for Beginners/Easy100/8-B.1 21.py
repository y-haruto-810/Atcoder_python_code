# 
a,b = input().split()
ab = int(a+b)
for i in range(1,100101) :
    if i**2 == ab :
        print("Yes")
        exit()
print("No")
# 約７分でAC

# より短く簡単で分かりやすいコード
a,b = input().split()
ab = int(a+b)
if (ab**0.5//1)**2 == ab:
    print("Yes")
else:
    print("No")
