# 間違いのコード
n,q = map(int,input().split())
a = list(map(int,input().split()))
a_copy = a.copy() 
for _ in range(q) :
    k = int(input())
    b = list(map(int,input().split()))
    if len(b) == 1 :
        a_copy.remove(a[b[0]-1])
    elif len(b) == 2 :
        a_copy.remove(a[b[0]-1])
        a_copy.remove(a[b[1]-1])
    elif len(b) == 3 :
        a_copy.remove(a[b[0]-1])
        a_copy.remove(a[b[1]-1])
        a_copy.remove(a[b[2]-1])
    elif len(b) == 4 :
        a_copy.remove(a[b[0]-1])
        a_copy.remove(a[b[1]-1])
        a_copy.remove(a[b[2]-1])
        a_copy.remove(a[b[3]-1])
    elif len(b) == 5 :
        a_copy.remove(a[b[0]-1])
        a_copy.remove(a[b[1]-1])
        a_copy.remove(a[b[2]-1])
        a_copy.remove(a[b[3]-1])
        a_copy.remove(a[b[4]-1])
    a_copy.sort()
    print(a_copy[0])
    a_copy = a.copy() 

# 正解のコード
n, q = map(int, input().split())
a = list(map(int, input().split()))
# 【準備】
ball_list = [] # (値, 元の番号) のペアを作り、値が小さい順に並べ替える
for i in range(n): # (※問題文は1始まりなので、i+1 にしています)
    ball_list.append((a[i], i + 1))
ball_list.sort() # 値が小さい順に並ぶ
top_balls = ball_list[:6]# 上位6個だけを「最強のスタメン」として確保する！
# 【クエリ処理】
for _ in range(q): # k は使わないので読み飛ばしてもOK
    _ = input() 
    b_set = set(map(int, input().split())) # 取り出したボールの番号を高速化するためにsetにする
    for value, index in top_balls: # スタメン（小さい順）を下から確認していく
        if index not in b_set: # もしこのボールがb_setに入っていなければ
            print(value) # それが絶対に最小値！出力してこのクエリは終了！
            break
