from turtle import *
from math import *
speed(10)
bgcolor("black")
color("red")
def nagram(n, a):
    if n % 2 != 0:
        deg_nagram = 360 / (2*n)
    elif (n/2)%2 != 0:
        deg_nagram = 360 / (n/2)
    elif (n/2)%2 == 0:
        deg_nagram = 360 / n
        print("ok")
    
    dist_to_start = (a/2) / cos(radians(deg_nagram/2))
    penup()
    lt(180-(deg_nagram/2))
    fd(dist_to_start)
    seth(0)
    pendown()
    for i in range(n):
        fd(a)
        rt(180-deg_nagram)
        
nagram(11, 350)
