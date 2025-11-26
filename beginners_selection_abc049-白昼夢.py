s = input()
s_reverse = s[::-1]
s_target = ("maerd","remaerd","esare","resare")
while s_reverse != "" : 
    flag = False
    for i in s_target : 
        if s_reverse.startswith(i) :
            s_reverse = s_reverse[len(i):] 
            flag = True
    if flag == False :
        print("NO")
        break
if s_reverse == "" :
    print("YES")
