# 正解のより良いコード
n = int(input())
a = list(map(int,input().split()))
toukou = [0]*n
num = 1
for i in a :
    toukou[i-1] = num 
    num += 1
print(*toukou)
# ８分半でAC

# よくあるコード
n = int(input())
a = list(map(int, input().split()))
students = [] # (登校した順番, 出席番号) を入れるリスト
for i in range(n):
    students.append((a[i], i + 1)) # a[i] が順番、i+1 が出席番号
students.sort() # 順番を基準にソート（並び替え）
ans = [] # 答えを入れるリスト
for order, student_id in students:
    ans.append(student_id)
print(*ans)
