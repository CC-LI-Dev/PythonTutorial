from turtle import *
#shape("turtle")
#left(90)
#forward(100)
#right(90)
#forward(100)
#right(90)
#forward(100)
#right(90)
#forward(100)
#right(135)
#forward(141.4213562)
#left(90)
#forward(70.71067812)
#left(90)
#forward(70.71067812)
#left(90)
#forward(141.4213562)



shape("turtle")
speed(3)
left(90)
for i in range(10):
    forward(100-i*10)
    left(90)
    forward(100-i*10)
    left(90)
    forward(100-i*10)
    left(90)
    forward(100-i*10)
    
    penup()
    left(180)
    forward(5)
    right(90)
    forward(5)
    pendown()
    
    
    
