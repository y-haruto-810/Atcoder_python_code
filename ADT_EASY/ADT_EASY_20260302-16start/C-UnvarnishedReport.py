s = input()
t = input()
if s == t :
    print(0)
else :
    if len(s) == len(t) :
        for i in range(len(s)) :
            if s[i] != t[i] :
                print(i+1)
                exit()
    else :
        if len(s) == min(len(s),len(t)) :
            s = s + (len(t) - len(s))*"A"   
        else :
            t = t + (len(s) - len(t))*"A"
    for j in range(len(s)) :
        if s[j] != t[j] :
            print(j+1)
            exit()
