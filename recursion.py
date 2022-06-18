from dis import dis
from turtle import *
speed(0)
def rek(dist, depth):
    if depth == 0:
        return
    else:
        fd(dist)
        rek(dist/2, depth-1)
        backward(dist)
        lt(120)

        fd(dist)
        rek(dist/2, depth-1)
        backward(dist)
        lt(120)

        fd(dist)
        rek(dist/2, depth-1)
        backward(dist)
        lt(120)

      
rek(50, 5)
