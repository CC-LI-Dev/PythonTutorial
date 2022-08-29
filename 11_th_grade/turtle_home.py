from turtle import *
import math
speed(10)
x = 0
def polygon(n, a):
    global x
    for i in range(a): 
        fd(n)
        lt(360/a)
        
    
    x = x+10
    lt(45)
    polygon(x, 6)
polygon(50, 6)



def circle(r, deg):
    degNew = 360 / deg
    for i in range(1):
            move = 2*math.pi * r / degNew
            move = move / deg
            for j in range(deg):
                forward(move)
                left(1)

#circle(100, 180)

