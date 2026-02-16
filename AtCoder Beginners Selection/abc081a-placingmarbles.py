# before
bidama = 0
num = input()
number = str(num)
s_list = list(number)
int_s_list = [int(i) for i in s_list]
for j in int_s_list :
    if j == 1 :
        bidama += 1
print(bidama)

#after
s = input()
num = 0
for i in s :
    if i == "1" :
        num += 1
print(num)
