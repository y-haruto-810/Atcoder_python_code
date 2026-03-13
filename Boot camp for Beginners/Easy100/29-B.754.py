s = input()
sa = 1000
for i in range(len(s)-2) :
    sa = min(sa,abs(753-int(s[i]+s[i+1]+s[i+2])))
print(sa)
# 約６分でAC
