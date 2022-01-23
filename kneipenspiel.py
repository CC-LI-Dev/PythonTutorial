import random
balance = 0
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
        balance = balance-1
        print("Sie müssen 1 Euro hineinlegen.")
    elif count == 1:
        balance = balance+1
        print("Sie bekommen 1 Euro.")
    elif count == 2:
        balance = balance+2
        print("Sie bekommen 2 Euro.")
    elif count == 3:
        balance = balance+5
        print("Sie bekommen 5 Euro.")

    balance = 0
    