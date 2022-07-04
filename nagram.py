from turtle import *
from math import *
speed(5)
bgcolor("black")
color("red")
x = 0
def nagram(n, a):
    global x

    # calculation of interior angle & drawing of hexagram
    if n == 6:
        #hexagram
        dist_to_start_hex = (a/2) / cos(radians(30))
        penup()
        lt(180-30)
        fd(dist_to_start_hex)
        seth(0)
        pendown()
        fd(a)
        rt(180-60)
        fd(a)
        rt(180-60)
        fd(a)
        penup()
        goto(0,0)
        seth(0)
        rt(180-30)
        fd(dist_to_start_hex)
        seth(0)
        pendown()
        fd(a)
        lt(180-60)
        fd(a)
        lt(180-60)
        fd(a)     
        return "Done"
    elif n % 2 != 0:
        deg_nagram = 360 / (2*n)
    elif (n/2)%2 != 0:
        deg_nagram = 360 / (n/2)
    elif (n/2)%2 == 0:
        deg_nagram = 360 / n
    
    
    # calculation of distance from 0,0 to begin poitn
    dist_to_start = (a/2) / cos(radians(deg_nagram/2))
    # centralization of shape / move to begin point
    penup()
    lt(180-(deg_nagram/2))
    fd(dist_to_start)
    seth(0)
    pendown()

    #drawing process
    for i in range(n):
        fd(a)
        rt(180-deg_nagram)

        
nagram(8, 350)
