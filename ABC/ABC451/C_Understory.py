# TLEのコード
import sys
input = sys.stdin.readline
q = int(input())
tree = []
tree_len = 0
newtree = []
for i in range(q) :
    num,h = map(int,input().split())
    if num == 1 :
        tree.append(h)
        tree_len += 1
        print(tree_len)
    elif num == 2 :
        for n in range(tree_len) :
            if tree[n] > h :
                newtree.append(tree[n])
        tree = newtree
        newtree = []
        tree_len = len(tree)
        print(tree_len)
        
# setでうまくやろうとしたもののWAになったコード
import sys
input = sys.stdin.readline
q = int(input())
tree = set()
tree_len = 0
newtree = set()
for i in range(q) :
    num,h = map(int,input().split())
    if num == 1 :
        tree.add(h)
        tree_len += 1
        print(tree_len)
    elif num == 2 :
        for n in tree : 
            if n > h :
                newtree.add(n)
        tree = newtree
        newtree = set()
        tree_len = len(tree)
        print(tree_len)

# 正解のコード
import sys
import heapq # 新しい魔法をインポート
input = sys.stdin.readline# 30万回のクエリが来るので爆速入力は必須
q = int(input()) # ただのリストを用意しますが heapq の魔法をかけることでヒープとして使えます
trees = [] 
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1: # クエリ1：高さ h の木を追加する
        h = query[1]
        heapq.heappush(trees, h) # 魔法の箱に追加
    else: # クエリ2：高さ h 以下の木をすべて削除する
        h = query[1]
        while trees and trees[0] <= h: # trees が空っぽじゃなくて、かつ「一番低い木(trees[0])」が h 以下である限り…
            heapq.heappop(trees) # その木を切り倒す（箱から取り出す）
    print(len(trees)) # 今残っている木の本数は、リストの長さを出力するだけでOK
    