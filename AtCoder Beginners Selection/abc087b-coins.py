a = int(input())
b = int(input())
c = int(input())
x = int(input())
num = 0
for i in range(0,a+1) :
    for j in range(0,b+1) :
        if 0 <= (x - (500*i + 100*j)) // 50 <= c :
            num += 1
print(num)
#↑最新コード

#最初のコード
a = int(input())
a_list = [a_d for a_d in range(0,a+1)]
b = int(input())
b_list = [b_e for b_e in range(0,b+1)]
c = int(input())
c_list = [c_f for c_f in range(0,c+1)]
x = int(input())
touri = 0
for d in a_list :
    for e in b_list :
        for f in c_list :
            if d * 500 + e * 100 + f * 50 == x :
                touri += 1
print(touri)
