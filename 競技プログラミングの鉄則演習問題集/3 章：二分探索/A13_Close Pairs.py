# a[mid-1] - a[i-1] の条件間違いを修正してACしたコード 
n,k = map(int,input().split())
a = list(map(int,input().split()))
num = 0
for i in range(1,n+1) :
    ans = 0
    left = i+1
    right = n
    while left <= right :
        mid = (left + right) // 2
        if a[mid-1] - a[i-1] > k :
            right = mid - 1
        else :
            ans = mid - i
            left = mid + 1
    num += ans
print(num)

# 尺取り法を使ったコード
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
right = 0
current_sum = 0 # 今見ている区間の合計値
for left in range(n): # 左端(left) を 0 から N-1 まで順番に進めていく
# 【ステップ1】右端(right)を伸ばせるだけ伸ばす
    while right < n and current_sum + a[right] <= k: # 配列の最後に到達していない ＆ 次の数字を足しても K 以下である
        current_sum += a[right]
        right += 1
# 【ステップ2】条件を満たす区間の長さを答えに足す
    ans += (right - left) # right は「条件を満たさなかった最初の場所」を指しているので引き算だけで個数が出る
# 【ステップ3】左端(left)を1つ進める準備
    if right == left: 
        right += 1 # もし右端と左端が同じ場所にいたら、右端も一緒に1つ進める（追い越し防止）
    else:
        current_sum -= a[left] # 今の左端の数字を、合計値からポイッと捨てる
print(ans)
