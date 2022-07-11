from random import *


pos_door = 0
width_door = 0
test1 = 1.0
test2 = 0.0

pos_door = float(input("Number between 1 and 0 for position of door:"))
while pos_door >= test1 or pos_door <= test2:
    pos_door = float(input("Number between 1 and 0 for position of door:"))
while width_door >= 1 or width_door <= 0 or width_door+pos_door > 1:
    width_door = float(input("Number between 1 and 0 for width of door:"))
n = int(input("Number of tries:"))

num_of_tries = 0
list_of_tries = []

def move_of_zombie(width, position):
    
    door_begin = position
    door_end = position+width
    zom_pos = random()
    if zom_pos >= door_begin and zom_pos <= door_end:
        return True
    else:
        return False
for i in range(n):
    while move_of_zombie(pos_door, width_door) == False:
        num_of_tries = num_of_tries+1

print(num_of_tries)