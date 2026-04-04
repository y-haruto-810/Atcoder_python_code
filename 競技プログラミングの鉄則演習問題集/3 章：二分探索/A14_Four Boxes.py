# ヒントをもらってACしたコード
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
ab_set = set()
cd_set = set()
for i in a:
    for j in b:
        ab_set.add(i+j)
for i in c:
    for j in d:
        cd_set.add(i+j)
cd_list = list(cd_set)
cd_list.sort()
for ab in ab_set:
    left = 1 
    right = len(cd_list)
    while left <= right:
        mid = (left+right)//2
        if k == cd_list[mid-1] + ab :
            print("Yes")
            exit()
        elif k < cd_list[mid-1] + ab :
            right = mid - 1
        else:            
            left = mid + 1
print("No")

# bisectモジュールを使ったコード
import bisect
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
ab_set = set()
cd_set = set()
for i in a:
    for j in b:
        ab_set.add(i+j)
for i in c:
    for j in d:
        cd_set.add(i+j)
cd_list = list(cd_set)
cd_list.sort()
for ab in ab_set:
    target = k - ab # 探したい数字（Kから、今のabを引いた残り）
    idx = bisect.bisect_left(cd_list, target) # cd_list の中に target があるか、bisectで一瞬で探す
    if idx < len(cd_list) and cd_list[idx] == target: # 見つかった場所(idx)の数字が、本当に target と同じかチェック
        print("Yes")
        exit()
print("No")
