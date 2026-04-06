# ACだがTLEになりやすいコード
q = int(input())
people = []
for _ in range(q):
    num_hito = input().split()
    if num_hito[0] == "1":
        people.append(num_hito[1])
    elif num_hito[0] == "2":
        print(people[0])
    elif num_hito[0] == "3":
        people.pop(0)
# 約４分１５秒でAC

# dequeを使ったTLEになりにくいコード
from collections import deque 
q = int(input())
people = deque()
for _ in range(q):
    num_hito = input().split()
    if num_hito[0] == "1":
        people.append(num_hito[1])
    elif num_hito[0] == "2":
        print(people[0])
    elif num_hito[0] == "3":
        people.popleft()
