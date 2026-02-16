n = int(input())
s = input()
s_list = [i for i in s]
num = n - len(s_list)
s_r = "o" * num + s
print(s_r)