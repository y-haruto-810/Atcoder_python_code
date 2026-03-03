retu = ["a","b","c","d","e","f","g","h"]
gyou= [1,2,3,4,5,6,7,8]
gyou.reverse()
for i in range(8) :
    s = input()
    num = 0 
    for j in s :
        if j == "*" :
            print(retu[num]+str(gyou[i]))
            exit()
        num += 1
