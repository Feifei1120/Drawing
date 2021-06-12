from turtle import *
from random import *
from math import *

def tree(n,l):
    pd()

    t = cos(radians(heading()+45))/8 +0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)

    if n >0 :
        b = random()*15 + 10
        c = random()*15 + 10
        d = l*(random()*0.25+0.7)

        right(b)
        tree(n-1,d)
        left(b+c)
        tree(n-1,d)
        right(c)
    else:
        pass

bgcolor (0.5,0.5,0.5)
ht()
speed(10)
tracer(0,0)
pu()
backward(100)
