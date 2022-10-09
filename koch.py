from turtle import *
speed(0)
def koch(n, size):

    if n == 0:
        forward (size)

    else:
        koch (n-1, size) 
        left (60)
        koch (n-1, size)
        right (120)
        koch (n-1, size) 
        left (60)
        koch (n-1, size)

penup()
goto (-200, 200)
pendown() 
for i in range(3):
    koch (4,3)
    right(120)