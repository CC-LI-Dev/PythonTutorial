from turtle import *
from math import *
speed(10)

def tri_fun():
    width(2)
    bgcolor("black")
    color_number = 0 
    col = ["", "red", "orange", "yellow", "green", "blue", "purple"]
        
        
            
    x = 20
    for i in range(500):
        if color_number == 6:
            color_number = 0
        color_number =  color_number +1
        
        print(color_number)
        color("white")
        r = (x/2) / cos(radians(30))
        penup()
        fd(r)
        pendown()
        lt(180-30)
        fd(x)
        lt(180-60)
        fd(x)
        lt(180-60)
        fd(x)
        penup()
        seth(0)
        goto(0,0)
        lt(i*5)
        pendown()
        

        x = x + 20


tri_fun()
