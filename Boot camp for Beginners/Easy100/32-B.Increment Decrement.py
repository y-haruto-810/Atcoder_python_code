n = int(input())
s = input()
x = 0 
max_x = 0
for i in s :
    if i == "I" :
        x += 1
        if max_x < x :
            max_x = x
    elif i == "D" :
        x -= 1 
print(max_x)
# 約５分でAC
