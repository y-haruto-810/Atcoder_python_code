# 間違いのコード
n,q = map(int,input().split())
s = list(input())
for i in range(q) :
    x,c = input().split()
    x = int(x)
    s = s[:x]+s[x]+s[x+1:]
    num = 0
    for j in range(n-2) :
        if s[j] == "a" and s[j+1] == "b" and s[j+2] == "c" :
            num += 1
    print(num)

# 正解のコード
n,q = map(int,input().split())
s = list(input())
num = 0
for i in range(n-2) :
    if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C" :
        num += 1

def check(j) :
    if 0 <= j and j+2 < n :
        if s[j] == "A" and s[j+1] == "B" and s[j+2] == "C" :
            return 1
    return 0
        
for _ in range(q) :
    x,c = input().split()
    x = int(x)-1
    num -= check(x-2)
    num -= check(x-1)
    num -= check(x)
    s[x] = c
    num += check(x-2)
    num += check(x-1)
    num += check(x)
    print(num)
    