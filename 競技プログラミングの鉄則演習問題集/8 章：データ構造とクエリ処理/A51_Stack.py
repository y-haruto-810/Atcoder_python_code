
# numによってmojiがあるか変わるためエラーになるコード
q = int(input())
book = []
for i in range(q) :
    num,moji = input().split()
    if int(num) == 1 :
        book.append(moji)
    elif int(num) == 2 :
        print(book[-1])
    elif int(num) == 3 :
        del book[-1]

# numとmojiをlistで受け取ることでエラーを回避するコード
q = int(input())
book = []
for i in range(q) :
    num_moji = list(input().split()) # num_moji = input.split()で良い
    if int(num_moji[0]) == 1 :
        book.append(num_moji[1])
    elif int(num_moji[0]) == 2 :
        print(book[-1])
    elif int(num_moji[0]) == 3 :
        del book[-1]
