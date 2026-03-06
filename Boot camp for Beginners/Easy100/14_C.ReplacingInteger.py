# 間違いのコード
n,k = map(int,input().split())
if k == n or k == 1:
    print(0)
elif k - n > 0 :
    print(min(n,k-n))
elif k == 2 :
    if k % 2 == 1:
        print(1)
    else :
        print(0)
elif k == 3 :
    if k % 3 == 0:
        print(0)
    elif k % 3 == 1:
        print(1)
    else  :
        print(1)
elif k == 4 :
    if k % 4 == 0:
        print(0)
    elif k % 4 == 1:
        print(1)
    elif k % 4 == 2:
        print(2)
    else  :
        print(1)
else :
    
# 正解のコード
n,k = map(int,input().split())
if k == n or k == 1:
    print(0)
elif k - n > 0 :
    print(min(n,k-n))
else :
    print(min(n % k,abs((n%k)-k))) 

# 無駄を省いたコード
n,k = map(int, input().split())
print(min(n % k, k - (n % k)))
