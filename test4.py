from turtle import *
import math
fd(110)
goto(0,0)
lt(90)
fd(110)
penup()
goto(100,0)
pendown()
circle(100, extent=90)

goto(0,0)
seth(90)

n = 20
x = 0



for i in range(n):
    
    fd(math.sqrt(100-x*x))
    
