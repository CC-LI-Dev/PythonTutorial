from random import * 
from turtle import *

pos_door = float(input("Position Tür (zwischen 1 & 0):"))
while pos_door < 0 or pos_door >= 1:
    pos_door = float(input("Position Tür (zwischen 1 & 0):"))
width_door = float(input("Breite Tür (zwischen 1 & 0 sowie Breite plus Position kleiner 1):"))
while 