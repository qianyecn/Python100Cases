# 导入turtle包的所有内容:
from turtle import *

def haigui():
    # 设置笔刷宽度:
    width(4)

    # 前进:
    forward(200)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)


    pencolor('red')
    right(180)
    forward(150)
    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()

def wujiaoxing():  
    def drawStar(x, y):
        pu()
        goto(x, y)
        pd()
        # set heading: 0
        seth(0)
        for i in range(5):
            fd(40)
            rt(144)

    for x in range(0, 250, 50):
        drawStar(x, 0)

    done()

r = 0
g = 0
b = 0
def fenxingshu():
    colormode(255)

    lt(90)

    lv = 14
    l = 120
    s = 45

    width(lv)


    pencolor(r, g, b)

    penup()
    bk(l)
    pendown()
    fd(l)

    def draw_tree(l, level):
        global r, g, b
        # save the current pen width
        w = width()

        # narrow the pen width
        width(w * 3.0 / 4.0)
        # set color:
        r = r + 1
        g = g + 2
        b = b + 3
        pencolor(r % 200, g % 200, b % 200)

        l = 3.0 / 4.0 * l

        lt(s)
        fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        bk(l)
        rt(2 * s)
        fd(l)

        if level < lv:
            draw_tree(l, level + 1)
        bk(l)
        lt(s)

        # restore the previous pen width
        width(w)
        print(r,g,b)
    speed("fastest")

    draw_tree(l, 4)

    done()
def hua():
    win_w=600
    win_h=100
    # 初始化画布
    # screensize(win_w, win_h, "green")
    colormode(255)
    # 初始化画布 startx y表示矩形窗口左上角顶点的位置
    setup(width=600, height=500, startx=0, starty=0,)
    width(4)
    # 画笔尺寸
    pensize(0)
    #设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快
    speed(5)
    penup()
    # goto(-win_w/2,-win_h/2)
    #forward(100)
    write("文字",font=('', 40, 'normal'))
    pendown()
    circle(50)
    circle(50,steps=3) 
    circle(120, 180)
    left(90)
    forward(100)
    done()


if __name__=='__main__':
    hua()