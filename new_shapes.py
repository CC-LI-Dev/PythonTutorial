from turtle import *
from math import *
speed(10)


def polygon_tri_draw(n, a):
    num_of_turns = 1
    # degree calculations
    deg_tri = 360 / n
    deg_s = (180-deg_tri) / 2
    s = (a/2) / sin(radians(deg_tri/2)) 
    for i in range(n):
        fd(s)
        lt(180-deg_s)
        fd(a)
        lt(180-deg_s)
        fd(s)
        goto(0,0)
        seth(0)
        #reset()
        lt(deg_tri*num_of_turns)
        num_of_turns += 1


        #fd(a)
        #lt(180-deg_s)
        #fd(s)
        #rt(180)
        #fd(s)
        #lt(180-deg_s)
    
        #fd(s)
        #lt(180-deg_s)
        #fd(a)
        #lt(180-deg_s)
        #fd(s)
        #lt(180)
        #lt(deg_tri)
    a_len = a + 20
    n_up = n  

    polygon_tri_draw(n_up,a_len)        

polygon_tri_draw(5, 100)