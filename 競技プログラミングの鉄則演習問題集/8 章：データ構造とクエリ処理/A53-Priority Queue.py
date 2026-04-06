# 工夫してACにしたがTLEになりやすいコード
q = int(input())
price = []
num = input().split()
price.append(int(num[1]))
min_price = price[0]
for _ in range(q-1):
    num = input().split()
    if num[0] == '1':
        price.append(int(num[1]))
        if int(num[1]) < min_price:
            min_price = int(num[1])
    elif num[0] == '2':
        print(min_price)
    elif num[0] == '3':
        price.remove(min_price)
        if price != []:
            min_price = min(price)
        else:
            min_price = 1000000

# heapqを使ったTLEになりにくいコード
import heapq
q = int(input())
price = [] # 普通のリストを用意しますが、操作は heapq に任せます
for _ in range(q):
    num = input().split()
    if num[0] == '1':
        heapq.heappush(price, int(num[1])) # 自動で「一番小さいやつ」が先頭に来るように入れてくれる
    elif num[0] == '2':  # 常に hq[0] が最小値になっているから探す必要なし
        print(price[0])
    elif num[0] == '3': # 一番小さいやつを消して、次に小さいやつを自動で先頭に持ってくる
        heapq.heappop(price)
