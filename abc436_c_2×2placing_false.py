n,m = map(int,input().split())
r_c_list = [list(map(int,input().split())) for i in range(2)]
mas = [[0]*n]*n
num = 0 
for j in range(m) :
    if mas[r_c_list[j][0]-1][r_c_list[j][1]-1] and mas[r_c_list[j][0]][r_c_list[j][1]-1] and mas[r_c_list[j][0]-1][r_c_list[j][1]] and mas[r_c_list[j][0]][r_c_list[j][1]] == 0 :
        num+=4
print(num)
