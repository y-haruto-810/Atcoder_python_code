s = input()
num_i = -1
num_j = 0
count = 0
for i in s :
    num_i += 1
    if i == "A" :
        num_j = num_i 
        for j in s[num_i+1:] :
            num_j += 1
            if j == "B" :
                if 2*(num_j)-num_i < len(s) :
                    if s[2*(num_j)-num_i] == "C"  :
                        count += 1
print(count)
