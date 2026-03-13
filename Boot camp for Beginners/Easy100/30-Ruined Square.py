x1,y1,x2,y2 = map(int,input().split())
x3,y3 = x2-(y2-y1),y2+(x2-x1)
x4,y4 = x1-(y2-y1),y1+(x2-x1)
print(x3,y3,x4,y4)
# 約２４分でAC

# 綺麗なコード
x1, y1, x2, y2 = map(int, input().split())
dx = x2 - x1 # 頂点1から頂点2への移動量 (dx, dy)
dy = y2 - y1
x3, y3 = x2 - dy, y2 + dx # 90度回転させた移動量は(-dy, dx)だからそれを足すだけ
x4, y4 = x1 - dy, y1 + dx 
print(x3, y3, x4, y4)
