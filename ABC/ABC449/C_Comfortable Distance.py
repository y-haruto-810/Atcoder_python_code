# TLEのコードその１
n,l,r = map(int,input().split())
s = input()
count = 0
for i in range(n) :
    for j in range(i+l,min(i+r+1,n)) :
        if s[i] == s[j] :
            count += 1
print(count)
# TLEのコードその２
n,l,r = map(int,input().split())
s = input()
kazu = 0
for i in range(n) :
    if i+l >= n :
        break
    kazu += s[i+l:min(i+r+1,n)].count(s[i])
print(kazu)

# 素のpythonだけで書いた尺取り法を使ったコード
n, l, r = map(int, input().split())
s = input()
window_count = {} # 普通の辞書を用意する
for char in "abcdefghijklmnopqrstuvwxyz": # a〜z までのキーを作って全部 0 を入れておく
    window_count[char] = 0
ans = 0
left = l
right = l - 1  # 最初は枠の中身を空っぽにしておく
for i in range(n):
    target_left = i + l # 今の i に対して、枠の正しい左端と右端を計算
    target_right = min(i + r, n - 1)
    if target_left >= n: # 枠の左端が文字列の最後まで行っちゃったら終了
        break
    while right < target_right: # 枠の右端を広げて新しく入ってきた文字をカウントに足す
        right += 1
        window_count[s[right]] += 1
    while left < target_left: # 枠の左端を縮めてハミ出た文字をカウントから減らす
        window_count[s[left]] -= 1
        left += 1 
    ans += window_count[s[i]] # 枠の中の文字のカウントを足す！
print(ans)

# collectionsのdefaultdictを使ったコード
from collections import defaultdict
n, l, r = map(int, input().split())
s = input()
window_count = defaultdict(int) # ウィンドウ（枠）の中にある文字の個数を記録する辞書
ans = 0
left = l
right = l - 1  # 最初は枠の中身を空っぽにしておく
for i in range(n):
    target_left = i + l # 今の i に対して枠の正しい左端と右端を計算
    target_right = min(i + r, n - 1)
    if target_left >= n: # 枠の左端が文字列の最後まで行っちゃったら終了
        break
    while right < target_right: # 枠の右端を広げて新しく入ってきた文字をカウントに足す
        right += 1
        window_count[s[right]] += 1
    while left < target_left:  # 枠の左端を縮めてハミ出た文字をカウントから減らす
        window_count[s[left]] -= 1
        left += 1
    ans += window_count[s[i]] # 枠の中の文字のカウントが完璧に更新されたので
print(ans) # 今の文字 s[i] と同じものが枠内に何個あるか足すだけ

# 上のコードにbisectを追加したコード
from collections import defaultdict
from bisect import bisect_left, bisect_right
n, l, r = map(int, input().split())
s = input()
pos = defaultdict(list) # アルファベットごとに、出現するインデックス(場所)を記録する辞書
for i in range(n):
    pos[s[i]].append(i)
ans = 0
for i in range(n):
    left = i + l # 探したい範囲の左端と右端
    right = i + r
    target_list = pos[s[i]] # 今の文字が記録されているリストを取得
    count = bisect_right(target_list, right) - bisect_left(target_list, left)
    ans += count # 範囲内に何個の数字があるか一瞬で出る
print(ans)
