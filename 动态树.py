import turtle as T
import random
import time


# 画樱花的躯干(60,t)
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 12 <= branch <= 14:
            if random.randint(0, 2) == 0:
                t.color('snow') 
            else:
                t.color('lightcoral') 
            t.pensize(branch / 2.5)
        elif branch < 12:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral') 
            t.pensize(branch / 1.5)
        else:
            t.color('dimgray') 
            t.pensize(branch / 10) 
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()
# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral') # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

def main():
    # 绘图区域
    t = T.Turtle()
    # 画布大小
    w = T.Screen()
    t.hideturtle() # 隐藏画笔
    t.getscreen().tracer(5, 0)
    w.screensize(1000,1000,bg='silver') # 银灰色
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('dimgray')
    # 画樱花的躯干
    Tree(60, t)
    # 掉落的花瓣
    Petal(200, t)
    w.exitonclick()
main()
