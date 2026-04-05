h,w = map(int,input().split())
print("#"*w)
for _ in range(h-2) :
    print("#","."*(w-2),"#",sep="")
print("#"*w)
