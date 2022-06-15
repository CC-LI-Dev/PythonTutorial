from turtle import *
from math import *
#speed(1)


def polygon_tri_draw(n, a):
    # degree calculations
    deg_tri = 360 / n
    deg_s = (180-deg_tri) / 2
    s = (a/2) / sin(radians(deg_tri/2)) 
    for i in range(n):
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
        

polygon_tri_draw(5, 100)