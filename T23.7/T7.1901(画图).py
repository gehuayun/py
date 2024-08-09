print("""
实例056:画圈
题目 画图,学用circle画圆形。
""")

from tkinter import *

canvas = Canvas(width=500, height=500, bg='yellow')     # 页面大小 500*500  背景颜色 黄色
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(26):
    canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
    k += j
    j += 0.3
mainloop()

print("""
实例057:画线
题目 画图,学用line画直线。
""")

if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=500, height=500, bg='green')      # 页面大小 300*300  背景颜色 绿色
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()

print("""
实例058:画矩形
题目 画图,学用rectangle画方形。
""")

if __name__ == '__main__':
    from tkinter import *

    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=500, height=500, bg='yellow')
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()

print("""
实例059:画图(丑)
题目 画图，综合例子
""")

if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
    import math

    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='red')
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
    mainloop()


print("网络图形")
import math
from tkinter import *


class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0


points = []


def LineToDemo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width=screenx, height=screeny, bg='white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius, ycenter - radius,
                       xcenter + radius, ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y)

    canvas.pack()
    mainloop()


if __name__ == '__main__':
    LineToDemo()
