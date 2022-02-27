# imports
from turtle import *
from sympy import *

# inputs
fx = input("Put in f(x) =")
xo = int(input("assumed x0 = "))

# differentiation of the function
x = Symbol('x')
y = eval(fx)
ydiff = y.diff(x)

# calculation
xn = xo
xn = xn - ()
