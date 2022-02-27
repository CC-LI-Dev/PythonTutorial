from random import *
amount = 0
balance = 0
while True:

    while amount < 100:
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        num3 = randint(1, 9)
        print("Numbers", " ", num1, " ", num2, " ", num3)
        pick = int(input("Wich number do you want?"))
        amount = amount+pick
        print("Your number is:", amount)

        if amount == 100:
            print("You won. Your balance will be updated")
            print(" ")
            print("The game restarts...")
            balance = balance+100
            break
        elif amount > 100:
            print("You lost. Your balance will be updated.")
            print(" ")
            print("The game restarts...")
            balance = balance-(amount-100)

    amount = 0
    