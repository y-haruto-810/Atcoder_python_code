# 点をもらえたが不正解のコード
h,w = map(int,input().split())
s_list = []
t_list = []
for _ in range(h) :
    s = input()
    count = 0
    for i in s :
        if i == "#" :
            count += 1
    s_list.append(count)
for _ in range(h) :
    t = input()
    count = 0
    for j in t :
        if j == "#" :
            count += 1
    t_list.append(count)
if s_list != t_list :
    print("No")
else :
    print("Yes")

# 正しいコード
h,w = map(int,input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]
s = list(zip(*s))
t = list(zip(*t))
s.sort()
t.sort()
if s == t :
    print("Yes")
else :
    print("No")
