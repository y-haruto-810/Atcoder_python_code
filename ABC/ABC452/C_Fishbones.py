# 正解のコード
n = int(input())
# 肋骨の条件をメモ
a_list = []
b_list = []
for _ in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
m = int(input())
s_list = []
for _ in range(m):
    s_list.append(input())
# 【魔法の前処理】存在するパーツの条件をすべて Set に突っ込む
available_parts = set()
for s in s_list:
    length = len(s)
    for idx in range(length):
        char = s[idx]
        pos = idx + 1 # 1番目スタートに合わせる
        # 「長さ length で、pos 文字目が char のパーツが存在する」とメモ
        # タプル (長さ, 位置, 文字) にして set に入れる
        available_parts.add((length, pos, char))
# クエリ処理：順番通りに Yes/No を判定する
for s in s_list:
    # 脊椎の長さは N じゃなきゃ絶対にダメ！
    if len(s) != n:
        print("No")
        continue
    can_make = True
    # 1本目から N 本目の肋骨について、パーツが揃うか確認
    for i in range(n):
        req_len = a_list[i]
        req_pos = b_list[i]
        req_char = s[i]
        # 魔法のメモ帳(set)に、必要なパーツの組み合わせが載っているか一瞬で判定
        if (req_len, req_pos, req_char) not in available_parts:
            can_make = False
            break # 1本でもパーツが無ければ、この背骨は作れない
    if can_make:
        print("Yes")
    else:
        print("No")

# 考えたけどダメだったコード
n = int(input())
a_list = []
b_list = []
len_list = []
for i in range(n) :
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)
m = int(input())
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = [] 
s8 = [] 
s9 = []
s10 = []
for _ in range(m) :
    s = input()
    len_list.append(len(s))
    if len(s) == 1 :
        s1.append(s)
    elif len(s) == 2 :
        s2.append(s)
    elif len(s) == 3 :
        s3.append(s)
    elif len(s) == 4 :
        s4.append(s)
    elif len(s) == 5 :
        s5.append(s)
    elif len(s) == 6 :
        s6.append(s)
    elif len(s) == 7 :
        s7.append(s)
    elif len(s) == 8 :
        s8.append(s)
    elif len(s) == 9 :
        s9.append(s)
    elif len(s) == 10 :
        s10.append(s)
if m == 1 :
    m_str = s1
elif m == 2 :
    m_str = s2
elif m == 3 :
    m_str = s3
elif m == 4 :
    m_str = s4
elif m == 5 :
    m_str = s5
elif m == 6 :
    m_str = s6
elif m == 7 :
    m_str = s7
elif m == 8 :
    m_str = s8
elif m == 9 :
    m_str = s9
elif m == 10 :
    m_str = s10

for j in m_str :
    num = -1
    for l in j :
        num += 1
        if a_list[num] == 1 :
            for k in s1 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 2 :
            for k in s2 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 3 :
            for k in s3 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 4 :
            for k in s4 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 5 :
            for k in s5 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 6 :
            for k in s6 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 7 :
            for k in s7 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 8 :
            for k in s8 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 9 :
            for k in s9 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        elif a_list[num] == 10 :
            for k in s10 :
                if j[b_list[num]-1] not in k :
                    print("No") 
                    break
        print("Yes")
