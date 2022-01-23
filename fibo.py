from turtle import *
import math
pen = Turtle()
pen.pencolor("green")
pen.speed(0)
runtime = 20
magnitude = 5

def fibongui(runtime):
    x = 0
    y = 1
    xr = x
    yr = y

    #first square
    pen.forward(y * magnitude)
    pen.left(90)
    pen.forward(y * magnitude)
    pen.left(90)
    pen.forward(y * magnitude)
    pen.left(90)
    pen.forward(y * magnitude)

    # Fibonacci-Calculation
    h = yr
    yr = xr+yr
    xr = h

    #fibonacci squares


    for i in range(1, runtime):
        pen.backward(xr * magnitude)
        pen.right(90)
        pen.forward(yr * magnitude)
        pen.left(90)
        pen.forward(yr * magnitude)
        pen.left(90)
        pen.forward(yr * magnitude)

        # Fibonacci-Calculation 2
        h = yr
        yr = xr+yr
        xr = h

    # pen to origin & color switch
    pen.penup()
    pen.setposition(magnitude,0)
    pen.seth(0)
    pen.pendown()

    pen.pencolor("red")

    #drawing spiral
    pen.left(90)
    for i in range(runtime):
        move = math.pi * y * magnitude / 2
        move = move / 90
        for j in range(90):
            pen.forward(move)
            pen.left(1)
        h = x
        x = y
        y = h+x



fibongui(runtime)