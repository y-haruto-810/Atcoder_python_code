# ヒントをもらってACしたコード
n = int(input())
a = list(map(int,input().split()))
d = int(input())
leftmax = 0
leftmax_list = []
for i in a :
    if i > leftmax :
        leftmax = i 
    leftmax_list.append(leftmax)
lightmax = 0
lightmax_list = []
for j in a[::-1] :
    if j > lightmax :
            lightmax = j
    lightmax_list.append(lightmax)
lightmax_list.reverse()
for k in range(d) :
    l,r = map(int,input().split())
    print(max(leftmax_list[l-2],lightmax_list[r]))
