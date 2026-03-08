k,m = map(int,input().split())
for i in range(k) :
    c,l = map(int,input().split())
    if i == 0 :
        s = str(c) * l
    else :
        s += str(c) * l
kakko = (int(s) / m) // 1 
kotae = kakko % 10007
print(int(kotae))
