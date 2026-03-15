# 必死に考えたけど間違いのコード
a,b,c,k = map(int,input().split())
if k % 2 == 1 :
    new_a = ((4**(k//2))+2)*a + ((4**(k//2))+1)*b + ((4**(k//2))+1)*c
    new_b = ((4**(k//2))+1)*a + ((4**(k//2))+2)*b + ((4**(k//2))+1)*c
else :
    new_a = (2*(4**(k//2)-1))*a + (2*(4**(k//2)-1)+1)*b + (2*(4**(k//2)-1)+1)*c
    new_b = (2*(4**(k//2)-1)+1)*a + (2*(4**(k//2)-1))*b + (2*(4**(k//2)-1)+1)*c
if new_a - new_b > 10**18 :
    print("Unfair")
else :
    print(new_a - new_b)

# 絶対にTLEするコード 
a,b,c,k = map(int,input().split())
for i in range(k) :
    new_a = b+c
    new_b = a+c
    new_c = a+b
    a = new_a
    b = new_b
    c = new_c
if a - b > 10**18 :
    print("Unfair")
else :
    print(a - b)

# 正解は簡単だったコード
a, b, c, k = map(int, input().split())
if k % 2 == 0: # Kが偶数回なら、差は元のまま (A - B)
    print(a - b)
else: # Kが奇数回なら、差はひっくり返る (B - A)
    print(b - a)
