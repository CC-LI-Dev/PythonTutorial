from turtle import *
shape("turtle")
speed(0)
for i in range(21):
    goto(300,0-i*20)
    penup()
    goto(300, 0)
    pendown()
    goto(0,0-i*20)
    penup()
    goto(0, 0)
    pendown()

for i in range(30):
    pencolor("red")
    penup()
    goto(-200, 200)
    pendown()
    goto(200,200-i*10)

for i in range(30):
    pencolor("red")
    penup()
    goto(200, 200)
    pendown()
    goto(-200,200-i*10)

import time
from turtle import *

def recurse(n):
    if n>0:
        left(10)
        forward(5)
        recurse(n-1)

recurse(200)
time.sleep(5)