from turtle import *
speed(1)
def rek(depth, s):
    if depth == 0:
        return
    else:
        fd(s)
        rt(45)
        rek(depth-1, s/2)
        lt(45)
        backward(s)
        
        fd(s)
        lt(45)
        rek(depth-1,s/2)
        rt(45)
        backward(s)
        
        

lt(90)
rek(5, 200)