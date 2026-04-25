# 久しぶりにC問題をACしたコード
from collections import deque # いらなかった
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split()))
a_dict = dict()
for i in range(n) :
    if a[i] in a_dict :
        a_dict[a[i]] += a[i]
    else :
        a_dict[a[i]] = a[i]
a_list = list(a_dict.values())
a_list.sort()
for _ in range(k) :
    if a_list != [] :
        a_list.pop()
    else :
        print(0)
        exit()
num = 0
for j in a_list :
    num += j
print(num)

# もっとスリムな書き方
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
a_dict = dict()
for i in range(n):
    if a[i] in a_dict:
        a_dict[a[i]] += a[i]
    else:
        a_dict[a[i]] = a[i]
a_list = list(a_dict.values()) # 大きい順（降順）にソートする
a_list.sort(reverse=True)
print(sum(a_list[k:])) # 先頭からk個分をスライスで切り落とし（無視し）残った部分の合計を出す

# dequeとlistを比較してしまい空のlistからpopleftしてしまった効率の悪いエラーが出るコード
from collections import deque 
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split()))
a_dict = dict()
for i in range(n) :
    if a[i] in a_dict :
        a_dict[a[i]] += a[i]
    else :
        a_dict[a[i]] = a[i]
a_list = list(a_dict.values())
a_list.sort(reverse=True)
a_list = deque(a_list)
for _ in range(k) :
    if a_list != [] :    # if a_list :            ←こうすれば良かった
        a_list.popleft() #     a_list.popleft()   ←こうすれば良かった
    else :               
        print(0)
        exit()
num = 0
for j in a_list :
    num += j
print(num)
