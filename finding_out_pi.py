from math import *
from turtle import *

magnitude = 200

speed(10)
n = 200
x = 1/n
top_sum = 0
bottom_sum = 0
def function_of_cricle(step_n, color_of_turtle): 
    y = sqrt(1-(step_n/n)**2)

    if color_of_turtle == True:
        color("red")
    elif color_of_turtle == False:
        color("black")

    for i in range(2):
        fd(x*magnitude)
        lt(90)
        fd(y*magnitude)
        lt(90)
    
    


    return y



for i in range(n):
    top_sum = top_sum+(x*function_of_cricle(i+1, False))
    bottom_sum = bottom_sum+(x*function_of_cricle(i, True))
    fd(x*magnitude)
penup() 
goto(0,0)
seth(0)
pendown()

#for i in range(n+1):
#    bottom_sum = bottom_sum+(x*function_of_cricle(i, True))

top_sum = 4*top_sum
bottom_sum = 4*bottom_sum

pi = (top_sum+bottom_sum)/2
print(pi)