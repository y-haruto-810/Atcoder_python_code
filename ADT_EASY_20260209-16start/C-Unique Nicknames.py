#　解けなかったコード

n = int(input())
s_list = []
t_list = []
s_flag = False
f_flag = False
for _ in range(n) :
    s,t = map(str,input().split())
    s_list.append(s)
    t_list.append(t)
a = 0
for i in s_list[1:] :
    if s_list[a] == s_list[i] :
        
if s_flag :
    for j in t_list[:] :
        if s_list[a] == s_list[i] :
            s_flag = True
        for k in t_list :
            t_list[i]

#　正解のコード
n = int(input()) # 扱いやすいように、[苗字, 名前] のリストを人数分作る
people = []
for _ in range(n):
    s, t = input().split()
    people.append([s, t])

for i in range(n): # 全員について「あだ名がつけられるか」チェックする
    my_s = people[i][0]# i番目の人の苗字(s)と名前(t)
    my_t = people[i][1]
    
    s_ok = True # 1. 苗字は使えるか？フラグ
    for j in range(n):
        if i == j: 
            continue # 自分自身とは比較しない
        if my_s == people[j][0] or my_s == people[j][1]: 
            s_ok = False # 誰かの苗字か名前に被っていたらダメ
            break
            
    t_ok = True # 2. 名前は使えるか？フラグ
    for j in range(n):
        if i == j: 
            continue # 自分自身とは比較しない
        if my_t == people[j][0] or my_t == people[j][1]:
            t_ok = False
            break
    
    if s_ok == False and t_ok == False: 
        print("No") # 苗字も名前もダメなら、その時点で「不可能」確定
        exit()

print("Yes")
