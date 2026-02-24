n = int(input())
d_list = [int(input()) for i in range(n)]
d_list.sort(reverse=True)
count = 1
size = d_list[0]
for i in d_list[1:] :
    if i < size :
        count+=1
        size = i
print(count)
