# タイプミスした間違いのコード
n,a,b = map(int,input().split())
amari = n % (a+b) 
syou = n // (a+b) 
aodama = syou * a + min(b,amari)
print(aodama)

# 正解のコード
n,a,b = map(int,input().split())
amari = n % (a+b) 
syou = n // (a+b) 
aodama = syou * a + min(a,amari)
print(aodama)
