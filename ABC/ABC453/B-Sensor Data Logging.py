
T,x = map(int,input().split())
A = list(map(int,input().split()))
t = []
a = []
for i in range(T+1) :
    if i == 0 :
        t.append(0)
        a.append(A[0])
    elif abs(a[-1] - A[i]) >= x : # ここを10にしていたからWAになっていた
        t.append(i)
        a.append(A[i])
for j in range(len(t)) :
    print(t[j],a[j])

# プロのPythonicな書き方したコード
T,x = map(int,input().split())
A = list(map(int,input().split()))
t = []
a = []
for i in range(T+1) :
    if i == 0 :
        t.append(0)
        a.append(A[0])
    elif abs(a[-1] - A[i]) >= x :
        t.append(i)
        a.append(A[i])
for time, val in zip(t, a):
    print(time, val)

# その場で出力するコード
T, x = map(int, input().split())
A = list(map(int, input().split()))
print(0, A[0]) # 時刻0は確定で出力し、「最後に保存した値」として記録
last_saved = A[0]
for i in range(1, T + 1): # 時刻1から順番にチェック
    if abs(last_saved - A[i]) >= x:
        print(i, A[i])        # 条件を満たしたらその場で出力
        last_saved = A[i]     # 「最後に保存した値」を更新
