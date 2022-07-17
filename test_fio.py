from os import WUNTRACED


wurf = [1,3,2,4,2]

wurf.sort() # Funktioniert bei dir nur mit wurf = wurf.sort()

zahl1 = wurf.count(1)
zahl2 = wurf.count(2)
zahl3 = wurf.count(3)
zahl4 = wurf.count(4)
zahl5 = wurf.count(5)
zahl6 = wurf.count(6)

wurfstr = []
pges = 0

for i in wurf:
    if i not in wurfstr:
        wurfstr.append(i)


fullhouse = False
dreierp = False
viererp = False
chance = False
klstr = False
grstr = False
kniffel = False

wertung = str(input("Was willste werten?"))
if wertung == "full house" and fullhouse == False and (zahl1 == 3 or zahl2 == 3 or zahl3 == 3 or zahl4 == 3 or zahl5 == 3 or zahl6 == 3) and (zahl1 == 2 or zahl2 == 2 or zahl3 == 2 or zahl4 == 2 or zahl5 or zahl6 == 2):
    pges == pges + 25
    fullhouse = True
elif wertung == "dreier pasch" and dreierp == False and (zahl1 >= 3 or zahl2 >= 3 or zahl3 >= 3 or zahl4 >= 3 or zahl5 >= 3 or zahl6 >= 3):
    pges == pges + sum(wurf)
    dreierp = True
elif wertung == "vierer pasch" and viererp == False and (zahl1 >= 4 or zahl2 >= 4 or zahl3 >= 4 or zahl4 >= 4 or zahl5 >= 4 or zahl6 >= 4):
    pges == pges + sum(wurf)
    dreierp = True
elif wertung == "kleine straße" and klstr == False:
    pges == pges + sum(wurf)
    dreierp = True


