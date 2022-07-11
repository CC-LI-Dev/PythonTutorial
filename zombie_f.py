from random import *
from turtle import *
magnitude = 20
anzahl = 1000
speed(0)

t_pos = 0.5
t_br = 0.01
n = 2000
ges = []
ges = [0] * anzahl

#Eingabe
#t_pos = float(input("Tür Position (zwischen null und eins)"))
#while t_pos >= 1.0 or t_pos <= 0.0:
#    t_pos = float(input("Tür Position (zwischen null und eins)"))
#t_br = float(input("Tür Breite (zwischen null und eins)"))
#while t_br >= 1.0 or t_br <= 0.0 or t_pos + t_br >= 1.0:
#    t_br = float(input("Tür Breite (zwischen null und eins)"))

t_end = t_pos + t_br


#Verarbeitung
for i in range(n):
    leben = False
    v = 0
    while leben == False:
        v = v + 1
        zom_pos = random()
        if zom_pos > t_pos and zom_pos < t_end:
            leben = True
    ges[v] = ges[v] + 1
    
#Ausgabe
#print(ges)-400, -300
#setworldcoordinates(0, 0, -700, -500)

setup(width = 1500, height = 710, startx = None, starty = None)
setworldcoordinates(-750, -360, 750, 360)
width(1500/anzahl)
penup()
goto(-750, -360)
pendown()
fd(1500)
goto(-750, -360)
lt(90)
fd(710)
goto(-750, -360)
seth(0)
color("purple")

for i in range(len(ges)):
    fd(1)
    lt(90)
    fd(ges[i]*magnitude)
    backward(ges[i]*magnitude)
    seth(0)
