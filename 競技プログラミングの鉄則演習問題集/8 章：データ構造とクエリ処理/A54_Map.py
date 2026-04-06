# ヒントをもらってACしたコード
q = int(input())
seiseki = {}
for _ in range(q):
    num_people = input().split()
    if num_people[0] == "1":
        seiseki[num_people[1]] = int(num_people[2])
    else:
        print(seiseki[num_people[1]])
