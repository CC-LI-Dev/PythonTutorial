import random

while True:
    count = 0
    i = 3
    guess = int(input("Tipp?"))
    
    while i > 0:
        ranNum = random.randint(1,6)
        if ranNum == guess:
            count = count+1
        i = i-1
    if count == 0:
        print("Sie müssen 1 Euro hineinlegen.")
    elif count == 1:
        print("Sie bekommen 1 Euro.")
    elif count == 2:
        print("Sie bekommen 2 Euro.")
    elif count == 3:
        print("Sie bekommen 5 Euro.")
