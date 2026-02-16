n = int(input())
n_list = [[0 for j in range(n)] for i in range(n)]
n_list[0][(n-1)//2] = 1
r=0
c=(n-1)//2
k=1
for l in range(n*n-1) :
    if [(r-1)%n][(c+1)%n] == 0 :
        [(r-1)%n][(c+1)%n] = k+1
    else :
        [(r+1)%n][c] = k+1
print(n_list)
for o in range(n) :
    print((p for p in n_list[o]),end="")
    print()
print(n_list[o], sep='')
