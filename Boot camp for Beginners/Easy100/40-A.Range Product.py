# 奇跡的にACだが条件が抜けていたコード
a,b = map(int,input().split())
if a > 0 and b > 0 :
    print("Positive")
elif a < 0 and b >= 0 :
    print("Zero")
elif a < 0 and b < 0 :
    if -(a + b) % 2 == 0 :
        print("Negative")
    else :
        print("Positive")
# 約６分半でAC

a, b = map(int, input().split()) # aとbの間に0が含まれているか、どちらかが0なら絶対にZero
if a <= 0 <= b: # Python特有の美しい書き方「a <= 0 <= b」が使えます
    print("Zero")
elif a > 0: # 0を含まない場合で、aがプラスなら、bも絶対にプラス（a <= b だから）
    print("Positive")
else: # 残る可能性は「両方マイナス」しかない
    if (b - a + 1) % 2 == 0: # マイナスの数の個数「b - a + 1」が偶数ならPositive
        print("Positive")
    else:
        print("Negative")
        